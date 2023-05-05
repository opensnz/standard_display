import os, sys, json, signal
from modules.remoteClient import remoteClientClass
from sys import platform

sys.tracebacklimit = 0

os.environ["REMOTE_SERVER"] = "http://192.168.4.167:8000/"
if platform == "linux" or platform == "linux2":
    os.environ["GUI_DIR"] = "/home/pi/standard_display/Player/gui/"
    os.environ["BACKEND_DIR"] = "/home/pi/standard_display/Player/backend/"
elif platform == "win32":
    os.environ["GUI_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/gui/"
    os.environ["BACKEND_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/backend/"

def get_player_uiid() -> str:
    path = os.getenv('BACKEND_DIR') + "config/player.json"
    if os.path.exists(path):
        try :
            with open(path, "r") as file:
                data = json.load(file)
                if data["player"]["uuid"] != "":
                    return data["player"]["uuid"]
            return ""
        except:
            return ""
    else :
        return ""

def handler(signum, frame):
    print("Exiting...")
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    remoteClient = remoteClientClass(get_player_uiid())
    remoteClient.main()



