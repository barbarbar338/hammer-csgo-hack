import yaml
from datetime import datetime

version = "1.1.1"
latestKey = "squishy-rock"
currentHash = "0baf43871a87eb55fcf33390a582c86f:2085d5ed0ebb04af1c79b22d"
endDate = datetime(2050, 1, 15, 15, 30).timestamp()

with open("config.yaml") as file:
    config = yaml.safe_load(file)
    aimlock = config["aimlock"]
    bhop = config["bhop"]
    glow = config["glow"]
    noflash = config["noflash"]
    radar = config["radar"]
    trigger = config["trigger"]
    recoil = config["recoil"]
    default_fov = config["default_fov"]
    trigger_key = config["trigger_key"]
    bunny_key = config["bunny_key"]
    aim_key = config["aim_key"]
    aim_fov = config["aim_fov"]
    ct_colors = config["ct_colors"]
    t_colors = config["t_colors"]
