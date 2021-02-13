"""
Tkinter - Codemy.com #147 : How To Use Images as Backgrounds - Python Tkinter GUI Tutorial #147
Lien : https://www.youtube.com/watch?v=WurCpmHtQc4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=147

Dans ce programme on apprend à mettre une image en fond de fenêtre

Pour le positionnement des widgets, il existe trois méthodes : pack, grid et place
pack et grid ne peuvent pas être utilisés simultanément pour un même cadre.
Par contre, place peut être utilisé simultanément avec pack ou grid pour un même cadre

1ère méthode :
Récupération du fichier dans l'application Paint 3D puis avec le 'compte-goutte' récupérer la couleur du bleu ciel de
l'image pour obtenir le code hexadécimal du fond de couleur du titre en haut de l'image et du cadre pour les boutons.
Code couleur hexadécimal récupéré du bleu ciel de l'image : #6b88fe

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('800x500')

"""Chargement de l'image"""
bg = PhotoImage(file='images/mario.png')

"""Affichage de l'image dans la fenêtre"""
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)  # relwidth/relheight -> l'image accrochée au centre de la fenêtre

"""Ajout d'un titre en haut de l'image"""
my_text = Label(root, text='Bienvenue !', font='Helvetica 50', fg='white', bg='#6b88fe')
my_text.pack(pady=50)

"""Ajout d'un cadre"""
my_frame = Frame(root, bg='#6b88fe')
my_frame.pack(pady=20)

"""Ajout de boutons"""
my_button1 = Button(my_frame, text='Sortie')
my_button1.grid(row=0, column=0, padx=10)
my_button2 = Button(my_frame, text='Commencer')
my_button2.grid(row=0, column=1, padx=10)
my_button3 = Button(my_frame, text='Effacer')
my_button3.grid(row=0, column=2, padx=10)

root.mainloop()
