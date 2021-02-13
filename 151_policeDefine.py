"""
Tkinter - Codemy.com #151 : How To Define Custom Fonts - Python Tkinter GUI Tutorial #151
Lien : https://www.youtube.com/watch?v=JIqE3RMCMFE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=151

Dans ce programme on apprend à utiliser différents types de police d'écritures sur les widgets

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

from tkinter import *
from tkinter.font import Font

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')

"""Configuration de la police d'écriture pour le bouton"""
bigFont = Font(
    family='Times',
    size=42,
    weight='bold',  # normal : écriture régulière / bold : gras
    slant='roman',  # roman : écriture régulière / italic
    underline=0,  # écriture non soulignée
    overstrike=0  # écriture non barrée
)

"""Bouton """
my_button1 = Button(root, text='Grand texte', font=bigFont)
my_button1.pack(pady=20)

"""Configuration de la police d'écriture pour le message"""
mediumFont = Font(
    family='Helvetica',
    size=24,
    weight='normal',  # normal : écriture régulière / bold : gras
    slant='italic',  # roman : écriture régulière / italic
    underline=1,  # écriture soulignée
    overstrike=0  # écriture non barrée
)

"""Message"""
my_label = Label(root, text='Texte plus grand', font=mediumFont)
my_label.pack(pady=20)

root.mainloop()
