import json
from datetime import datetime

version = "1.1.0"
latestKey = "tasty-jellyfish"
currentHash = "f76d956963b5f01f80a5545791de8378:d3d0b26d6480cd18f2bfe01626c9ba"
endDate = datetime(2021, 1, 15, 15, 30).timestamp()

with open("config.json") as file:
    config = json.load(file)
    aimlock = config["aimlock"]
    bhop = config["bhop"]
    glow = config["glow"]
    noflash = config["noflash"]
    radar = config["radar"]
    trigger = config["trigger"]
    trigger_key = config["trigger_key"]
    bunny_key = config["bunny_key"]
    aim_key = config["aim_key"]
    aim_fov = config["aim_fov"]
    ct_colors = config["ct_colors"]
    t_colors = config["t_colors"]
