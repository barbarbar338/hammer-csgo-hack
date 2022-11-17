import keyboard

from utils.config import config
from utils.dll import client_dll, csgo, getPlayer
from utils.offsets import netvars, signatures


def bunny():
    player = getPlayer()
    if player and keyboard.is_pressed(config["bunny_key"]):
        on_ground = csgo.read_int(player + netvars["m_fFlags"])
        if on_ground and on_ground == 257 or on_ground == 263:
            csgo.write_int(client_dll + signatures["dwForceJump"], 6)
