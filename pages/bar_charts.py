"""
Lien : https://www.youtube.com/watch?v=lKXePw01R2A
Cours : Create your Plotly Dash Multipage App - Beta Version

Voir fichier indexC008 et indexC009
Date : 29-08-2023
"""

from dash import Dash, dcc, html, Input, Output, callback, register_page
import plotly.express as px

register_page(__name__)

df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
            style={"width": "50%"}
        ),
        dcc.Graph(id="bar-chart"),
    ]
)


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig
