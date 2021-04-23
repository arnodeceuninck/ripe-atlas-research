from util import *

data = get_data("https://stat.ripe.net/data/atlas-probes/data.json?", resource="gb")
data = data["data"]["probes"]

df = pd.DataFrame(data)
print(get_bounding_box(df))

plot_map(df, title="Brexit Probe Map 1", output_file="brexit_probe_map1.png")
plot_map(df, title="Brexit Probe Map 2", output_file="brexit_probe_map2.png", BBox=(-13, 5, 48, 61), image_location="../assets/uk.png")