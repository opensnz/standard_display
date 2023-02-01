from PIL import ImageGrab
screenshot = ImageGrab.grab()
import base64
import io

screenshot_bytes = io.BytesIO()
screenshot.save(screenshot_bytes, format='PNG')
screenshot_base64 = base64.b64encode(screenshot_bytes.getvalue()).decode("utf-8")

with open("image.png", "wb") as f:
    f.write(base64.decodebytes(screenshot_base64.encode("utf-8")))