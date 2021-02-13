"""
Tkinter - Codemy.com #12 : radio buttons
Lien : https://www.youtube.com/watch?v=uqJZWLlnSqs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=12

Ce programme permet d'afficher une liste d'option (ici le choix de pizzas)

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *

root = Tk()
root.title('Apprendre à coder avec Codemy.com')

"""Assignation d'une liste de tuples"""
MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Fromage', 'Fromage'),
    ('Champignon', 'Champignon'),
    ('Oignon', 'Oignon'),
]

"""Variable de contrôles"""
pizza = StringVar()
pizza.set('Pepporoni')  # cette instruction permet de décocher toutes les options affichées

"""Affichage des options"""
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    """Fonction permettant d'afficher l'option choisie"""
    myLabel = Label(root, text=value)
    myLabel.pack()


"""Bouton d'exécution permettant d'afficher l'option choisie"""
myButton = Button(root, text='Clique !', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
