"""
Tkinter - Codemy.com #26 : interface de programmation (API)
Lien : https://www.youtube.com/watch?v=Lcb6PTjnTOo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=26

Lorsqu'une collectivité, un ministère ou une entreprise construit un site internet ou un logiciel qui utilise de la
donnée publique, elle a besoin de passer par une API.

Une API est un outil informatique qui permet à un site internet ou à un logiciel de communiquer avec un autre
ordinateur et échanger de la donnée.

Par exemple, quand les entreprises françaises font leur Déclaration Sociale Nominative, leur logiciel de paie
communique directement les données de leurs employés à l'Etat grace à... une API !

Dans ce script, on ajuste la couleur selon le degré de pollution de l'encdroit choisi

Éditeur : Laurent REYNAUD
Date : 12-11-2020
"""

import tkinter
import requests  # package téléchargé
import json

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon API :)')
        root.geometry('600x100')
        self.widgets()

    def zipLookup(self):
        # Cette fonction permet de donner la pollution de l'air en récupérant le code postal saisi dans le champ Entry
        # zip.get()  # récupération des données saisies dans le champ de saisie
        # zipLabel = Label(root, text=zip.get())
        # zipLabel.grid(row=1, column=0, columnspan=2)

        # Récupération de l'URL de l'API météo US afin d'insérer les données dans le fichier JSON
        try:
            # URL de l'API météo US -> https://docs.airnowapi.org/"""
            api_request = requests.get(
                'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() +
                '&distance=5&API_KEY=A50C3B4E-303B-4E0F-B872-EFEBE4F92E26')
            # Contenu de l'URL de l'API météo inséré dans le fichier JSON qui est une liste de 3 dictionnaires"""
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

            # Configuration des Widgets"""
            myLabel = tkinter.Label(root, 
                text=city + " qualité de l'air " + str(quality) + ' : ' + category, 
                font='Helvetica 15',
                bg=weather_color)
            myLabel.grid(row=1, column=0, columnspan=2)

        except Exception as e:
            api = 'Erreur...'

    def widgets(self):

        # Widget champ de saisi du code postal"""
        zipEntry = tkinter.Entry(root, justify='center')
        zipEntry.grid(row=0, column=0, 
        stick='w' + 'e' + 'n' + 's')  # stick=W+E+S : adaptation avec la réponse obtenue du widget étiquette

        # Widget pour valider le code postal saisi"""
        zipButton = tkinter.Button(root, text='Rechercher le code postal', command=self.zipLookup)
        zipButton.grid(row=0, column=1,
        stick='w' + 'e' + 'n' + 's')  # stick=W+E+S : adaptation avec la réponse obtenue du widget étiquette


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()