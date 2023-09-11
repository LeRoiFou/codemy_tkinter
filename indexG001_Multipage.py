"""
Lien : https://www.youtube.com/watch?v=Np090pWEjIs&list=PLh3I780jNsiQWkxk05ek4M7rbLocVQaAb&index=2
Cours : Sharing Data between Multipage App Pages - Plotly Dash

Documentation sur le partage des données :
https://dash.plotly.com/sharing-data-between-callbacks

Documentation sur le composant store :
https://dash.plotly.com/dash-core-components/store

Le composant store permet d'interagir auprès de composants situés dans différentes
pages @
Ce composant comporte une identité et une propriété (data) dont ces valeurs sont
obligatoirement déclarées sur la page principale (pour ce cours -> ce fichier)

Date : 11-09-23
"""

from dash import Dash, dcc, page_container
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px

# Récupération des données DF pandas
df = px.data.tips()
# print(df.head())

# convert dataframe to list of dictionaries because dcc.Store
# accepts dict | list | number | string | boolean
df = df.to_dict('records')

app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.FLATLY],  # Mise en forme de la page @
    # Permet d'éviter des erreurs lorsqu'un ID d'un composant a été créé dans un
    # callback et que cet ID va être utilisé dans un autre callback
    # Dans ce tuto, voir l'ID 'dropdown' dans le fichier bargraph.py
    suppress_callback_exceptions=True, 
    use_pages=True # récupération des fichiers .py dans le répertoire 'pages'
)

# Configuration du menu déroulant
navbar = dbc.NavbarSimple(
    
    # Menu déroulant pour lister les onglets
    dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem(
                "Datatable", # Nom à afficher sur la page @
                href="/" # Fichier datatable.py dans le répertoire 'pages'
                ), 
            dbc.DropdownMenuItem(
                "Graphique", # Nom à afficher sur la page @
                href="/bargraph" # Fichier bargraph.py dans le repertoire 'pages'
                ),
            ],
        nav=True, # Toujours True (mise en forme bouton liste onglets)
        label="Mes onglets", # Nom du menu déroulant
    ),
    brand="Titre de la bannière", # Titre de la bannière du menu déroulant
    color="info", # Couleur de la bannière du menu déroulant
    dark=True, # Couleur du texte : dark = texte en blanc...
    className="mb-2",
)

# Configuration de la page @
app.layout = dbc.Container(
    [
        navbar, # Menu déroulant
        
        page_container, # Contenu de la page @
        
        # Ce composant permet de récupérer les données de la DF de ce fichier
        # pour pouvoir être alimenté sur les deux pages @ : datatable et graphique
        dcc.Store(id="stored-data", # identifiant
                  data=df), # propriété : DF récupérée convertie en dict
        
        # Ce composant permet de récupérer les données dans le menu déroulant de 
        # la page @ 'graphique' afin de pouvoir alimenter les données de la 
        # datatable de la page @ 'datatable
        dcc.Store(id="store-dropdown-value", # identifiant
                  data=None) # propriété : menu déroulant intervenant sur la datatable
     ],
    fluid=True # Affichage sur la page entière
    )

if __name__ == "__main__":
    app.run_server(debug=True, port=8003)
