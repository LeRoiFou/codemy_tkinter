"""
Tkinter - Codemy.com #160 : Changing The Mouse Cursor - Python Tkinter GUI Tutorial #160
Lien : https://www.youtube.com/watch?v=qRQZAsKI0kA

Dans ce programme on apprend à changer le curseur de la souris

Éditeur : Laurent REYNAUD
Date : 08-01-21
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')
root.config(cursor='fleur')  # curseur de la souris = 4 flêches en forme de croix

"""Assignation dans une liste des différents types de curseur"""
my_list = ['arrow',  # flêche
           'circle',  # cercle
           'clock',  # horloge
           'cross',  # croix
           "dotbox",  # boîte de carrés
           "exchange",  # échange par des flêches
           'fleur',  # 4 flêches en forme de croix
           'heart',  # coeur
           'man',  # homme
           'mouse',  # souris
           'pirate',  # pirate
           'plus',  # croix
           'shuttle',  # fusée
           'sizing',  # carré dimensionné
           'spider',  # araignée
           'spraycan',  # aérosol
           'star',  # étoile
           'target',  # cible
           'tcross',  # croix
           'trek']  # randonneur

count = 0
for i in range(5):  # Total row - 5
    for j in range(4):  # Total column - 4
        Button(root, text=my_list[count], cursor=my_list[count], width=10).grid(row=i, column=j, padx=10, pady=10)
        count += 1

root.mainloop()
