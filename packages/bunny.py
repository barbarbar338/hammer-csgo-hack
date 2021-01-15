import keyboard
from utils.dll import getPlayer, csgo, client_dll
from utils.offsets import dwForceJump, m_fFlags
from utils.config import bunny_key


def bunny():
    player = getPlayer()
    if player and keyboard.is_pressed(bunny_key):
        force_jump = client_dll + dwForceJump
        on_ground = csgo.read_int(player + m_fFlags)
        if on_ground and on_ground == 257 or on_ground == 263:
            csgo.write_int(force_jump, 6)
