from utils.dll import csgo, client_dll
from utils.offsets import signatures, netvars
from utils.config import config


def wgpm(glow_obj, gindex, colors):
    csgo.write_float(glow_obj + ((gindex * 0x38) + 0x4), colors["red"])
    csgo.write_float(glow_obj + ((gindex * 0x38) + 0x8), colors["green"])
    csgo.write_float(glow_obj + ((gindex * 0x38) + 0xC), colors["blue"])
    csgo.write_float(glow_obj + ((gindex * 0x38) + 0x10), colors["opacity"])


def glow():
    glow_obj = csgo.read_bytes(client_dll + signatures["dwGlowObjectManager"], 4)
    glow_obj = int.from_bytes(glow_obj, byteorder="little")
    for i in range(64):
        entity = csgo.read_bytes(client_dll + signatures["dwEntityList"] + i * 0x10, 4)
        entity = int.from_bytes(entity, byteorder="little")
        if entity != 0:
            team = csgo.read_int(entity + netvars["m_iTeamNum"])
            gindex = csgo.read_int(entity + netvars["m_iGlowIndex"])
            if team == 3:
                wgpm(glow_obj, gindex, config["ct_glow"])
            else:
                wgpm(glow_obj, gindex, config["t_glow"])
            csgo.write_uchar(glow_obj + ((gindex * 0x38) + 0x24), 1)
            csgo.write_uchar(glow_obj + ((gindex * 0x38) + 0x25), 0)
