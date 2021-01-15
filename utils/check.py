import sys
import requests
from datetime import datetime
from utils.config import version, latestKey, currentHash, endDate
from utils.offsets import *


def checkIfValid():
    now = datetime.now().timestamp()
    remaining = endDate - now
    return remaining > 0


def checkLicense():
    print("Checking license...")
    isValid = checkIfValid()
    if not isValid:
        print("Your license is expired. Please upgrade your license.")
        input("Press Enter to exit.")
        sys.exit()
    print("Your license is still valid!")


def checkUpdates():
    print("Checking updates...")
    data = requests.get("https://api.bariscodes.me/offsets").json()
    if (
        data["version"] != version
        or data["latestKey"] != latestKey
        or m_bDormant != data["offsets"]["m_bDormant"]
        or m_bSpotted != data["offsets"]["m_bSpotted"]
        or m_dwBoneMatrix != data["offsets"]["m_dwBoneMatrix"]
        or m_fFlags != data["offsets"]["m_fFlags"]
        or m_flFlashMaxAlpha != data["offsets"]["m_flFlashMaxAlpha"]
        or m_iCrosshairId != data["offsets"]["m_iCrosshairId"]
        or m_iGlowIndex != data["offsets"]["m_iGlowIndex"]
        or m_iHealth != data["offsets"]["m_iHealth"]
        or m_iTeamNum != data["offsets"]["m_iTeamNum"]
        or m_vecOrigin != data["offsets"]["m_vecOrigin"]
        or m_vecViewOffset != data["offsets"]["m_vecViewOffset"]
        or dwClientState != data["offsets"]["dwClientState"]
        or dwClientState_ViewAngles != data["offsets"]["dwClientState_ViewAngles"]
        or dwEntityList != data["offsets"]["dwEntityList"]
        or dwForceAttack != data["offsets"]["dwForceAttack"]
        or dwForceJump != data["offsets"]["dwForceJump"]
        or dwGlowObjectManager != data["offsets"]["dwGlowObjectManager"]
        or dwLocalPlayer != data["offsets"]["dwLocalPlayer"]
    ):
        latestVersion = data["version"]
        print(
            f"Version v{latestVersion} is available. Please download the newest version."
        )
        input("Press Enter to exit.")
        sys.exit()
    print("Everything is up to date!")


def check():
    print(f"Current Hash: {currentHash}")
    checkUpdates()
    checkLicense()
    print("Everything is okay, have fun!")
