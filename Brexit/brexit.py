from ripe.atlas.cousteau import ProbeRequest, MeasurementRequest
import requests

COUNTRY_CODE = "GB"


def get_probes_for_country(country_code):
    filters = {"country_code": country_code}
    return ProbeRequest(**filters)

def get_country(ip):
    request = requests.get(f"https://geolocation-db.com/json/{ip}")
    data = request.json()
    country_code = data["country_code"] # TODO: ipv6: '2001:7fb:fe01::1'
    print(country_code)
    return country_code

# probes = get_probes_for_country(COUNTRY_CODE)
#
# # For some reason gives 0 probes without this for loop
# for probe in probes:
#     pass
#
# print(f"Found {probes.total_count} probes in {COUNTRY_CODE}")

# https://atlas.ripe.net/docs/api/v2/reference/#!/measurements/Type
filters = {"status": 2}
measurements = MeasurementRequest(**filters)

# Get the amount of measurements (a lot)
i = 0
for msm in measurements:
    i += 1
    if not i % 1000:
        print(i)

target_country_count = 0
# for msm in measurements:
#     target_ip = msm["target_ip"]
#     if target_ip and get_country(target_ip) == COUNTRY_CODE:
#         target_country_count += 1

# Print total count of found measurements
print(f"Found {measurements.total_count} measurements, of which {target_country_count} going to {COUNTRY_CODE}")
