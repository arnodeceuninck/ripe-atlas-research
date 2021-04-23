from util import *
from datetime import datetime

# Geen handige manier gevonden om measurements per country te krijgen. Ik ga itereren over de ASN's en deze telkens als target ASN instellen.

data = get_data("https://atlas.ripe.net/api/v2/measurements/23853635/results/")

df = pd.json_normalize(data)  # Flattens the data

dates = []
for date in df['timestamp']:
    dates.append(str(datetime.fromtimestamp(date)))

generate_date_plot(df, date_list=dates, data_column_name='avg', plot_title='Average ping', output_file='average_ping.png')

