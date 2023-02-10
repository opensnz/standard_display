import os, json, requests
import io, base64
import subprocess
from PIL import ImageGrab
from modules.telemetry import Telemetry
from modules.downloader import *


class Handler():

    def __init__(self):
        self.__mapping__ = {
            "player": Handler._player,
            "activation": Handler._activation,
            "telemetry": Handler._telemetry,
            "playlist": Handler._playlist,
            "screenshot": Handler._screenshot,
            "reboot": Handler._reboot,
            "power": Handler._power,
        }


    def handle(self, data : str) -> str:
        try:
            data = json.loads(data)
            type = data["type"]
            return self.__mapping__.get(type)(self, data)
        except:
            return self.__error__()
    
    def __error__(self) -> str:
        return json.dumps({"type" : "error", "error":"message not handled"})

    def _player(self, data : dict) -> str:
        path = os.getenv('BACKEND_DIR') + "config/player.json"
        new_player = True
        if os.path.exists(path):
            try:
                with open(path, "r") as file:
                    data.update(json.load(file))
                    if data["player"]["uuid"] != "":
                        new_player = False
            except:
                new_player = True
        if new_player:
            remote_server = os.getenv('REMOTE_SERVER') + "player/new"
            response = requests.get(remote_server, allow_redirects=True)
            data.update(response.json())
            with open(path, "w") as file:
                file.write(json.dumps(data, indent=4))
        return json.dumps(data)
    
    def _activation(self, data : dict) -> str:
        path = os.getenv('BACKEND_DIR') + "config/player.json"
        player = data.pop(data["type"])
        data["type"] = "player"
        data["player"] = player
        with open(path, "w") as file:
            file.write(json.dumps(data, indent=4))
        return json.dumps(data)



    def _telemetry(self, data : dict) -> str:
        data[data["type"]] =  json.loads(Telemetry().to_json())
        return json.dumps(data)
    
    def _playlist(self, data : dict) -> str:
        data = download_playlist(data)
        path = os.getenv('BACKEND_DIR') + "config/playlist.json"
        open(path, 'w').write(json.dumps(data, indent=4))
        return json.dumps(data)

    
    def _screenshot(self, data : dict) -> str:
        screenshot = ImageGrab.grab()
        screenshot_bytes = io.BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_base64 = base64.b64encode(screenshot_bytes.getvalue()).decode("utf-8")
        data[data["type"]] = screenshot_base64
        return json.dumps(data)


    def _reboot(self, data : dict) -> str:
        # Traitement
        print("Reboot Message")
        os.system("sudo shutdown -r now")
        return json.dumps(data)
    
    def _power(self, data : dict) -> str:
        # Traitement
        print("power Message")
        #cmd = shlex.split("sudo shutdown -h now")
        #subprocess.call(cmd)
        return json.dumps(data)