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
    shutil.copy("config.yaml", "dist")
    print("🎈 Build successfull")


if __name__ == "__main__":
    build()
