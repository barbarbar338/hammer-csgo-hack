from tabulate import tabulate
from utils.config import *


def printAuthor():
    print(f"\nHammer CS:GO Hack v{version}\n- by barbarbar338\n")


def printHacks():
    print("\nHacks\n")
    print(
        tabulate(
            [
                ["Aim Lock", str(aimlock)],
                ["BHop", str(bhop)],
                ["Glow Hack", str(glow)],
                ["Charm Hack", str(charm)],
                ["No Flash", str(noflash)],
                ["Radar", str(radar)],
                ["Trigger Bot", str(trigger)],
                ["Recoil Helper", str(recoil)],
                ["FOV", str(fov)],
            ],
            headers=["Hack", "Is Active"],
            tablefmt="orgtbl",
        )
    )


def printConfig():
    print("\nConfigurations\n")
    print(
        tabulate(
            [
                ["Trigger Bot Key", str(trigger_key)],
                ["BHop Key", str(bunny_key)],
                ["Aim Lock Key", str(aim_key)],
                ["Aim Lock FOV", str(aim_fov)],
                ["FOV", str(default_fov)],
                ["Glow CT Colors", str(ct_glow)],
                ["Glow T Colors", str(t_glow)],
                ["Charm CT Colors", str(ct_charm)],
                ["Charm T Colors", str(t_charm)],
            ],
            headers=["Configuration", "Value"],
            tablefmt="orgtbl",
        )
    )


def printBanner():
    printAuthor()
    printHacks()
    printConfig()
