import sys
from datetime import datetime

import requests

from utils.config import currentHash, endDate, latestKey, version


# Simple license check, you can create your own license check system
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

    data = requests.get(
        "https://pinkie-api.fly.dev/check"
    ).json()  # API deprecated, create your own version check api
    if data["version"] != version or data["latestKey"] != latestKey:
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
