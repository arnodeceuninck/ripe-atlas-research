# Generates a graph of how meny probes are neverseen/connected/disconnected/abandonned between two given date. One point per date.
from util import *
from datetime import date
import matplotlib.dates as mdates



start = date(2020, 11, 1)
stop = date.today()

data = get_data("https://stat.ripe.net/data/atlas-probe-deployment/data.json?", resource="gb", starttime=start, endtime=stop)
data = data["data"]["deployments"][0]["deployment"]

df = pd.json_normalize(data)  # Flattens the data
print(df.head(3))

generate_date_plot(df, dates_column_name='date', data_column_name='statuses.connected', plot_title='Probes Connected', output_file='probes_connected.png')
generate_date_plot(df, dates_column_name='date', data_column_name='statuses.disconnected', plot_title='Probes Disconnected', output_file='probes_disconnected.png')
generate_date_plot(df, dates_column_name='date', data_column_name='statuses.abandoned', plot_title='Probes Abandoned', output_file='probes_abandoned.png')
generate_date_plot(df, dates_column_name='date', data_column_name='statuses.neverseen', plot_title='Probes Neverseen', output_file='probes_neverseen.png')
