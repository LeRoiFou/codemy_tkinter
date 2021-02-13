"""
Tkinter - Codemy.com #24 : interface de programmation (API)
Lien : https://www.youtube.com/watch?v=vJCjDevYDt8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=24

Lorsqu'une collectivité, un ministère ou une entreprise construit un site internet ou un logiciel qui utilise de la
donnée publique, elle a besoin de passer par une API.

Une API est un outil informatique qui permet à un site internet ou à un logiciel de communiquer avec un autre
ordinateur et échanger de la donnée.

Par exemple, quand les entreprises françaises font leur Déclaration Sociale Nominative, leur logiciel de paie
communique directement les données de leurs employés à l'Etat grace à... une API !

Éditeur : Laurent REYNAUD
Date : 10-11-2020
"""

from tkinter import *
from PIL import ImageTk, Image
import requests  # package téléchargé
import json

"""Configuration de la fenêtre"""
root = Tk()
root.title('Mon API :)')
root.geometry('400x40')
root.config(bg='green')

"""Récupération de l'URL de l'API météo US afin d'insérer les données dans le fichier JSON"""
try:
    """URL de l'API météo US -> https://docs.airnowapi.org/"""
    api_request = requests.get(
        'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode'
        '=89129&distance=5&API_KEY=A50C3B4E-303B-4E0F-B872-EFEBE4F92E26')
    """Contenu de l'URL de l'API météo inséré dans le fichier JSON qui est une liste de 3 dictionnaires"""
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']  # dictionnaire indice 0: récupération de la valeur de la clé 'ReportingArea'
    quality = api[0]['AQI']  # dictionnaire indice 0: récupération de la valeur de la clé 'AQUI'
    category = api[0]['Category']['Name']  # dictionnaire indice 0 : récupération dans le dictionnaire avec pour clé
    # 'Categorie', la valeur de la clé 'Name'
except Exception as e:
    pass
    api = 'Erreur...'

"""Configuration des Widgets"""
myLabel = Label(root, text=city + " qualité de l'air " + str(quality) + ' : ' + category, font='Helvetica 15',
                bg='green')
myLabel.pack()

root.mainloop()
