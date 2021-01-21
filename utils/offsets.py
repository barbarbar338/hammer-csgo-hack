import yaml
import requests

response = requests.get(
    "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.yaml"
).text
offsets = yaml.safe_load(response)

signatures = offsets["signatures"]
netvars = offsets["netvars"]
