from guiPlayer import GuiPlayerClass
import threading
import paho.mqtt.client as mqtt
from constants import *
import json, time

BACKEND_LOCAL_SERVER = "ws://localhost:8080"


class GuiClientClass:
    
    def __init__(self, guiPlayer : GuiPlayerClass):
        self.__guiPlayer : GuiPlayerClass =  guiPlayer
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
    
    
    #################################################################################
    
        
    def __mqtt_on_message__(self,  client:mqtt.Client, userdata, message:mqtt.MQTTMessage):
        print("MQTT_Message received")
        topic = message.topic
        if topic == MQTT_TOPIC_GUI_IN :
            data = json.loads((b''+message.payload).decode())
            if data["type"] == "playlist":
                self.__msg_playlist_handling__(data)
            elif data["type"] == "screenshot":        
                import os, datetime, base64
                path = os.path.join("screenshot_" + datetime.datetime.utcnow().isoformat().replace(':', '-') + ".png")
                with open(path, "wb") as f:
                    f.write(base64.decodebytes(data["screenshot"].encode("utf-8")))
                    data["screenshot"] = path
                    self.__msg_screenshot_handling__(data)

    def __mqtt_on_connect__(self, client:mqtt.Client, userdata, flags, rc):
        print("MQTT_Client connected")
        client.subscribe(MQTT_TOPIC_GUI_IN)


    def __mqtt_on_disconnect__(self, client:mqtt.Client, userdata, rc):
        print("MQTT_Client disconnected")
        client.reconnect()
    
    
    def __publish__(self, message:str):
        """Publish Message"""
        self.__mqtt_client.publish(MQTT_TOPIC_GUI_OUT, payload=message)
      
    def __msg_playlist_handling__(self, message : dict):
        self.__guiPlayer.play_media_list(message["playlist"])
    
    def __msg_screenshot_handling__(self, message : dict):
        self.__guiPlayer.play_media(message["screenshot"])