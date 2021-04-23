from util import *
from datetime import datetime

# Geen handige manier gevonden om measurements per country te krijgen. Ik ga itereren over de ASN's en deze telkens als target ASN instellen.

def make_maesurement_graph(measurement_id):
    data = get_data(f"https://atlas.ripe.net/api/v2/measurements/{measurement_id}/results/")

    df = pd.json_normalize(data)  # Flattens the data

    dates = []
    for date in df['timestamp']:
        dates.append(str(datetime.fromtimestamp(date)))

    generate_date_plot(df, date_list=dates, data_column_name='avg', plot_title='Average ping', output_file=f'average_ping_{measurement_id}.png')

make_maesurement_graph(4103859)
