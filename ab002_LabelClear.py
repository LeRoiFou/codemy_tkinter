""""
Les bases de tkinter

Dans ce programme on apprend à effacer les données affichées avec le widget Label et avec l'instruction grid_forget()

Éditeur : Laurent REYNAUD
Date : 06-01-2021
"""

from tkinter import *

"""Configuration de la fenêtre principale"""
root = Tk()
root.title('Titre !')
root.geometry('400x400')


def submit():
    my_label.config(text=f"Salut {my_entry.get()} !")


def clear():
    my_label.grid_forget()


title = Label(root, text='Entrez votre nom')
title.grid(row=0, column=0, columnspan=2, pady=5, padx=10)

my_entry = Entry(root, justify='center', width=30)
my_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=10)

my_button1 = Button(root, text='Afficher', command=submit)
my_button1.grid(row=2, column=0, pady=5, padx=10)

my_button2 = Button(root, text='Effacer', command=clear)
my_button2.grid(row=2, column=1, pady=5, padx=10)

my_label = Label(root, text='')
my_label.grid(row=3, column=0, columnspan=2, pady=5, padx=10)

root.mainloop()
