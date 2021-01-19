from utils.dll import getPlayer, csgo
from utils.offsets import m_iFOVStart
from utils.config import default_fov


def fov():
    player = getPlayer()
    if player:
        csgo.write_int(player + m_iFOVStart, default_fov)
