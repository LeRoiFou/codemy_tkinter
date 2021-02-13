"""
Tkinter - Codemy.com #116 : Treeview
Lien : https://www.youtube.com/watch?v=YTqDYmfccQU&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=116

Dans ce programme on apprend à crééer une arborescence

Deuxième présentation de l'arborescence en masquant la 1ère colonne 'Etiquette' qui s'affiche automatiquement dans
ce widget

Éditeur : Laurent REYNAUD
Date : 21-12-20
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')

"""Configuration de l'arborescence"""
my_tree = ttk.Treeview(root)

"""Configuration des colonnes"""
my_tree['columns'] = ('Name', 'ID', 'Favorite pizza')

"""Formatage des colonnes"""
my_tree.column('#0', width=0, stretch=NO)  # colonne fantôme
my_tree.column('Name', anchor=W, width=120)
my_tree.column('ID', anchor=CENTER, width=80)
my_tree.column('Favorite pizza', anchor=W, width=120)

"""Configuration des en-têtes"""
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Name', text='Nom', anchor=W)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('Favorite pizza', text='Pizza préférée', anchor=W)

"""Ajout des données dans les colonnes"""
my_tree.insert(parent='', index='end', iid=0, text='', values=('John', 1, 'Calzone'))
my_tree.insert(parent='', index='end', iid=1, text='', values=('Albert', 2, 'Fromages'))
my_tree.insert(parent='', index='end', iid=2, text='', values=('Marius', 3, 'Champignons'))
my_tree.insert(parent='', index='end', iid=3, text='', values=('Bob', 4, 'Anchois'))
my_tree.insert(parent='', index='end', iid=4, text='', values=('Clint', 5, 'Fruits de mer'))
my_tree.insert(parent='', index='end', iid=5, text='', values=('Erin', 6, 'Ananas'))
# """Ajout d'un enfant"""
# my_tree.insert(parent='', index='end', iid=6, text='Enfant', values=('Steve', '1.1', 'Poivrons'))
# my_tree.move('6', '0', '0')  # position idd initiale, position idd souhaitée, sous-position idd souhaitée

"""Affichage des données"""
my_tree.pack(pady=20)

root.mainloop()
