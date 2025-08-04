# multiple_plots_cases

# imports
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import matplotlib.dates as mdates
from matplotlib import rcParams
from matplotlib.ticker import FuncFormatter
from plot_utils import apply_common_formatting
import argparse

# setting option to display or save
parser = argparse.ArgumentParser(description="Choose whether to display the plot (0) or save it to a file (1).")
parser.add_argument('action', type=int, choices=[0, 1], help="0 - display the plot, 1 - save to file")
args = parser.parse_args()

# global style
rcParams['font.family'] = 'Liberation Serif' 
rcParams['font.size'] = 15                    
rcParams['text.color'] = '#2C3E50'          


date_format = mdates.DateFormatter('%b %Y') 
nordic_countries= [
    "Sweden",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland"
]

countries_per_100 = pd.read_csv("../csv/cases_per_100.csv")
countries_per_100["Date_reported"] = pd.to_datetime(countries_per_100["Date_reported"])
countries_per_100 = countries_per_100[countries_per_100["Country"].isin(nordic_countries)]


fig, axs = plt.subplots(2, 3, figsize = (11.5, 6))
fig.delaxes(axs[1, 2])

fig.text(-0.08, 0.5, 'cases [K]', va='center', rotation='vertical', fontsize=23)
fig.text(0.0, 1.09, 'Confirmed COVID-19 Cases per 1 mln People in the Nordic Region', va='center', rotation='horizontal', fontsize=32)

plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.05, wspace=0.1, hspace=0.2)

countries = countries_per_100["Country"].drop_duplicates().tolist()
 
colors = [
    '#C0392B',  # Sweden
    '#2980B9',  # Denmark
    '#27AE60',  # Finland
    '#F4D03F',  # Norway
    '#8E44AD'   # Iceland
]

x_vec = countries_per_100['Date_reported'].unique()
color_idx = 0




for row, i in enumerate(axs):
    for col, ax in enumerate(i):
        # limits
        y_down_limit = countries_per_100["cases_per_100"].min()
        y_up_limit =  countries_per_100["cases_per_100"].max()
        ax.set_ylim([0, y_up_limit])

        # parameters to apply_common_formatting
        title = ''
        x_label = ''
        y_label = ''
        x_major = 10
        x_minor = 5
        y_major = 20000
        y_minor = 10000
        date_formatter = True

        # setting grid and tickets 
        apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor, date_formatter)

        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}K'))

    
        if row!=1:
            ax.tick_params(axis='x', which='both', labelbottom=False, length=0)

        if col!=0:
            ax.tick_params(axis='y', which='both', labelleft=False, length=0)
        
        for spine in ax.spines.values():
            spine.set_visible(False)

for i, country in enumerate(countries):
    row = i // 3
    col = i % 3
    axs[row, col].set_title(country, fontsize=25)
    axs[row, col].plot(countries_per_100[countries_per_100["Country"] == country]["Date_reported"], 
                       countries_per_100[countries_per_100["Country"] == country]["cases_per_100"], 
                       label = country, 
                       color = colors[color_idx], 
                       linewidth = 2)
    color_idx += 1



fig.legend(loc='upper left', bbox_to_anchor=(1, 0.98), ncol=1, fontsize=20)

if args.action == 0:
    plt.show()
elif args.action == 1:
    fig.savefig('../images/' + os.path.basename(os.path.splitext(__file__)[0] + '.png'),
                format='png', dpi=300, bbox_inches='tight', pad_inches=1.0)
