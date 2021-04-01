import yaml
from datetime import datetime

version = "2.1.0"
latestKey = "disguised-shake"
currentHash = "f5a402f614e08bfa25d786cc7bdf2d48:7351bb0aef6e05bc31085de2a43e84"
endDate = datetime(2050, 1, 15, 15, 30).timestamp()

with open("config.yaml") as file:
    config = yaml.safe_load(file)

skins = []
with open("skins.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        skin = line.split("=")[-1].strip()
        skins.append(int(skin))
