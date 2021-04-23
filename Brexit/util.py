import requests
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def get_data(base_url, **kwargs):
    # Add parameters to base_url
    for key, value in kwargs.items():
        base_url += f"{key}={value}&"

    # Request the data
    print(f"Querying {base_url}")
    request = requests.get(base_url)
    return request.json()

def get_bounding_box(location_df):
    BBox = (location_df.longitude.min(), location_df.longitude.max(),
             location_df.latitude.min(), location_df.latitude.max())
    return BBox

def plot_map(df, title="", image_location="", output_file="", BBox=None):
    # src: https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db

    if BBox is None:
        BBox = get_bounding_box(df)

    fig, ax = plt.subplots(figsize=(8, 7))

    ax.scatter(df.longitude, df.latitude, zorder=1, alpha=0.2, c='b', s=10)
    if title != "":
        ax.set_title(title)
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])

    plt.gca().set_aspect('equal', adjustable='datalim') # equal step sizes

    if image_location != "":
        # Generate image on https://www.openstreetmap.org/export
        # BBox for this site is (Left, Right, Bottom, Top) from get_bounding_box
        # After setting the box, hit share button on the left
        # Note: Currently not used (also not tested), because the export doesn't work

        ruh_m = plt.imread(image_location)
        ax.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')

    if output_file != "":
        plt.savefig(output_file)

    plt.show()


def generate_date_plot(df, dates_column_name='date', data_column_name='data', plot_title='', output_file=''):
    dates = mdates.datestr2num(df[dates_column_name])

    # src: https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()  # datums schuin

    plt.plot(dates, df[data_column_name])
    if plot_title != '':
        plt.title(plot_title)

    if output_file != '':
        plt.savefig(output_file)

    plt.show()

