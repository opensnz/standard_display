import paho.mqtt.client as mqtt
import cv2, time, json, os
from modules.constants import *
from sys import platform

if platform == "linux" or platform == "linux2":
    os.environ["GUI_DIR"] = "/home/pi/standard_display/Player/gui/"
    os.environ["BACKEND_DIR"] = "/home/pi/standard_display/Player/backend/"
elif platform == "win32":
    os.environ["GUI_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/gui/"
    os.environ["BACKEND_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/backend/"


classNames = []
classFile = os.getenv("BACKEND_DIR") + "config/coco.names"
FORM_FILE = os.getenv("BACKEND_DIR") + "config/form.json"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = os.getenv("BACKEND_DIR") + "config/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = os.getenv("BACKEND_DIR") + "config/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #cap.set(10,70)

    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img,0.45,0.2)
        for info in objectInfo:
            if info[1] == 'person':
                print(time.time(), "person detected")
                ## Send MQTT message
                payload = None
                mqtt_client = mqtt.Client("detection")
                mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
                with open(FORM_FILE) as file:
                    payload = json.load(file)
                if payload is not None:
                    mqtt_client.publish(topic=MQTT_TOPIC_GUI_IN, payload=json.dumps(payload))
                    time.sleep(10)
        time.sleep(5)