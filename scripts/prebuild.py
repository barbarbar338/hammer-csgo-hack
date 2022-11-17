import os
import shutil


def prebuild():
    print('🧹 Cleaning "dist" directory')

    if os.path.isdir("dist"):
        shutil.rmtree("dist")

    print('🧹 Cleaning "build" directory')

    if os.path.isdir("build"):
        shutil.rmtree("build")


if __name__ == "__main__":
    prebuild()
