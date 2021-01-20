import keyboard
import time
from utils.dll import getPlayer, csgo, client_dll
from utils.config import trigger_key, trigger_delay
from utils.offsets import m_iCrosshairId, dwEntityList, m_iTeamNum, dwForceAttack


def trigger():
    player = getPlayer()
    if player and keyboard.is_pressed(trigger_key):
        entity_id = csgo.read_int(player + m_iCrosshairId)
        entity = csgo.read_int(client_dll + dwEntityList + (entity_id - 1) * 0x10)
        if entity:
            entity_team = csgo.read_int(entity + m_iTeamNum)
            player_team = csgo.read_int(player + m_iTeamNum)
            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                time.sleep(trigger_delay)
                csgo.write_int(client_dll + dwForceAttack, 6)
