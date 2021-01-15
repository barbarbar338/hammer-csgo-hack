import utils.config as config
from utils.banner import printBanner
from utils.check import check
from packages.aim import aim
from packages.bunny import bunny
from packages.glow import glow
from packages.noflash import noflash
from packages.radar import radar
from packages.trigger import trigger


def main():
    check()
    printBanner()
    while True:
        if config.aimlock:
            aim()
        if config.bhop:
            bunny()
        if config.glow:
            glow()
        if config.noflash:
            noflash()
        if config.radar:
            radar()
        if config.trigger:
            trigger()


if __name__ == "__main__":
    main()
