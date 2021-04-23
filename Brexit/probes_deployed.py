# Generates a graph of how meny probes are neverseen/connected/disconnected/abandonned between two given date. One point per date.
from util import *
from datetime import datetime

start = datetime.now()
data = get_data("https://stat.ripe.net/data/atlas-probe-deployment/data.json?", resource="gb")
data = data["data"]["deployments"]["deployment"]
pass