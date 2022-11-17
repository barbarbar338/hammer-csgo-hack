import time

import keyboard

from utils.config import config
from utils.dll import client_dll, csgo, getPlayer
from utils.offsets import netvars, signatures


def trigger():
    player = getPlayer()
    if player and (
        keyboard.is_pressed(config["trigger_key"])
        or (config["aim_force_shoot"] and keyboard.is_pressed(config["aim_key"]))
    ):
        entity_id = csgo.read_int(player + netvars["m_iCrosshairId"])
        entity = csgo.read_int(
            client_dll + signatures["dwEntityList"] + (entity_id - 1) * 0x10
        )
        if entity:
            entity_team = csgo.read_int(entity + netvars["m_iTeamNum"])
            player_team = csgo.read_int(player + netvars["m_iTeamNum"])
            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                time.sleep(config["trigger_delay"])
                csgo.write_int(client_dll + signatures["dwForceAttack"], 6)
