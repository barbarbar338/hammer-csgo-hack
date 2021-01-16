from utils.dll import getPlayer, csgo
from utils.offsets import m_iFOV
from utils.config import default_fov


def fov():
    player = getPlayer()
    if player:
        csgo.write_int(player + m_iFOV, default_fov)
