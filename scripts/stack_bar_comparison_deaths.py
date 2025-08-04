import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
import matplotlib
matplotlib.use('TkAgg')
import argparse

# setting option to display or save
parser = argparse.ArgumentParser(description="Choose whether to display the plot (0) or save it to a file (1).")
parser.add_argument('action', type=int, choices=[0, 1], help="0 - display the plot, 1 - save to file")
args = parser.parse_args()

pio.renderers.default = 'browser'  



comparison = pd.read_csv("../csv/comparison-SWE-DEN-NOR.csv")

data = [
    go.Bar(
        # Sweden non covid deaths
        x=comparison["year"],
        y=comparison["SWE-all_deaths"]-comparison["SWE-COVID-19_deaths"],
        name='Non-Covid-19 deaths in Sweden',
        offsetgroup="Sweden",
        marker=dict(color='#4B7BAA')
    ),
    go.Bar(
        # Sweden covid deaths
        x=comparison["year"],
        y=comparison["SWE-COVID-19_deaths"],
        name='Covid-19 deaths in Sweden',
        offsetgroup="Sweden",
        marker=dict(color='#A6C7E8')
    ),
    go.Bar(
        # Norway Denmark non covid
        x=comparison["year"],
        y=comparison["all_deaths_nor_den"] - comparison["COVID-19_deaths_nor_den"],
        name='Non-Covid-19 deaths average <br>in Norway and Denmark',
        offsetgroup="Norway_Denmark",
        marker=dict(color='#9A3B3B')
    ),
    go.Bar(
        # Norway Denmark non covid
        x=comparison["year"],
        y=comparison["COVID-19_deaths_nor_den"],
        name='Covid-19 deaths average <br>in Norway and Denmark',
        offsetgroup="Norway_Denmark",
        marker=dict(color='#DDAAAA')
    )
]

fig = go.Figure(data=data)
fig.update_layout(
    font=dict(
        family="Liberation Serif", 
        size=26,                    
        color="#2C3E50"            
    ),
    barmode='stack',
    title=dict(
        text="COVID-19 and Non-COVID-19 Deaths <br>in Sweden vs. Norway-Denmark Average",
        x=0.5,  
        xanchor='center',
        font=dict(
            family="Liberation Serif", 
            size=42,
            color="#2C3E50"
        )
    ),
    xaxis_title="Year",
    yaxis_title="Deaths per 100,000",
    margin=dict(t=140),
)

if args.action == 0:
    fig.show()
elif args.action == 1:
    fig.write_html('../images/plotly-stack-bar-comparison.html')
