import yaml
from datetime import datetime

version = "1.1.2"
latestKey = "butter-crayfish"
currentHash = "221445c26c5b32118117ec1b081cd693:fffa31ff05e7e1ba27d34b508257fe"
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
    charm = config["charm"]
    default_fov = config["default_fov"]
    trigger_key = config["trigger_key"]
    bunny_key = config["bunny_key"]
    aim_key = config["aim_key"]
    aim_fov = config["aim_fov"]
    ct_glow = config["ct_glow"]
    t_glow = config["t_glow"]
    fov = config["fov"]
    ct_charm = config["ct_charm"]
    t_charm = config["t_charm"]
