# ani_SWE_NOR_EUR_cases

# imports
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams
from plot_utils import apply_common_formatting
import argparse

# parser
parser = argparse.ArgumentParser(description="Choose whether to display the plot (0) or save it to a file (1).")
parser.add_argument('action', type=int, choices=[0, 1], help="0 - display the plot, 1 - save to file")
args = parser.parse_args()


rcParams['font.family'] = 'Liberation Serif' 
rcParams['font.size'] = 16.9     
rcParams['text.color'] = '#2C3E50' 

europe = pd.read_csv("../csv/europe_avg.csv") # df with info about stats in Europe
europe = europe.rename(columns={"cases_per_100": "cases_per_100_e", "deaths_per_100": "deaths_per_100_e"})
europe["Date_reported"] = pd.to_datetime(europe["Date_reported"])


nordic_countries= [
    "Sweden",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland"
]
countries_per_100 = pd.read_csv("../csv/cases_per_100.csv")
countries_per_100 = countries_per_100[countries_per_100["Country"].isin(nordic_countries)]

# Sweden data
sweden = countries_per_100[countries_per_100["Country"] == "Sweden"].copy()
sweden = sweden.rename(columns={"cases_per_100": "cases_per_100_s", "deaths_per_100": "deaths_per_100_s"})

# Nordic except Sweden average
nordic = countries_per_100[countries_per_100["Country"] != "Sweden"].copy()
nordic = nordic.groupby(by=["Date_reported"], as_index=False)[["cases_per_100", "deaths_per_100"]].mean()

# Sweden and nordic
merge_df = sweden[["Date_reported", "Country", "cases_per_100_s", "deaths_per_100_s"]].merge(nordic[['Date_reported', 'deaths_per_100', 'cases_per_100']], left_on=['Date_reported'], right_on=['Date_reported'], how='left')
merge_df["Date_reported"] = pd.to_datetime(merge_df["Date_reported"])
merge_df["date_to_nums"] = range(len(merge_df))
merge_w_e = merge_df[["Date_reported", "Country", "cases_per_100_s", "deaths_per_100_s", 'deaths_per_100', 'cases_per_100']].merge(europe[['Date_reported', 'deaths_per_100_e', 'cases_per_100_e']], left_on=['Date_reported'], right_on=['Date_reported'], how='left')

fig, ax = plt.subplots(figsize=(10.5, 6))

line_s, = ax.plot([], [], label = "Sweden", color='#C0392B', linewidth=2.5)
line_w, = ax.plot([], [], label = "Nordic countries", color='#2980B9', linewidth=2.5, linestyle='--')
line_e, = ax.plot([], [], label = "Europe", color='#F4D03F', linewidth=2.5, linestyle='--')
ax.legend()

# parameters to apply_common_formatting
title = f'COVID-19 Cases per Million: \nSweden vs Nordic Countries vs Europe'
x_label = 'Reporting day'
y_label = 'Number of cases per 1 mln'
x_major = 6
x_minor = 3
y_major = 4000
y_minor = 2000
date_formatter = True

# setting grid and tickets 
apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor, date_formatter)

# limits
y_down_limit = min(merge_df["cases_per_100"].min(), merge_df["cases_per_100_s"].min())
y_down_limit = min(y_down_limit, merge_w_e["cases_per_100_e"].min())
y_up_limit = max(merge_df["cases_per_100"].max(), merge_df["cases_per_100_s"].max())
y_up_limit = max(y_up_limit, merge_w_e["cases_per_100_e"].max())
ax.set_ylim([y_down_limit, y_up_limit])
ax.set_xlim([merge_w_e["Date_reported"].min(), merge_w_e["Date_reported"].max()])

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}K'))

ax.legend()

date_format = mdates.DateFormatter('%b %Y') 

def update(frame):
    row = merge_w_e[merge_w_e["Date_reported"] <= frame]
    data_x = row["Date_reported"]
    data_y_s = row["cases_per_100_s"]
    data_y_n = row["cases_per_100"]
    data_y_e = row["cases_per_100_e"]
    line_s.set_ydata(data_y_s)
    line_s.set_xdata(data_x)
    line_w.set_ydata(data_y_n)
    line_w.set_xdata(data_x)
    line_e.set_ydata(data_y_e)
    line_e.set_xdata(data_x)

    # Konwersja datetime na numeryczny format matplotlib
    num_date = mdates.date2num(frame)
    formatted_date = date_format.format_data(num_date)

    for txt in ax.texts:
        txt.remove()
    ax.text(0.1, 0.9, formatted_date, transform=ax.transAxes, fontsize=22)

    return [line_s, line_w]


ani = FuncAnimation(fig, update, frames=merge_df["Date_reported"], blit=False, repeat=True)

if args.action == 0:
    plt.tight_layout()
    plt.show()
elif args.action == 1:
    plt.tight_layout()
    ani.save('../images/' + os.path.basename(os.path.splitext(__file__)[0] + '.gif'), fps=20)
