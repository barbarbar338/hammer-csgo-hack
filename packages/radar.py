from utils.dll import csgo, client_dll
from utils.offsets import dwEntityList, m_bSpotted


def radar():
    for i in range(1, 32):
        entity = csgo.read_int(client_dll + dwEntityList + i * 0x10)
        if entity:
            csgo.write_int(entity + m_bSpotted, 1)
