import subprocess
import shutil
from prebuild import prebuild
from format import format


def build():
    prebuild()
    format()
    print("🚧 Building")
    subprocess.call(
        [
            "pyinstaller",
            "--onefile",
            "--icon=assets/favicon.ico",
            "--name",
            "hammer",
            "main.py",
        ]
    )
    print("📌 copying config.yaml to output")
    shutil.copy("config.yaml", "dist")
    print("📌 copying skins.txt to output")
    shutil.copy("skins.txt", "dist")
    print("🎈 Build successfull")


if __name__ == "__main__":
    build()
