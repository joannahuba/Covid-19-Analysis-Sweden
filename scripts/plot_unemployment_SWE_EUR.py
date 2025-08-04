# plot_unemployment_SWE_EUR

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

unemployment = pd.read_csv("../csv/Unemployment_Rate.csv")
unemployment = unemployment.melt(
    id_vars=['Country Name', 'Country Code'],
    value_vars=[str(year) for year in range(2010, 2025)],
    var_name='year',                             
    value_name='Unemployment Rate'  
)

Sweden = unemployment[unemployment['Country Name'] == 'Sweden']
Europe_avg = unemployment.groupby('year')['Unemployment Rate'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10.5, 6))

# parameters to apply_common_formatting
title = 'Unemployment Rate in Sweden and other European Countries'
x_label = 'Year'
y_label = 'Unemployment Rate'
x_major = 2
x_minor = 1
y_major = 3
y_minor = 1.5

# setting grid and tickets 
apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor)

ax.set_ylim(0, 13)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x}%'))

# Marking the most affected period by covid-19
ax.axvspan(xmin=10, xmax=12, color='lightblue', alpha=0.3, label='Crisis')

colors = [
    '#C0392B',  # Sweden
    '#2980B9',  # Denmark
    '#27AE60',  # Finland
    '#F4D03F',  # Norway
    '#8E44AD'   # Iceland
]


ax.plot(unemployment['year'].unique(), Sweden['Unemployment Rate'], label = 'Sweden')
ax.plot(Europe_avg['year'].unique(), Europe_avg['Unemployment Rate'], label = 'Europe average')


ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

if args.action == 0:
    plt.show()
elif args.action == 1:
    fig.savefig('../images/' + os.path.basename(os.path.splitext(__file__)[0] + '.png'),
                format='png', dpi=300, bbox_inches='tight', pad_inches=0.5)

