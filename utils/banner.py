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
                ["No Flash", str(noflash)],
                ["Radar", str(radar)],
                ["Trigger Bot", str(trigger)],
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
                ["Glow CT Colors", str(ct_colors)],
                ["Glow T Colors", str(t_colors)],
            ],
            headers=["Configuration", "Value"],
            tablefmt="orgtbl",
        )
    )


def printBanner():
    printAuthor()
    printHacks()
    printConfig()
