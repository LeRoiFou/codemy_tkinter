"""
Tkinter - Codemy.com #101 : Add Images to Text Box Widgets
Lien : https://www.youtube.com/watch?v=bdKxTH7Y-38&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=101

Dans ce programme on apprend à ajouter une image dans le text box et à mettre une barre de défilement

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

from tkinter import *
from tkinter import filedialog

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x600')


def open_text():
    """Fonction permettant de récupérer un fichier texte et de l'afficher dans le widget textbox"""
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Ouvrir un fichier texte',
                                           filetypes=(('Fichiers .txt', '*.txt'),))  # voir tuto n° 15_DialogBox.py
    text_file = open(text_file, 'r')  # ouverture du fichier, lecture du fichier
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def save_txt():
    """Fonction permettant de sauvegarder les modifications faites dans le widget textbox dans le fichier ouvert"""
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Enregistrer sous',
                                           filetypes=(('Fichiers .txt', '*.txt'),))
    text_file = open(text_file, 'w')  # ouverture du fichier, écriture du fichier
    text_file.write(my_text.get(1.0, END))


def add_image():
    """Ajout d'une image dans le text box"""
    global my_image
    my_image = PhotoImage(file='images/shrek.png')  # chargement de l'image
    position = my_text.index(INSERT)  # insertion à la position du curseur de la souris
    my_text.image_create(position, image=my_image)  # insertion de l'image dans le widget textbox


"""Création d'un cadre pour le textbox et la barre de défilement"""
my_frame = Frame(root)
my_frame.pack(pady=10)

"""Création d'une barre de défilement pour le texbox"""
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

"""Configuration de la boîte à texte"""
my_text = Text(my_frame, width=40, height=10, font='helvetica 16',
               selectbackground='red',  # surbrillance en rouge du texte sélectionné
               selectforeground='black',  # écriture en noir du texte en surbrillance de couleur rouge
               yscrollcommand=text_scroll.set  # liaison avec la barre de défilement
               )
my_text.pack(pady=20)

"""Configuration de la barre de défilement"""
text_scroll.config(command=my_text.yview)

"""Configuration du bouton d'exécution permettant d'ouvrir un fichier texte"""
open_button = Button(root, text='Ouvrir un fichier texte', command=open_text)
open_button.pack(pady=20)

"""Configuration du bouton de sauvegarde des données saisies dans le widget text box"""
save_button = Button(root, text='Sauvegarder', command=save_txt)
save_button.pack(pady=20)

"""Configuration du bouton d'exécution pour insérer une image dans le text box"""
image_button = Button(root, text='Ajouter une image', command=add_image)
image_button.pack(pady=5)

root.mainloop()
