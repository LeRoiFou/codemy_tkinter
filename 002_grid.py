"""
Tkinter - Codemy.com #2 : positionnement des widgets avec l'instruction grid()
Lien : https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2

Dans ce programme on apprend à position les widgets avec l'instruction grid()

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

from tkinter import *

root = Tk()

"""Etiquette"""
myLabel1 = Label(root, text='Bonjour !')
myLabel2 = Label(root, text='Mon nom est John Gerald')

"""Affichage"""
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)  # équivaut à la colonne 2 car rien n'est saisi de la colonne 2 à 4

root.mainloop()
