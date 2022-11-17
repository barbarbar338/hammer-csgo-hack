import shutil
import subprocess

from format import format
from prebuild import prebuild


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

    print("🎈 Build successfull")


if __name__ == "__main__":
    build()
