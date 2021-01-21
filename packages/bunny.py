import keyboard
from utils.dll import getPlayer, csgo, client_dll
from utils.offsets import signatures, netvars
from utils.config import config


def bunny():
    player = getPlayer()
    if player and keyboard.is_pressed(config["bunny_key"]):
        on_ground = csgo.read_int(player + netvars["m_fFlags"])
        if on_ground and on_ground == 257 or on_ground == 263:
            csgo.write_int(client_dll + signatures["dwForceJump"], 6)
