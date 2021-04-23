# Generates a graph of how meny probes are neverseen/connected/disconnected/abandonned between two given date. One point per date.
from util import *
from datetime import date, timedelta
import matplotlib.dates as mdates

query_date = date(2020, 11, 1)
query_date = date(2019, 1, 1)

# Collect data over time
dates = []
registered = []
routed = []
while query_date < date.today():
    data = get_data("https://stat.ripe.net/data/country-asns/data.json?", resource="gb", query_time=query_date)
    data = data["data"]["countries"][0]["stats"]

    dates.append(str(query_date))
    registered.append(data['registered'])
    routed.append(data["routed"])

    query_date += timedelta(days=31)

data = {'date': dates, 'registered': registered, 'routed': routed}
df = pd.DataFrame(data)

generate_date_plot(df, dates_column_name='date', data_column_name='registered', plot_title='ASNs registered', output_file='registered_asns.png')
generate_date_plot(df, dates_column_name='date', data_column_name='routed', plot_title='ASNs routed', output_file='routed_asns.png')
