"""
Tkinter - Codemy.com #80 : How To Resize A Window Dynamically 
Lien : https://www.youtube.com/watch?v=NytF3pJSMc8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=80 

Dans ce programme on apprend à redimensionner une fenêtre de manière dynamique 

Éditeur : Laurent REYNAUD 
Date : 11-12-20 
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('800x800')


def resize():
    """Fonction permettant de redimensionner la fenêtre"""
    w = width_entry.get()
    h = height_entry.get()
    root.geometry(f'{w}x{h}')


"""Configuration étiquette et champ de saisie pour saisir la largeur de la fenêtre"""
width_label = Label(root, text='Largeur : ')
width_label.pack(pady=20)
width_entry = Entry(root, justify='center')
width_entry.pack()

"""Configuration étiquette et champ de saisie pour saisir la hauteur de la fenêtre"""
height_label = Label(root, text='Hauteur : ')
height_label.pack(pady=20)
height_entry = Entry(root, justify='center')
height_entry.pack()

"""Configution du bouton d'exécution"""
my_button = Button(root, text='Redimensionner', command=resize)
my_button.pack(pady=20)

root.mainloop()
