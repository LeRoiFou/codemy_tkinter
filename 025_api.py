"""
Tkinter - Codemy.com #25 : interface de programmation (API)
Lien : https://www.youtube.com/watch?v=ARQH_3_Erao&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=25

Lorsqu'une collectivité, un ministère ou une entreprise construit un site internet ou un logiciel qui utilise de la
donnée publique, elle a besoin de passer par une API.

Une API est un outil informatique qui permet à un site internet ou à un logiciel de communiquer avec un autre
ordinateur et échanger de la donnée.

Par exemple, quand les entreprises françaises font leur Déclaration Sociale Nominative, leur logiciel de paie
communique directement les données de leurs employés à l'Etat grace à... une API !

Dans ce script, on ajuste la couleur selon le degré de pollution de l'encdroit choisi

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

"""Récupération de l'URL de l'API météo US afin d'insérer les données dans le fichier JSON"""
try:
    """URL de l'API météo US -> https://docs.airnowapi.org/"""
    api_request = requests.get(
        'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode'
        '=97317&distance=5&API_KEY=A50C3B4E-303B-4E0F-B872-EFEBE4F92E26')
    """Contenu de l'URL de l'API météo inséré dans le fichier JSON qui est une liste de 3 dictionnaires"""
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']  # dictionnaire indice 0: récupération de la valeur de la clé 'ReportingArea'
    quality = api[0]['AQI']  # dictionnaire indice 0: récupération de la valeur de la clé 'AQUI'
    category = api[0]['Category']['Name']  # dictionnaire indice 0 : récupération dans le dictionnaire avec pour clé
    # 'Categorie', la valeur de la clé 'Name'

    if category == 'Good':
        weather_color = '#00e400'
    elif category == 'Moderate':
        weather_color = '#ffff00'
    elif category == 'Unhealthy for Sensitive Groups':
        weather_color = '#ff7e00'
    elif category == 'Unhealthy':
        weather_color = '#ff0000'
    elif category == 'Very Unhealthy':
        weather_color = '#8f3f97'
    elif category == 'Hazardous':
        weather_color = '#7e0023'

    root.config(bg=weather_color)

    """Configuration des Widgets"""
    myLabel = Label(root, text=city + " qualité de l'air " + str(quality) + ' : ' + category, font='Helvetica 15',
                    bg=weather_color)
    myLabel.pack()

except Exception as e:
    pass
    api = 'Erreur...'

root.mainloop()
