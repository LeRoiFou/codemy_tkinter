"""
Cours : indexG001_Multipages.py
Onglet : "Graphique"
"""

from dash import html, dcc, Input, Output, State, callback, register_page
import plotly.express as px
import pandas as pd

# URL d'accès
register_page(__name__, 
              path="/bargraph") # URL d'accès

# Configuration de la page @
layout = html.Div(
    [
        # Label
        html.P("Choose Day:"),
        
        # Zone vide : menu déroulant
        html.Div(id="dropdown-container", children=[]),
        
        # Zone vide : graphique diagramme en barres
        html.Div(id="bar-container", children=[]),
    ]
)

# MAJ du menu déroulant à partir des données de la DF assignée dans le fichier
# indexG001_Multipage.py
@callback(
    Output("dropdown-container", "children"),  # Sortie : menu déroulant
    Input("stored-data", "data")) # Entrée : données de la DF converties en dict
def populate_dropdownvalues(data):
    
    # Récupération des données converties en DF pandas
    dff = pd.DataFrame(data)
    
    # MAJ du menu déroulant
    return dcc.Dropdown(
        # Attention, ID créé dans le callback (ce n'était pas obligatoire): 
        # Fonction suppress_callback_exceptions à ajouter à la page principale !
        id="dropdown", 
        # Compréhension de liste : récupération des jours avec l'instruction 
        # unique() dans la DF
        options=[{"label": x, "value": x} for x in dff.day.unique()],
        value=dff.day.unique()[0], # Valeur par défaut : Sunday
        clearable=False, # Pas de possibilité de supprimer la valeur affichée
        style={"width": "50%"}, # Largeur du menu déroulant
        persistence=True, # Garde la valeur si changement de page @
        persistence_type="session" # en lien avec la précédente instruction si True
    ),

# MAJ du graphique à partir du menu déroulant
@callback(
    [Output("bar-container", "children"), # Sortie : graphique
     Output("store-dropdown-value", "data") # Sortie : données dans le menu déroulant
     ], 
    [Input("dropdown", "value"), # Entrée : menu déroulant
     State("stored-data", "data") # Entrée : données de la DF convertie en dict
     ]
)
def graph_and_table(dropdown_day, data): # 2 entrées
    
    # Récupération des données converties en DF
    dff = pd.DataFrame(data)
    
    # Filtre opéré sur la valeur sélectionnée dans le champ 'day' : récupérer
    # la valeur sélectionnée dans le menu déroulant
    dff = dff[dff["day"] == dropdown_day]
    
    # MAJ du graphique
    fig = px.bar(dff, x="sex", y="total_bill", color="smoker", barmode="group")
    
    # la variable dropdown_day va être utilisée pour la MAJ de l'autre page @
    # concernant la datatable
    return dcc.Graph(figure=fig), dropdown_day
