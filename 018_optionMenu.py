"""
Tkinter - Codemy.com #18 : Dropdown menus
Lien : https://www.youtube.com/watch?v=3E_fK5hCUnI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=18

Dans ce programme on apprend à afficher un menu déroulant avec des titres (bof...)

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

from tkinter import *

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.geometry('400x400')

options = ['Lundi',
           'Mardi',
           'Mercredi',
           'Jeudi',
           'Vendredi',
           'Samedi',
           'Dimanche'
           ]

clicked = StringVar()
clicked.set(options[2])  # affichage par défaut : Mercredi

drop = OptionMenu(root, clicked, *options)  # argument options précédé de l'*' pour un affichage vertical des données
drop.pack()


def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()


myButton = Button(root, text='Montrer la sélection', command=show)
myButton.pack()

root.mainloop()
