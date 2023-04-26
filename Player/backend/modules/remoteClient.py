import websocket, threading
import paho.mqtt.client as mqtt
from modules.handler import Handler
from modules.constants import *
import json, time

BACKEND_REMOTE_SERVER = 'ws://192.168.4.167:8000/player/'

class remoteClientClass:
    
    def __init__(self, uiid : str):
        self.__uiid = uiid
        self.__socket : websocket.WebSocketApp = None
        self.__thread : threading.Thread = None
        self.__handler = Handler()
        self.__mqtt_client = mqtt.Client(transport="tcp",client_id="backend")
        
    def __setup__(self):
        self.__mqtt_client.on_connect    = self.__mqtt_on_connect__
        self.__mqtt_client.on_message    = self.__mqtt_on_message__
        self.__mqtt_client.on_disconnect = self.__mqtt_on_disconnect__
        self.__mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.__mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
        self.__ws_run__()
        
    def __loop__(self):
        while True:
            time.sleep(3600)
            
    #####################################################################
        
    def __ws_on_open__(self, ws : websocket.WebSocketApp):
        print("Remote connexion openned")
        
    def __ws_on_message__(self, ws, message):
        print("message : ", message)
        response = self.__handler.handle(message)
        print("response : ", response)
        self.__publish__(response)
        
        
    def __ws_on_error__(self, ws : websocket.WebSocketApp, exception):
        print(exception)
        ws.close()
        
    def __ws_on_close__(self, ws : websocket.WebSocketApp, close_status_code, close_msg):
        print(close_status_code, close_msg)
        # reconnect after 100 milliseconds
        threading.Timer(0.1, self.__ws_reconnect__).start()
        
    def __ws_run__(self):
        self.__socket = websocket.WebSocketApp(BACKEND_REMOTE_SERVER+self.__uiid,
                                        on_open=self.__ws_on_open__,
                                        on_message=self.__ws_on_message__,
                                        on_error=self.__ws_on_error__,
                                        on_close=self.__ws_on_close__)
        self.__thread = threading.Thread(target=self.__socket.run_forever)
        self.__thread.daemon = True
        self.__thread.start()  
    
    def __ws_reconnect__(self):
        self.__ws_run__()
        
    def __ws_send__(self, message : str):
        self.__socket.send(message)
        

    #######################################################################################
     

    def __mqtt_on_message__(self,  client:mqtt.Client, userdata, message:mqtt.MQTTMessage):
        print("MQTT_Message received")
        topic = message.topic
        if topic == MQTT_TOPIC_GUI_OUT:
            data = json.loads((b''+message.payload).decode())
            print(data)
            # Send to remote server

    def __mqtt_on_connect__(self, client:mqtt.Client, userdata, flags, rc):
        print("MQTT_Client connected")
        client.subscribe(MQTT_TOPIC_GUI_OUT)


    def __mqtt_on_disconnect__(self, client:mqtt.Client, userdata, rc):
        print("MQTT_Client disconnected")
        client.reconnect()
    
    
    def __publish__(self, message:str):
        """Publish Message"""
        self.__mqtt_client.publish(MQTT_TOPIC_GUI_IN, payload=message)
        
    
    ################################################################################
     
    
    def main(self):
        """ Blocking method """
        try :
            self.__setup__()
            self.__mqtt_client.loop_start()
            self.__loop__()
        except:
            pass
    