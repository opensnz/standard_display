# Constants for MQTT
MQTT_BROKER    = "localhost"
MQTT_PORT      = 1883
MQTT_USERNAME  = "gui"
MQTT_PASSWORD  = "gui#2023"

MQTT_TOPIC_GUI_IN    = "/gui/data/in"
MQTT_TOPIC_GUI_OUT   = "/gui/data/out"

class TYPE(enumerate):
    PLAYER = "player"
    PLAYLIST = "playlist"
    ACTIVATION = "activation"
    SCREENSHOT = "screenshot"
    TELEMETRY = "telemetry"
    REBOOT = "reboot"
    POWER = "power"
    IMAGE = "image"
    ERROR = "error"