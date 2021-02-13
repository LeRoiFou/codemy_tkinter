"""
Tkinter - Codemy.com #153 : Save To Dat File Instead of Databases - Python Tkinter GUI Tutorial #153
Lien : https://www.youtube.com/watch?v=l2Qs0GvI6Ho&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=153

Dans ce programme on apprend la sérialisation et la désérialisation avec le module pickle

Dans cet exemple on sérialise des données saisies dans le widget Text

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

from tkinter import *
import pickle

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x400')


def save_file():
    """Fonction permettant de sauvegarder les données"""

    """Assignation de l'obtention des données saisies dans la zone de texte"""
    stuff = my_text.get(1.0, END)

    """Assignation d'un nom de fichier"""
    file_name = 'data/dat_stuff'

    """Assignation de l'ouverture du fichier en mode écriture"""
    output_file = open(file_name, 'wb')

    """Ajout des données de la zone de texte (variable stuff) dans le fichier en mode écriture (variable output_file)"""
    pickle.dump(stuff, output_file)


def open_file():
    """Fonction permettant d'ouvrir le fichier"""

    """Assignation d'un nom de fichier"""
    file_name = 'data/dat_stuff'

    """Assignation de l'ouverture du fichier en mode lecture"""
    input_file = open(file_name, 'rb')

    """Assignation de la récupération des données sauvegardées"""
    stuff = pickle.load(input_file)

    """Insertion des données récupérées dans la zone de texte"""
    my_text.insert(1.0, stuff)
    print(stuff)


"""Assignation d'une liste de tailles"""
sizes = ['Petit', 'Moyen', 'Grand']

"""Configuration d'une zone de texte"""
my_text = Text(root, width=40, height=10)
my_text.pack(pady=20)

"""Configuration et affichage des boutons"""
my_button1 = Button(root, text='Sauvegarder', command=save_file)
my_button1.pack(pady=20)
my_button2 = Button(root, text='Ouvrir', command=open_file)
my_button2.pack(pady=20)

root.mainloop()
