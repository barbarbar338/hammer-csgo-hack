from utils.dll import getPlayer, csgo
from utils.offsets import netvars
from utils.config import config


def fov():
    player = getPlayer()
    if player:
        csgo.write_int(player + netvars["m_iDefaultFOV"], config["default_fov"])
