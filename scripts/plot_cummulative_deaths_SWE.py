# plot_cummulative_deaths_SWE

# imports
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import rcParams 
import os
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

df = pd.read_csv("../csv/SWEDEN-weekly-cases-deaths.csv")
df['Date_reported'] = pd.to_datetime(df['Date_reported'])

# figure
fig, ax = plt.subplots(figsize=(10.5, 6))

# parameters to apply_common_formatting
title = 'Cummulative deaths in Sweden'
x_label = 'Date'
y_label = 'Deaths (cummulative)'
x_major = 14
x_minor = 7
y_major = 6000
y_minor = 3000
date_formatter = True

# setting grid and tickets 
apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor, date_formatter)

# marking the period after the start of the vaccination program
ax.axvspan(
    xmin=pd.to_datetime("2021-01-01"),
    xmax=pd.to_datetime("2025-04-27"),
    color='lightblue',
    alpha=0.3,
    label='after vaccine'
)

# Sweden deaths
ax.plot(df['Date_reported'].unique(), df['Cumulative_deaths'], label = "deaths (cummulative)", color='#C0392B')
ax.legend()

if args.action == 0:
    plt.show()
elif args.action == 1:
    fig.savefig('../images/' + os.path.basename(os.path.splitext(__file__)[0] + '.png'),
                format='png', dpi=300, bbox_inches='tight', pad_inches=1.0)