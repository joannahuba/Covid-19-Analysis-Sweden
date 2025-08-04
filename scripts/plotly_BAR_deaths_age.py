import plotly.graph_objects as go
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import argparse

# setting option to display or save
parser = argparse.ArgumentParser(description="Choose whether to display the plot (0) or save it to a file (1).")
parser.add_argument('action', type=int, choices=[0, 1], help="0 - display the plot, 1 - save to file")
args = parser.parse_args()


# Load data
df = pd.read_csv("../csv/SWEDEN-AGE-GROUPS-DEATHS_per100K.csv")

# Unique age groups (will correspond to bar colors)
age_groups = df["age_group"].unique()
age_groups = age_groups[6:]
years = df["year"].unique()

bars = []
colors = ['#7FB3D5',  
          '#1F618D',  
          '#F4D03F',   
          '#C0392B',   
          '#5D6D7E',   
          '#C0392B']
 
# Generate bars: one color per age group
for i, age_group in enumerate(age_groups):
    df_age = df[df["age_group"] == age_group]
    bar = go.Bar(
        x=df_age["year"],
        y=df_age["deaths_per_100K"],
        name=age_group, 
        marker=dict(color=colors[i])
    )
    bars.append(bar)

# Create figure
fig = go.Figure(data=bars)
fig.update_layout(
    font=dict(
        family="Liberation Serif",  
        size=30,                 
        color="#2C3E50"            
    ),
    barmode='group',
    title=dict(
        text="Deaths per 100K by Year and Age Group",
        x=0.5,  # center title
        xanchor='center',
        font=dict(
            family="Liberation Serif",  
            size=45,
            color="#2C3E50"
        )
    ),
    xaxis_title="Year",
    yaxis_title="Deaths per 100,000",
)

if args.action == 0:
    fig.show()
elif args.action == 1:
    fig.write_html('../images/plotly-BAR-deaths_age.html')
