from tabulate import tabulate
from utils.config import config, version


def printAuthor():
    print(f"\nHammer CS:GO Hack v{version}\n- by barbarbar338\n")


def printHacks():
    print("\nHacks\n")
    print(
        tabulate(
            [
                ["Aim Lock", str(config["aimlock"])],
                ["BHop", str(config["bhop"])],
                ["Glow Hack", str(config["glow"])],
                ["Charm Hack", str(config["charm"])],
                ["No Flash", str(config["noflash"])],
                ["Radar", str(config["radar"])],
                ["Trigger Bot", str(config["trigger"])],
                ["Recoil Helper", str(config["recoil"])],
                ["FOV", str(config["fov"])],
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
                ["Trigger Bot Key", str(config["trigger_key"])],
                ["Trigger Bot Delay", str(config["trigger_delay"])],
                ["BHop Key", str(config["bunny_key"])],
                ["Aim Lock Key", str(config["aim_key"])],
                ["Aim Lock FOV", str(config["aim_fov"])],
                ["Aim Lock Force Shoot", str(config["aim_force_shoot"])],
                ["Aim Type", str(config["aim_type"])],
                ["Aim Lock Type", str(config["aim_lock_type"])],
                ["FOV", str(config["default_fov"])],
                ["Glow CT Colors", str(config["ct_glow"])],
                ["Glow T Colors", str(config["t_glow"])],
                ["Charm CT Colors", str(config["ct_charm"])],
                ["Charm T Colors", str(config["t_charm"])],
                ["Rank Checker Key", str(config["rank_checker_key"])],
            ],
            headers=["Configuration", "Value"],
            tablefmt="orgtbl",
        )
    )


def printBanner():
    printAuthor()
    printHacks()
    printConfig()
