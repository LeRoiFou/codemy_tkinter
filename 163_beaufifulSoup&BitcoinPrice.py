"""
Tkinter - Codemy.com #163 : Bitcoin Price Web Scraper With BeautifulSoup - Python Tkinter GUI Tutorial #163
Lien : https://www.youtube.com/watch?v=LQsZyGNM9ag

Dans ce programme on apprend à connaître la valeur du Bitcoin toutes les 30 secondes à partir d'un site internet.
À la différence du module API, ici les données sont prises directement sur un site internet, comme par exemple connaître
le cours du fioul au jour le jour...

Le code source de la page web concernée a été copiée avec un clique droit de la souris sur la page web concernée ->
"Afficher le code source de la page" puis CTRL+A puis CTRL+C et CTRL+V dans un nouveau fichier .html afin de trouver le
nom de la classe où se trouve la ligne où est affichée la valeur du bitcoin

Package à télécharger : beautifulsoup4

Dans ce programme on affiche également le temps et la date actuel (voir tuto tkinter 79_Time&Locale)
Concernant l'instruction strftime du module time, voir le lien : https://www.tutorialspoint.com/python/time_strftime.htm

Éditeur : Laurent REYNAUD
Date : 19-01-21
"""

from tkinter import *
from bs4 import BeautifulSoup  # permet d'obtenir la mise à jour des données
import urllib  # récupération des données d'une URL
from urllib import request
from datetime import datetime  # mise à jour des données à un temps T
import locale  # conversion du module time en français

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('550x210')
root.config(bg='black')

"""Conversion des données du module time en français"""
locale.setlocale(locale.LC_TIME, 'FR')

"""Temps actuel"""
now = datetime.now()
current_time = now.strftime('%H:%M:%S')

"""Assignation d'une variable booléenne"""
global previous
previous = False

"""Configuration d'une fenêtre"""
my_frame = Frame(root, bg='black')
my_frame.pack(pady=20)

"""Chargement d'une image"""
logo = PhotoImage(file='images/bitcoin.png')
logo_label = Label(my_frame, image=logo, bd=0)
logo_label.grid(row=0, column=0, rowspan=2)

"""Ajout du label 'bitcoin'"""
bit_label = Label(my_frame, text='TEST', font='Helvetica 45', bg='black', fg='green', bd=0)
bit_label.grid(row=0, column=1, padx=20, sticky=S)

"""Dernière valeur du bitcoin"""
latest_price = Label(my_frame, text='test de déplacement', font='Helvetica 8', bg='black', fg='grey')
latest_price.grid(row=1, column=1, sticky=N)


def Update():
    """Mise à jour de la valeur du bitcoin toutes les 30 secondes"""

    """Assignation d'une variable booléenne"""
    global previous

    """Récupération de la valeur du bitcoin"""
    page = urllib.request.urlopen('https://www.coindesk.com/price/bitcoin').read()  # site internet de la valeur bitcoin
    html = BeautifulSoup(page, 'html.parser')  # récupération de la page source du site internet concerné
    price_large = html.find(class_='price-large')  # récupération du nom de la classe où se trouve la ligne de la valeur
    # du bitcoin
    print(price_large)  # affichage de la ligne récupérée du fichier .html
    price_large1 = str(price_large)  # conversion de la chaîne de récupération du fichier html en str
    price_large2 = price_large1[54:63]  # récupération de la valeur du bitcoin dans la str
    bit_label.config(text=f"${price_large2}")  # mise à jour de l'étiquette

    """Mise à jour de la fenêtre principale toutes les 30 secondes"""
    root.after(30_000, Update)  # 30_000 ms = 30 secondes

    """Temps actuel"""
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')

    """Mise à jour de la barre de statuts"""
    status_bar.config(text=f"Dernière mise à jour : {current_time}    ")

    """Sélection du cours en cours"""
    current = price_large2

    """Suppression de la virgule affichée à la valeur du bitcoin pour les centimes"""
    current = current.replace(',', '')

    """Détermination du changement de valeur entre deux visus"""
    if previous:  # si faux (la variable previous est toujours une booléenne)
        if float(previous) > float(current):  # si la valeur actuelle a diminué (la variable previous devient un float)
            latest_price.config(text=f"La valeur du Bitcoin a baissé de "
                                     f"{round(float(previous) - float(current), 2)} $", fg='red')
        elif float(previous) == float(current):  # si la valeur actuelle est inchangée
            latest_price.config(text='Valeur du bitcoin inchangée', fg='grey')
        else:  # si vrai :
            latest_price.config(text=f"La valeur du Bitcoin a augmenté de "
                                     f"{round(float(current) - float(previous), 2)} $", fg='green')
    else:  # sinon si vrai (la variable previous est toujours une booléenne)
        previous = current  # la variable previous devient un float
        latest_price.config(text='Valeur du bitcoin inchangée', fg='grey')


"""Création d'une barre de statuts"""
status_bar = Label(root, text=f"Dernière mise à jour : {current_time}    ", bd=0, anchor=E, bg='black', fg='grey')
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

Update()  # lancement du programme mise à jour toutes les 30 secondes
root.mainloop()
