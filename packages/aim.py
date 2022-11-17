from math import atan, isnan, pi, sqrt
from random import randint

import keyboard

from utils.config import config
from utils.dll import client_dll, csgo, engine_dll, getPlayer
from utils.offsets import netvars, signatures


def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    try:
        delta_x = localpos1 - enemypos1
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
        x = atan(delta_z / hyp) * 180 / pi
        y = atan(delta_y / delta_x) * 180 / pi
        if delta_x >= 0.0:
            y += 180.0
        return x, y
    except Exception as e:
        print(e)
        pass


def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY


def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex

    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey


def nanchecker(first, second):
    if isnan(first) or isnan(second):
        return False
    else:
        return True


def aim():
    engine_dll_pointer = csgo.read_int(engine_dll + signatures["dwClientState"])
    player = getPlayer()
    if player:
        localTeam = csgo.read_int(player + netvars["m_iTeamNum"])
        olddistx = 111111111111
        olddisty = 111111111111
        for i in range(1, 32):
            entity = csgo.read_int(client_dll + signatures["dwEntityList"] + i * 0x10)
            if entity:
                entity_team_id = csgo.read_int(entity + netvars["m_iTeamNum"])
                entity_hp = csgo.read_int(entity + netvars["m_iHealth"])
                entity_dormant = csgo.read_int(entity + signatures["m_bDormant"])
                target_hp = 0
                target = None
                target_dormant = None
                target_x = 0
                target_y = 0
                target_z = 0
                if localTeam != entity_team_id and entity_hp > 0:
                    entity_bones = csgo.read_int(entity + netvars["m_dwBoneMatrix"])
                    localpos_x_angles = csgo.read_float(
                        engine_dll_pointer + signatures["dwClientState_ViewAngles"]
                    )
                    localpos_y_angles = csgo.read_float(
                        engine_dll_pointer
                        + signatures["dwClientState_ViewAngles"]
                        + 0x4
                    )
                    localpos1 = csgo.read_float(player + netvars["m_vecOrigin"])
                    localpos2 = csgo.read_float(player + netvars["m_vecOrigin"] + 4)
                    localpos_z_angles = csgo.read_float(
                        player + netvars["m_vecViewOffset"] + 0x8
                    )
                    localpos3 = (
                        csgo.read_float(player + netvars["m_vecOrigin"] + 8)
                        + localpos_z_angles
                    )
                    if config["aim_type"] == "body":
                        try:
                            entitypos_x = csgo.read_float(entity_bones + 0x30 * 5 + 0xC)
                            entitypos_y = csgo.read_float(
                                entity_bones + 0x30 * 5 + 0x1C
                            )
                            entitypos_z = csgo.read_float(
                                entity_bones + 0x30 * 5 + 0x2C
                            )
                        except:
                            continue
                    elif config["aim_type"] == "random":
                        try:
                            random_value = randint(3, 9)
                            entitypos_x = csgo.read_float(
                                entity_bones + 0x30 * random_value + 0xC
                            )
                            entitypos_y = csgo.read_float(
                                entity_bones + 0x30 * random_value + 0x1C
                            )
                            entitypos_z = csgo.read_float(
                                entity_bones + 0x30 * random_value + 0x2C
                            )
                        except:
                            continue
                    elif config["aim_type"] == "legit":
                        try:
                            legit_range = randint(4, 8)
                            entitypos_x = csgo.read_float(
                                entity_bones + 0x30 * legit_range + 0xC
                            )
                            entitypos_y = csgo.read_float(
                                entity_bones + 0x30 * 4 + 0x1C
                            )
                            entitypos_z = csgo.read_float(
                                entity_bones + 0x30 * legit_range + 0x2C
                            )
                        except:
                            continue
                    else:
                        try:
                            entitypos_x = csgo.read_float(entity_bones + 0x30 * 8 + 0xC)
                            entitypos_y = csgo.read_float(
                                entity_bones + 0x30 * 5 + 0x1C
                            )
                            entitypos_z = csgo.read_float(
                                entity_bones + 0x30 * 8 + 0x2C
                            )
                        except:
                            continue
                    X, Y = calcangle(
                        localpos1,
                        localpos2,
                        localpos3,
                        entitypos_x,
                        entitypos_y,
                        entitypos_z,
                    )
                    newdist_x, newdist_y = calc_distance(
                        localpos_x_angles, localpos_y_angles, X, Y
                    )
                    if (
                        newdist_x < olddistx
                        and newdist_y < olddisty
                        and newdist_x <= config["aim_fov"]
                        and newdist_y <= config["aim_fov"]
                    ):
                        olddistx, olddisty = newdist_x, newdist_y
                        target, target_hp, target_dormant = (
                            entity,
                            entity_hp,
                            entity_dormant,
                        )
                        target_x, target_y, target_z = (
                            entitypos_x,
                            entitypos_y,
                            entitypos_z,
                        )
                        if keyboard.is_pressed(config["aim_key"]) and player:
                            if target and target_hp > 0 and not target_dormant:
                                localpos1 = csgo.read_float(
                                    player + netvars["m_vecOrigin"]
                                )
                                localpos2 = csgo.read_float(
                                    player + netvars["m_vecOrigin"] + 4
                                )
                                localpos_z_angles = csgo.read_float(
                                    player + netvars["m_vecViewOffset"] + 0x8
                                )
                                localpos3 = (
                                    csgo.read_float(player + netvars["m_vecOrigin"] + 8)
                                    + localpos_z_angles
                                )
                                pitch, yaw = calcangle(
                                    localpos1,
                                    localpos2,
                                    localpos3,
                                    target_x,
                                    target_y,
                                    target_z,
                                )
                                if nanchecker(pitch, yaw):
                                    normalize_x, normalize_y = normalizeAngles(
                                        pitch, yaw
                                    )
                                    punchx = csgo.read_float(
                                        player + netvars["m_aimPunchAngle"]
                                    )
                                    punchy = csgo.read_float(
                                        player + netvars["m_aimPunchAngle"] + 0x4
                                    )
                                    Commands = csgo.read_int(
                                        client_dll + signatures["dwInput"] + 0xF4
                                    )
                                    VerifedCommands = csgo.read_int(
                                        client_dll + signatures["dwInput"] + 0xF8
                                    )
                                    Desired = (
                                        csgo.read_int(
                                            engine_dll_pointer
                                            + signatures[
                                                "clientstate_last_outgoing_command"
                                            ]
                                        )
                                        + 2
                                    )
                                    OldUser = Commands + ((Desired - 1) % 150) * 100
                                    VerifedOldUser = (
                                        VerifedCommands + ((Desired - 1) % 150) * 0x68
                                    )
                                    m_buttons = csgo.read_int(OldUser + 0x30)
                                    Net_Channel = csgo.read_uint(
                                        engine_dll_pointer
                                        + signatures["clientstate_net_channel"]
                                    )
                                    if config["aim_lock_type"] == "silent":
                                        csgo.write_uchar(
                                            engine_dll + signatures["dwbSendPackets"], 0
                                        )
                                        if csgo.read_int(Net_Channel + 0x18) >= Desired:
                                            csgo.write_float(
                                                OldUser + 0x0C, normalize_x
                                            )
                                            csgo.write_float(
                                                OldUser + 0x10, normalize_y
                                            )
                                            csgo.write_int(
                                                OldUser + 0x30, m_buttons | (1 << 0)
                                            )
                                            csgo.write_float(
                                                VerifedOldUser + 0x0C,
                                                normalize_x,
                                            )
                                            csgo.write_float(
                                                VerifedOldUser + 0x10,
                                                normalize_y,
                                            )
                                            csgo.write_int(
                                                VerifedOldUser + 0x30,
                                                m_buttons | (1 << 0),
                                            )
                                            csgo.write_uchar(
                                                engine_dll
                                                + signatures["dwbSendPackets"],
                                                1,
                                            )
                                        else:
                                            csgo.write_uchar(
                                                engine_dll
                                                + signatures["dwbSendPackets"],
                                                1,
                                            )
                                    elif config["aim_lock_type"] == "silentrcs":
                                        csgo.write_uchar(
                                            engine_dll + signatures["dwbSendPackets"], 0
                                        )
                                        if csgo.read_int(Net_Channel + 0x18) >= Desired:
                                            csgo.write_float(
                                                OldUser + 0x0C, normalize_x
                                            )
                                            csgo.write_float(
                                                OldUser + 0x10, normalize_y
                                            )
                                            csgo.write_int(
                                                OldUser + 0x30, m_buttons | (1 << 0)
                                            )
                                            csgo.write_float(
                                                VerifedOldUser + 0x0C,
                                                normalize_x - (punchx * 2),
                                            )
                                            csgo.write_float(
                                                VerifedOldUser + 0x10,
                                                normalize_y - (punchy * 2),
                                            )
                                            csgo.write_int(
                                                VerifedOldUser + 0x30,
                                                m_buttons | (1 << 0),
                                            )
                                            csgo.write_uchar(
                                                engine_dll
                                                + signatures["dwbSendPackets"],
                                                1,
                                            )
                                        else:
                                            csgo.write_uchar(
                                                engine_dll
                                                + signatures["dwbSendPackets"],
                                                1,
                                            )
                                    else:
                                        csgo.write_float(
                                            engine_dll_pointer
                                            + signatures["dwClientState_ViewAngles"],
                                            normalize_x,
                                        )
                                        csgo.write_float(
                                            engine_dll_pointer
                                            + signatures["dwClientState_ViewAngles"]
                                            + 0x4,
                                            normalize_y,
                                        )
