# plot_vaccine_doses_SWE

# imports
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams 
from plot_utils import apply_common_formatting
import os
import argparse

# setting option to display or save
parser = argparse.ArgumentParser(description="Choose whether to display the plot (0) or save it to a file (1).")
parser.add_argument('action', type=int, choices=[0, 1], help="0 - display the plot, 1 - save to file")
args = parser.parse_args()

rcParams['font.family'] = 'Liberation Serif' 
rcParams['font.size'] = 16                  
rcParams['text.color'] = '#2C3E50' 

df = pd.read_csv("../csv/cumulative-covid-vaccinations.csv")
df['Day'] = pd.to_datetime(df['Day'])

fig, ax = plt.subplots(figsize=(10.5, 6))

# parameters to apply_common_formatting
title = 'Number of Covid-19 doses in Sweden'
x_label = 'Year'
y_label = 'Number of vaccine doses(cummulative)'
x_major = 8
x_minor = 4
y_major = 5000000
y_minor = 2500000
date_formatter = True

# setting grid and tickets 
apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor, date_formatter)

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000000)}mln')) 

for spine in ax.spines.values():
    spine.set_visible(False)

# Sweden
ax.plot(df['Day'].unique(), df['COVID-19 doses (cumulative)'], label = "vaccine doses (cummulative)", color='#C0392B')
ax.legend()

if args.action == 0:
    plt.show()
elif args.action == 1:
    fig.savefig('../images/' + os.path.basename(os.path.splitext(__file__)[0] + '.png'),
                format='png', dpi=300, bbox_inches='tight', pad_inches=1.0)