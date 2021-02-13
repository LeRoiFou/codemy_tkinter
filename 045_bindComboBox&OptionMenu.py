"""
Tkinter - Codemy.com #45 : Binding Dropdown Menus and Combo Boxes
Lien : https://www.youtube.com/watch?v=OPUSBBD2OJw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=45

Création d'un bouton avec une liste des données + barre de menu déroulant

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x400')
root.title("Titre !")


def selected(event):
    if clicked.get() == 'vendredi':
        myLabel = Label(root, text="C'est vendredi !").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()


def comboclick(event):
    if myCombo.get() == 'vendredi':
        myLabel = Label(root, text="C'est vendredi !").pack()
    else:
        myLabel = Label(root, text=myCombo.get()).pack()


options = [
    'lundi',
    'mardi',
    'mercredi',
    'jeudi',
    'vendredi',
    'samedi',
    'dimanche'
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind('<<ComboboxSelected>>', comboclick)  # remplace l'instruction command non applicable pour un Combobox
myCombo.pack()

root.mainloop()
