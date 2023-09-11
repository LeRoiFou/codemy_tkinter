"""
Lien : https://www.youtube.com/watch?v=lKXePw01R2A
Cours : Create your Plotly Dash Multipage App - Beta Version

Voir fichier indexC008 et indexC009
Date : 29-08-2023
"""

from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px

register_page(
    __name__, 
    # path="/"
    ) # Premier élément à afficher dans la liste des onglets

df = px.data.medals_wide(indexed=True)

layout = html.Div(
    [
        html.P("Medals included:"),
        dcc.Checklist(
            id="heatmaps-medals",
            options=[{"label": x, "value": x} for x in df.columns],
            value=df.columns.tolist(),
        ),
        dcc.Graph(id="heatmaps-graph"),
    ]
)


@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig
