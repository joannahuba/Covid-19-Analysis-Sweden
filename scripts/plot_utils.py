# plot_utils

# imports
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mdates

def apply_common_formatting(ax, title, x_label, y_label, x_major, x_minor, y_major, y_minor, date_formatter=False):
    '''Setting of grid and tickets'''

    ax.set_title(title, fontsize=24.7)

    # x and y labels
    ax.set_xlabel(x_label, fontsize=20.8)
    ax.set_ylabel(y_label, fontsize=20.8)

    ax.set_facecolor('#EAF4FB')

    if date_formatter:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=x_major))
        ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=x_minor))
    else:
        ax.xaxis.set_major_locator(MultipleLocator(x_major))
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor))

    # y tickets
    ax.yaxis.set_major_locator(MultipleLocator(y_major))
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor))

    # grid setting
    ax.xaxis.grid(True, 'minor', color='#FFFFFF', linewidth=0.5)
    ax.yaxis.grid(True, 'minor', color='#FFFFFF', linewidth=0.5)
    ax.xaxis.grid(True,'major', color='#FFFFFF', linewidth=1)
    ax.yaxis.grid(True,'major', color='#FFFFFF', linewidth=1)

    ax.tick_params(axis='both', which='major', labelsize=15.6, color="#EAF4FB") 
    ax.tick_params(axis='both', which='minor', labelsize=15.6, color="#EAF4FB")

    for spine in ax.spines.values():
        spine.set_visible(False)