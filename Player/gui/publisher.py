
import paho.mqtt.client as mqtt
import json, time

payload = {
    "type": "form",
    "form": [
        {
            "label":"name"
        },
        {
            "label":"email"
        },
        {
            "label":"telephone"
        }
    ]
}

mqtt_client    = mqtt.Client("test")
mqtt_client.connect("localhost", 1883)

mqtt_client.publish(topic="/gui/data/in", payload=json.dumps(payload))