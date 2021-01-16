from math import isnan
from utils.dll import getPlayer, csgo, engine_dll
from utils.offsets import (
    m_iShotsFired,
    dwClientState,
    dwClientState_ViewAngles,
    m_aimPunchAngle,
)


def nanchecker(first, second):
    if isnan(first) or isnan(second):
        return False
    else:
        return True


def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True


def recoil():
    oldpunchx = 0.0
    oldpunchy = 0.0
    player = getPlayer()
    engine_pointer = csgo.read_int(engine_dll + dwClientState)
    if player:
        if csgo.read_int(player + m_iShotsFired) > 2:
            rcs_x = csgo.read_float(engine_pointer + dwClientState_ViewAngles)
            rcs_y = csgo.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
            punchx = csgo.read_float(player + m_aimPunchAngle)
            punchy = csgo.read_float(player + m_aimPunchAngle + 0x4)
            newrcsx = rcs_x - (punchx - oldpunchx) * 1.5
            newrcsy = rcs_y - (punchy - oldpunchy) * 1.5
            oldpunchx = punchx
            oldpunchy = punchy
            if nanchecker(newrcsx, newrcsy) and checkangles(newrcsx, newrcsy):
                csgo.write_float(engine_pointer + dwClientState_ViewAngles, newrcsx)
                csgo.write_float(
                    engine_pointer + dwClientState_ViewAngles + 0x4, newrcsy
                )
        else:
            oldpunchx = csgo.read_float(player + m_aimPunchAngle)
            oldpunchy = csgo.read_float(player + m_aimPunchAngle + 0x4)
            newrcsx = oldpunchx
            newrcsy = oldpunchy
