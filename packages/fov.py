from utils.config import config
from utils.dll import csgo, getPlayer
from utils.offsets import netvars


def fov():
    player = getPlayer()
    if player:
        csgo.write_int(player + netvars["m_iDefaultFOV"], config["default_fov"])
