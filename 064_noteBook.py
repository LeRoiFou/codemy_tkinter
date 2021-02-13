"""
Tkinter - Codemy.com #64 : Create tabs in your GUI interface using Notebook
Lien : https://www.youtube.com/watch?v=kqbkUKIc1Gk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=64

Ce widget Notebook permet d'avoir des onglets à la fenêtres qui sont situés en haut à l'inverse d'Excel et de Calc

Éditeur : Laurent REYNAUD
Date : 08-12-20
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Mon titre !')
root.geometry('500x500')

"""Configuration du notebook"""
my_notebook = ttk.Notebook(root)
my_notebook.pack()


def hide():
    """Permet de cacher l'onglet 2 situé à l'index 1"""
    my_notebook.hide(1)  # (1) -> index 1 qui est l'onglet n° 2 (l'onglet n° 1 est à l'index 0)


def show():
    """Permet de remontrer l'onglet 2 caché"""
    my_notebook.add(my_frame2, text='Onglet rouge')


def select():
    """Permet d'accéder à l'onglet n° 2 situé à l'index 1"""
    my_notebook.select(1)


"""Configuration des cadres"""
my_frame1 = Frame(my_notebook, width=500, height=500, bg='blue')
my_frame2 = Frame(my_notebook, width=500, height=500, bg='red')

"""Affichage des cadres sur toute la longueur et la largeur configurée ci-avant"""
my_frame1.pack(fill='both', expand=1)
my_frame2.pack(fill='both', expand=1)

"""Ajout des onglets"""
my_notebook.add(my_frame1, text='Onglet bleu')
my_notebook.add(my_frame2, text='Onglet rouge')

"""Configuration de boutons"""
my_button = Button(my_frame1, text="Cacher l'onglet n° 2", command=hide).pack(pady=15)
my_button2 = Button(my_frame1, text="Montrer l'onglet n° 2", command=show).pack(pady=15)
my_button3 = Button(my_frame1, text="Aller à l'onglet n° 2", command=select).pack(pady=15)

root.mainloop()
