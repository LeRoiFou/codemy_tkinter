"""
Tkinter - Codemy.com #66 : Image Buttons And Rounded Buttons
Lien : https://www.youtube.com/watch?v=bVnKX0315lo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=66

Dans ce programme on créé un bouton à la forme d'une image et ne pas avoir la forme géométrique d'un bouton carré

ATTENTION  : pour les images, ne prendre en compte que les fichiers au format .png. Avec une image avec le format .jpg,
une erreur va s'afficher, il suffit donc de convertir le fichier au format .png.
PAR AILLEURS, ON NE PEUT PAS RECOURIR À LA POO AVEC CETTE INSTRUCTION... MONTRE LA LIMITE DE TKINTER

Éditeur : Laurent REYNAUD
Date : 08-12-20
"""

import tkinter

root = tkinter.Tk()
root.title('Mon titre !')
root.geometry('400x400')


def stuff():
    # fonction permettant d'afficher le texte ci-après après avoir cliqué sur le bouton

    my_label.config(text='Tu as cliqué sur le bouton...')


# chargement de l'image
login_btn = tkinter.PhotoImage(file='Images/Login.png')

# configuration d'un bouton à la forme d'une image et sans bordure
my_button = tkinter.Button(root, image=login_btn, borderwidth=0, command=stuff)
my_button.pack(pady=20)

# configuration d'une étiquette
my_label = tkinter.Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
