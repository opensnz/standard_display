import json
from modules.telemetry import Telemetry
telemetry = Telemetry()
print(json.dumps(telemetry, default=lambda o:o.__dict__, sort_keys=True, indent=4))