import json

version = "1.0.0"
latestKey = "flying-squid"
currentHash = "8589834b86c10cbd4642671e4b673148:2085516e5ec3449efcbcae02"

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
