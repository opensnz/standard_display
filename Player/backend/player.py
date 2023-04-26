import os, sys, json, signal
from modules.remoteClient import remoteClientClass

sys.tracebacklimit = 0

os.environ["GUI_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/gui/"
os.environ["BACKEND_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/backend/"
os.environ["REMOTE_SERVER"] = "http://192.168.4.167:8000/"

def get_uiid() -> str:
    path = os.getenv('BACKEND_DIR') + "config/player.json"
    if os.path.exists(path):
        try :
            with open(path, "r") as file:
                data = json.load(file)
                if data["player"]["uuid"] != "" and data["player"]["activated"] == True:
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
    remoteClient = remoteClientClass(get_uiid())
    remoteClient.main()



