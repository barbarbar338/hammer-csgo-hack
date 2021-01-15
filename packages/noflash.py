from utils.dll import getPlayer, csgo
from utils.offsets import m_flFlashMaxAlpha


def noflash():
    player = getPlayer()
    if player:
        flash_value = player + m_flFlashMaxAlpha
        if flash_value:
            csgo.write_float(flash_value, float(0))
