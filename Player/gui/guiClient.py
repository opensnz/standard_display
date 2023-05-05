from guiPlayer import GuiPlayerClass
import paho.mqtt.client as mqtt
from constants import *
import json, time, os
from guiWelcome import GuiWelcomeClass
from monitor import *

BACKEND_LOCAL_SERVER = "ws://localhost:8080"


class GuiClientClass:
    
    def __init__(self, guiPlayer : GuiPlayerClass = None, guiWelcome : GuiWelcomeClass = None):
        self.__guiPlayer : GuiPlayerClass =  guiPlayer
        self.__guiWelcome : GuiWelcomeClass =  guiWelcome
        self.__mqtt_client = mqtt.Client(transport="tcp",client_id="gui")
        
    def __setup__(self):
        self.__mqtt_client.on_connect    = self.__mqtt_on_connect__
        self.__mqtt_client.on_message    = self.__mqtt_on_message__
        self.__mqtt_client.on_disconnect = self.__mqtt_on_disconnect__
        self.__mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.__mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
        
        
    def run(self):
        """ Launch GUI Client """
        try :
            self.__setup__()
            self.__mqtt_client.loop_start()
        except:
            pass
    
    def __get_current_playlist__(self) -> dict|None:
        path = os.getenv('BACKEND_DIR') + "config/playlist.json"
        if os.path.exists(path):
            try :
                with open(path, "r") as file:
                    return json.load(file)
            except:
                return None
        else :
            return None
    
    
    #################################################################################
    
        
    def __mqtt_on_message__(self,  client:mqtt.Client, userdata, message:mqtt.MQTTMessage):
        print("MQTT_Message received")
        topic = message.topic
        if topic == MQTT_TOPIC_GUI_IN :
            data = json.loads((b''+message.payload).decode()) 
            if data["type"] == TYPE.PLAYER:
                self.__msg_player_handling__(data)
            elif data["type"] == TYPE.ACTIVATION:
                self.__msg_activation_handling__(data)
            elif data["type"] == TYPE.PLAYLIST:
                self.__msg_playlist_handling__(data)
            elif data["type"] == TYPE.IMAGE:
                self.__msg_image_handling__(data)

    def __mqtt_on_connect__(self, client:mqtt.Client, userdata, flags, rc):
        print("MQTT_Client connected")
        client.subscribe(MQTT_TOPIC_GUI_IN)
        if self.__guiWelcome is not None :
            self.__publish__(json.dumps({"type": "player", "player": "gui"}))
        playlist = self.__get_current_playlist__()
        if playlist != None:
            self.__msg_playlist_handling__(playlist)


    def __mqtt_on_disconnect__(self, client:mqtt.Client, userdata, rc):
        print("MQTT_Client disconnected")
        client.reconnect()
    
    
    def __publish__(self, message:str):
        """Publish Message"""
        self.__mqtt_client.publish(MQTT_TOPIC_GUI_OUT, payload=message)
      
    def __msg_player_handling__(self, message : dict):
        if self.__guiWelcome is not None:
            if message["player"]["activated"] == False:
                self.__guiWelcome.display_passcode(message["player"]["passcode"])
                
    def __msg_activation_handling__(self, message : dict):
        self.__guiWelcome.display_activation()
        time.sleep(3)
        self.__guiPlayer = GuiPlayerClass(self.__guiWelcome.root)
        monitor = get_primary_monitor()
        self.__guiPlayer.place(x=0, y=0, width=monitor.width, height=monitor.height)
        self.__guiWelcome.destroy()
    
    def __msg_playlist_handling__(self, message : dict):
        if self.__guiPlayer is not None:
            self.__guiPlayer.play_media_list(message["playlist"])
            
    def __msg_image_handling__(self, message : dict):
        pass