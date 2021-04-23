from util import *
from datetime import datetime
from ping_measurement_analyzer import make_maesurement_graph

# Geen handige manier gevonden om measurements per country te krijgen. Ik ga itereren over de ASN's en deze telkens als target ASN instellen.

data = get_data("https://stat.ripe.net/data/atlas-probes/data.json?", resource="gb")
probes = data["data"]["probes"]

count = 0
i = 0
for probe in probes:
    start_min = datetime(2020, 11, 1, 0, 0).timestamp()
    start_max = datetime(2021, 1, 14, 0, 0).timestamp()
    end_min = datetime(2021, 2, 14, 0, 0).timestamp()
    end_max = datetime(2021, 4, 1, 0, 0).timestamp()

    data = get_data("https://atlas.ripe.net/api/v2/measurements/ping/?", current_probes=probe['id'], start_time__gt=start_min, start_time__lt=start_max, stop_time__gt=end_min, stop_time__lt=end_max)
    # data = get_data("https://atlas.ripe.net/api/v2/measurements/ping/?", current_probes=probe['id'],
    #                 start_time__lt=start_max, stop_time__gt=end_min)

    if i % 10:
        print(f"{i}/{len(probes)}")

    if data["count"] != 0:
        count += data["count"]
        print(f"Count: {data['count']}")
        make_maesurement_graph(data["results"][0]["id"])

        # print(f"Total: {count}")
    # Geeft voor alle ASN's een count van 0, dus geen succes met deze meting

    # Found a great probe here: 753 (measurement 23853635), continuing analysis in seperate file
