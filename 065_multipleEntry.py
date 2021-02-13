"""
Tkinter - Codemy.com #65 : Creating Multiple Entry Boxes Automatically - Python Tkinter GUI Tutorial #65
Lien : https://www.youtube.com/watch?v=H3Cjtm6NuaQ

Dans ce programme on apprend à afficher plusieurs champs de saisis avec une boucle

Éditeur : Laurent REYNAUD
Date : 06-02-21
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('700x500')

"""Assignation d'une liste"""
my_entries = []


def something():
    """Fonction permettant d'afficher ce que l'on saisit dans les champs de saisis"""

    """Assignation d'une str"""
    entry_list = ''

    """Affichage des données de la liste 'my_entries' en tant que str"""
    for data in my_entries:  # pour chaque donnée dans la liste 'my_entries'...
        entry_list = entry_list + str(data.get()) + '\n'  # conversion des données de la liste 'my_entries' en str
        my_label.config(text=entry_list)


"""Configuration des champs de saisis en recourant à la boucle  'for in range'"""
for x in range(5):  # nombre de libnes = 5
    for y in range(5):  # nombre de colonnes = 5
        my_entry = Entry(root)
        my_entry.grid(row=x, column=y, pady=20, padx=5)
        my_entries.append(my_entry)  # ajout des données écrites dans les champs de saisis dans la liste 'my_entries'

"""Configuration du bouton d'exécution"""
my_button = Button(root, text='Appuie !', command=something)
my_button.grid(row=6, column=0, pady=20)

"""Configuration du l'étiquette"""
my_label = Label(root, text='')
my_label.grid(row=7, column=0, pady=20)

root.mainloop()
