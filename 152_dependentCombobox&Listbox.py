"""
Tkinter - Codemy.com #152 : Dependent Drop Downs and List Boxes - Python Tkinter GUI Tutorial #152
Lien : https://www.youtube.com/watch?v=bH9r3wM9Idw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=152

Dans ce programme on apprend à rendre dépendant :
-> Un deuxième menu déroulant (dropdown) par rapport au premier menu déroulant
-> Une deuxième zone de liste (listbox) par rapport à la première zone de liste

Exemple :
Dans le 1er menu déroulant figure les départements d'une région
Dans le 2ème menu déroulant figure les communes du département sélectionné dans le 1er menu déroulant

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x400')


def pick_color(e):
    """Fonction pour les menus déroulants permettant d'afficher les différentes couleurs selon la taille choisie"""
    if my_combo.get() == 'Petit':
        color_combo.config(value=small_colors)
        color_combo.current(0)
    elif my_combo.get() == 'Moyen':
        color_combo.config(value=medium_colors)
        color_combo.current(0)
    elif my_combo.get() == 'Grand':
        color_combo.config(value=large_colors)
        color_combo.current(0)


def list_color(e):
    """Fonction pour les zones de listes permettant d'afficher les différentes couleurs selon la taille choisie"""
    my_list2.delete(0, END)  # réinitialisation des données
    if my_list1.get(ANCHOR) == 'Petit':
        for item in small_colors:
            my_list2.insert(END, item)
    elif my_list1.get(ANCHOR) == 'Moyen':
        for item in medium_colors:
            my_list2.insert(END, item)
    elif my_list1.get(ANCHOR) == 'Grand':
        for item in large_colors:
            my_list2.insert(END, item)


"""Assignation d'un liste de tailles"""
sizes = ['Petit', 'Moyen', 'Grand']

"""Assignation d'une liste de couleurs"""
small_colors = ['Rouge', 'Vert', 'Bleu', 'Noir']
medium_colors = ['Rouge', 'Vert']
large_colors = ['Bleu', 'Noir']

"""Configuration de la liste déroulante pour les différentes tailles"""
my_combo = ttk.Combobox(root, value=sizes)
my_combo.current(0)  # valeur par défaut en affichage : 'Petit'
my_combo.pack(pady=20)

"""Liaison du menu déroulant des différentes tailles avec le menu déroulant des différentes couleurs"""
my_combo.bind('<<ComboboxSelected>>', pick_color)

"""Configuration de la liste déroulante pour les différentes couleurs"""
color_combo = ttk.Combobox(root, value=[' '])
color_combo.pack(pady=20)

"""Cadre pour les zones de liste"""
my_frame = Frame(root)
my_frame.pack(pady=50)

"""Configuration des zones de liste"""
my_list1 = Listbox(my_frame)
my_list1.grid(row=0, column=0)
my_list2 = Listbox(my_frame)
my_list2.grid(row=0, column=1, padx=20)

"""Ajout des éléments à la zone de liste 1"""
for item in sizes:
    my_list1.insert(END, item)

"""Liaison de la 1ère zone de liste avec la 2ème zone de liste"""
my_list1.bind('<<ListboxSelect>>', list_color)

root.mainloop()
