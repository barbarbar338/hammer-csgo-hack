import yaml
from datetime import datetime

version = "2.0.0"
latestKey = "spicy-donut"
currentHash = "f162cf5126d44de878974b96f0cb97cb:63363e17ebcc6ca7d6384f"
endDate = datetime(2050, 1, 15, 15, 30).timestamp()

with open("config.yaml") as file:
    config = yaml.safe_load(file)
