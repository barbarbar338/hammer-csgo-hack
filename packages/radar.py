from utils.dll import client_dll, csgo
from utils.offsets import netvars, signatures


def radar():
    for i in range(1, 32):
        entity = csgo.read_int(client_dll + signatures["dwEntityList"] + i * 0x10)
        if entity:
            csgo.write_int(entity + netvars["m_bSpotted"], 1)
