from utils.dll import csgo, client_dll
from utils.offsets import signatures, netvars
from utils.config import config


def wcpm(entity, charm):
    csgo.write_int(entity + netvars["m_clrRender"], charm["red"])
    csgo.write_int(entity + netvars["m_clrRender"] + 0x1, charm["green"])
    csgo.write_int(entity + netvars["m_clrRender"] + 0x2, charm["blue"])


def charm():
    for i in range(32):
        entity = csgo.read_int(client_dll + signatures["dwEntityList"] + i * 0x10)
        if entity:
            team_id = csgo.read_int(entity + netvars["m_iTeamNum"])
            if team_id == 3:
                wcpm(entity, config["ct_charm"])
            else:
                wcpm(entity, config["t_charm"])
