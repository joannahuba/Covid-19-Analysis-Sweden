# plot_inflation_SWE_NOR

# imports
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams 
from plot_utils import apply_common_formatting
import argparse

# setting option to display or save
parser = argparse.ArgumentParser(description="Choose whether to display the plot (0) or save it to a file (1).")
parser.add_argument('action', type=int, choices=[0, 1], help="0 - display the plot, 1 - save to file")
args = parser.parse_args()

# global style
rcParams['font.family'] = 'Liberation Serif' 
rcParams['font.size'] = 16                   
rcParams['text.color'] = '#2C3E50' 

nordic_countries= [
    "Sweden",
    "Denmark",
    "Finland",
    "Norway",
    "Iceland"
]

unemployment = pd.read_csv("../csv/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_37769.csv", skiprows=4)
unemployment_nor = unemployment[unemployment['Country Name'].isin(nordic_countries)]
unemployment = unemployment.melt(
    id_vars=['Country Name', 'Country Code'],
    value_vars=[str(year) for year in range(2010, 2025)],
    var_name='year',                             
    value_name='Inflation'  
)

fig, ax = plt.subplots(figsize=(10.5, 6))

# parameters to apply_common_formatting
title = 'Inflation in Sweden and other Nordic Countries'
x_label = 'Year'
y_label = 'Inflation'
x_major = 2
x_minor = 1
y_major = 3
y_minor = 1.5

# setting grid and tickets 
apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor)

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x}%'))
ax.set_ylim(-1, 13)

# Marking the period which Covid-19 affected the most
ax.axvspan(xmin=10, xmax=12, color='lightblue', alpha=0.3, label='Crisis')

colors = [
    '#C0392B',  # Sweden
    '#2980B9',  # Denmark
    '#27AE60',  # Finland
    '#F4D03F',  # Norway
    '#8E44AD'   # Iceland
]

for i, country in enumerate(nordic_countries):
    ax.plot(unemployment['year'].unique(), unemployment[unemployment['Country Name'] == country]['Inflation'], label = country, color=colors[i])



ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

if args.action == 0:
    plt.show()
elif args.action == 1:
    fig.savefig('../images/' + os.path.basename(os.path.splitext(__file__)[0] + '.png'),
                format='png', dpi=300, bbox_inches='tight', pad_inches=1.0)