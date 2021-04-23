from util import *
from datetime import datetime

# Geen handige manier gevonden om measurements per country te krijgen. Ik ga itereren over de ASN's en deze telkens als target ASN instellen.

data = get_data("https://stat.ripe.net/data/country-resource-list/data.json?", resource="gb")
asns = data["data"]["resources"]["asn"]


for asn in asns:
    start = datetime(2020, 11, 1, 0, 0).timestamp()
    data = get_data("https://atlas.ripe.net/api/v2/measurements/ping/?", target_asn=asn, start_time__gt=start)
    print(f"{data['count']}\t{asn}")

    # Geeft voor alle ASN's een count van 0, dus geen succes met deze meting
