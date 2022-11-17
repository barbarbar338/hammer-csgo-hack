from utils.dll import csgo, getPlayer
from utils.offsets import netvars


def noflash():
    player = getPlayer()
    if player:
        flash_value = player + netvars["m_flFlashMaxAlpha"]
        if flash_value:
            csgo.write_float(flash_value, float(0))
