from utils.dll import csgo, client_dll
from utils.offsets import dwEntityList, m_iTeamNum, m_clrRender
from utils.config import t_charm, ct_charm


def wcpm(entity, charm):
    csgo.write_int(entity + m_clrRender, charm["red"])
    csgo.write_int(entity + m_clrRender + 0x1, charm["green"])
    csgo.write_int(entity + m_clrRender + 0x2, charm["blue"])


def charm():
    for i in range(32):
        entity = csgo.read_int(client_dll + dwEntityList + i * 0x10)
        if entity:
            team_id = csgo.read_int(entity + m_iTeamNum)
            if team_id == 3:
                wcpm(entity, ct_charm)
            else:
                wcpm(entity, t_charm)
