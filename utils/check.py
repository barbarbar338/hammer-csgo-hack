import requests
import sys
from utils.config import version, latestKey, currentHash
from utils.offsets import *


def check():
    print("Checking updates...")
    print(f"Current Hash: {currentHash}")
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
        input("Press Enter to continue.")
        sys.exit()
    print("Everything is up to date!")
