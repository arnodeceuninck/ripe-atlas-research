from util import *
from datetime import datetime

# Geen handige manier gevonden om measurements per country te krijgen. Ik ga itereren over de ASN's en deze telkens als target ASN instellen.

data = get_data("https://stat.ripe.net/data/atlas-probes/data.json?", resource="gb")
probes = data["data"]["probes"]

count = 0
i = 0
for probe in probes:
    start_min = datetime(2020, 1, 14, 0, 0).timestamp()
    start_max = datetime(2021, 1, 31, 0, 0).timestamp()
    end_min = datetime(2021, 2, 1, 0, 0).timestamp()
    end_max = datetime(2021, 2, 15, 0, 0).timestamp()

    data = get_data("https://atlas.ripe.net/api/v2/measurements/ping/?", current_probes=probe['id'], start_time__gt=start_min, start_time__lt=start_max, end_time__gt=end_min, end_time__lt=end_max, is_all_scheduled=True, interval__gte=60*60, interval__lte=60*60*24*7)

    if i % 10:
        print(f"{i}/{len(probes)}")

    if data["count"] != 0:
        count += data["count"]
        print(f"Count: {data['count']}")
        # print(f"Total: {count}")
    # Geeft voor alle ASN's een count van 0, dus geen succes met deze meting

    # Found a great probe here: 753, continuing analysis in seperate file
