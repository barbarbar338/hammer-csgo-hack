import yaml
from datetime import datetime

version = "1.2.0"
latestKey = "salty-jellyfish"
currentHash = "43ecd7049f5ad703133cd7f7b5307ef0:00a152be18d5321cea84fb15872213"
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
    trigger_delay = config["trigger_delay"]
    bunny_key = config["bunny_key"]
    aim_key = config["aim_key"]
    aim_fov = config["aim_fov"]
    aim_force_shoot = config["aim_force_shoot"]
    ct_glow = config["ct_glow"]
    t_glow = config["t_glow"]
    fov = config["fov"]
    ct_charm = config["ct_charm"]
    t_charm = config["t_charm"]
    rank_checker = config["rank_checker"]
    rank_checker_key = config["rank_checker_key"]
