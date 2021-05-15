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

import tkinter
from PIL import ImageTk, Image
import requests  # package téléchargé
import json

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon API :)')
        root.geometry('400x40')
        self.database()
        self.widgets()

    def database(self):
        # Récupération de l'URL de l'API météo US afin d'insérer les données dans le fichier JSON"""
        
        try:
            # URL de l'API météo US -> https://docs.airnowapi.org/"""
            api_request = requests.get(
                'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode'
                '=97317&distance=5&API_KEY=A50C3B4E-303B-4E0F-B872-EFEBE4F92E26')
            # Contenu de l'URL de l'API météo inséré dans le fichier JSON qui est une liste de 3 dictionnaires"""
            api = json.loads(api_request.content)
            self.city = api[0]['ReportingArea']  # dictionnaire indice 0: récupération de la valeur de la clé 'ReportingArea'
            self.quality = api[0]['AQI']  # dictionnaire indice 0: récupération de la valeur de la clé 'AQUI'
            """dictionnaire indice 0 : récupération dans le dictionnaire avec pour clé
            'Categorie', la valeur de la clé 'Name'"""
            self.category = api[0]['Category']['Name']  # 

            if self.category == 'Good':
                self.weather_color = '#00e400'
            elif category == 'Moderate':
                self.weather_color = '#ffff00'
            elif category == 'Unhealthy for Sensitive Groups':
                self.weather_color = '#ff7e00'
            elif category == 'Unhealthy':
                self.weather_color = '#ff0000'
            elif category == 'Very Unhealthy':
                self.weather_color = '#8f3f97'
            elif category == 'Hazardous':
                self.weather_color = '#7e0023'       
        except Exception as e:
            pass
            api = 'Erreur...'

    def widgets(self):
        # Configuration des Widgets"""

        root.config(bg=self.weather_color)
        
        myLabel = tkinter.Label(root, 
            text=self.city + " qualité de l'air " + str(self.quality) + ' : ' + self.category, 
            font='Helvetica 15',
            bg=self.weather_color)
        myLabel.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()