"""
Lien : https://www.youtube.com/watch?v=lKXePw01R2A
Cours : Create your Plotly Dash Multipage App - Beta Version

Voir fichier indexC008 et indexC009
Date : 29-08-2023
"""

from dash import html, register_page

register_page(__name__, path="/404")


layout = html.H1("Custom 404")
