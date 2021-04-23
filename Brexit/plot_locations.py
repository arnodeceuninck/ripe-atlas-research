from util import *

data = get_data("https://stat.ripe.net/data/atlas-probes/data.json?", resource="gb")
data = data["data"]["probes"]

df = pd.DataFrame(data)
print(get_bounding_box(df))

plot_map(df, title="Brexit Probe Map", output_file="brexit_probe_map.png")