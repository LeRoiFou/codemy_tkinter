"""
Cours : indexG001_Multipages.py
Onglet : "Datatable"
"""

from dash import (html, Input, Output, callback, 
                  dash_table, register_page)
import pandas as pd

# URL d'accès
register_page(__name__,
              path='/', # URL d'accès : page d'accès par défaut
              ) 

# Configuration de la page @
layout = html.Div(
    [
        # Zone vide pour afficher la datatable
        html.Div(id="table-container", children=[]),
    ]
)

# MAJ de la datatable
@callback(Output("table-container", "children"), # Sortie : datatable
          [Input("stored-data", "data"), # Entrée : données de la DF convertie en dict
           Input("store-dropdown-value", "data") # Entrée : données du menu déroulant
           ])
def populate_checklist(data, day):
    
    # Si aucune valeur n'a été sélectionnée dans le menu déroulant de la page @
    # 'graphique' : message d'information
    if day is None: # None : valeur attribuée par défaut dans dcc.Store
        return html.H5("Choisir svp un jour dans l'onglet Graphique")
    
    # Récupération des données convertis en DF pandas du fichier indexG001
    dff = pd.DataFrame(data)
    
    # Filtre opéré sur la valeur sélectionnée dans le champ 'day' : récupérer
    # la valeur sélectionnée dans le menu déroulant de la page @ 'graphique'
    dff = dff[dff["day"] == day]
    
    # MAJ de la datatable dans la page @
    my_table = dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in dff.columns],
                    data=dff.to_dict('records'),
                )
    
    return my_table # 1 sortie = datatable
