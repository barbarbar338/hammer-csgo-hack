import subprocess
import shutil
import os

if os.path.isdir("dist"):
    shutil.rmtree("dist")
if os.path.isdir("build"):
    shutil.rmtree("build")
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
