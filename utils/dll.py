import pymem
import pymem.process
from utils.offsets import signatures

csgo = pymem.Pymem("csgo.exe")


def readDll(name):
    return pymem.process.module_from_name(csgo.process_handle, name).lpBaseOfDll


def getPlayer():
    return csgo.read_int(client_dll + signatures["dwLocalPlayer"])


client_dll = readDll("client.dll")
engine_dll = readDll("engine.dll")
