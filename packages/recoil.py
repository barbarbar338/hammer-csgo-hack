from math import isnan

from utils.dll import csgo, engine_dll, getPlayer
from utils.offsets import netvars, signatures


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
    engine_pointer = csgo.read_int(engine_dll + signatures["dwClientState"])
    if player:
        if csgo.read_int(player + netvars["m_iShotsFired"]) > 2:
            rcs_x = csgo.read_float(
                engine_pointer + signatures["dwClientState_ViewAngles"]
            )
            rcs_y = csgo.read_float(
                engine_pointer + signatures["dwClientState_ViewAngles"] + 0x4
            )
            punchx = csgo.read_float(player + netvars["m_aimPunchAngle"])
            punchy = csgo.read_float(player + netvars["m_aimPunchAngle"] + 0x4)
            newrcsx = rcs_x - (punchx - oldpunchx) * 0.02
            newrcsy = rcs_y - (punchy - oldpunchy) * 0.02
            oldpunchx = punchx
            oldpunchy = punchy
            if nanchecker(newrcsx, newrcsy) and checkangles(newrcsx, newrcsy):
                csgo.write_float(
                    engine_pointer + signatures["dwClientState_ViewAngles"], newrcsx
                )
                csgo.write_float(
                    engine_pointer + signatures["dwClientState_ViewAngles"] + 0x4,
                    newrcsy,
                )
        else:
            oldpunchx = csgo.read_float(player + netvars["m_aimPunchAngle"])
            oldpunchy = csgo.read_float(player + netvars["m_aimPunchAngle"] + 0x4)
            newrcsx = oldpunchx
            newrcsy = oldpunchy
