import os, sys, json, signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from modules.server import Server

sys.tracebacklimit = 0
os.environ["FRONTEND_DIR"] = "/home/pi/standard_display/Player/frontend/"
os.environ["BACKEND_DIR"] = "/home/pi/standard_display/Player/backend/"
os.environ["REMOTE_SERVER"] = "http://192.168.1.88:8000/"
WELCOME_HTML_PATH  = os.getenv("FRONTEND_DIR") + "welcome.html"
INDEX_HTML_PATH    = os.getenv("FRONTEND_DIR") + "index.html"


def go_to_index() -> bool:
    path = os.getenv('BACKEND_DIR') + "config/player.json"
    if os.path.exists(path):
        try :
            with open(path, "r") as file:
                data = json.load(file)
                if data["player"]["uuid"] != "" and data["player"]["activated"] == True:
                    return True
            return False
        except:
            return False
    else :
        return False

def handler(signum, frame):
    print("Exiting...")
    exit(0)


if __name__ == "__main__":

    # Define the ChromeOptions variable
    options = ChromeOptions()

    # Enable kiosk mode
    options.add_argument("--kiosk")
    # Disable the extensions
    options.add_argument("--disable-extensions")
    # Set the autoplay policy to "document user activation is required"
    options.add_argument("--autoplay-policy=no-user-gesture-required")
    # Disable "Chrome is being controlled by automated test software" notification
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    # Create a ChromeService object
    service = ChromeService()

    # Start Chromium
    driver = webdriver.Chrome(service=service, options=options)

    if go_to_index() :
        # Navigate to index page
        driver.get("file://"+INDEX_HTML_PATH)
        pass
    else :
        # Navigate to welcome page
        driver.get("file://"+WELCOME_HTML_PATH)
        pass


    signal.signal(signal.SIGINT, handler)


    server = Server(host="127.0.0.1", port=8080)
    server.run()


