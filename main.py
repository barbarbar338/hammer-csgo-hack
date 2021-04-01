import sys
from utils.config import config
from utils.banner import printBanner
from utils.check import check, checkIfValid
from packages.aim import aim
from packages.bunny import bunny
from packages.glow import glow
from packages.noflash import noflash
from packages.radar import radar
from packages.trigger import trigger
from packages.fov import fov
from packages.recoil import recoil
from packages.charm import charm
from packages.rank import rank
from packages.skinchanger import change_skin


def main():
    check()
    printBanner()
    while True:
        isValid = checkIfValid()
        if not isValid:
            print("Your license is expired. Please upgrade your license.")
            input("Press Enter to exit.")
            sys.exit()
        if config["aimlock"]:
            aim()
        if config["bhop"]:
            bunny()
        if config["glow"]:
            glow()
        if config["noflash"]:
            noflash()
        if config["radar"]:
            radar()
        if config["trigger"]:
            trigger()
        if config["recoil"]:
            recoil()
        if config["fov"]:
            fov()
        if config["charm"]:
            charm()
        rank()
        #change_skin()


if __name__ == "__main__":
    main()
