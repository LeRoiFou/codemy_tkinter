"""
Lien : https://www.youtube.com/watch?v=lKXePw01R2A
Cours : Create your Plotly Dash Multipage App - Beta Version

Voir fichier indexC008 et indexC009
Date : 29-08-2023
"""

from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import numpy as np

register_page(__name__)

np.random.seed(2020)

layout = html.Div(
    [
        dcc.Graph(id="histograms-graph"),
        html.P("Mean:"),
        dcc.Slider(
            id="histograms-mean", min=-3, max=3, value=0, marks={-3: "-3", 3: "3"}
        ),
        html.P("Standard Deviation:"),
        dcc.Slider(id="histograms-std", min=1, max=3, value=1, marks={1: "1", 3: "3"}),
    ]
)


@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
)
def display_color(mean, std):
    data = np.random.normal(mean, std, size=500)
    fig = px.histogram(data, nbins=30, range_x=[-10, 10])
    fig.update_layout(showlegend=False)
    return fig
