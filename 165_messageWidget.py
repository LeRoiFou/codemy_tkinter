"""
Tkinter - Codemy.com #165 : How To Use The Message Widget For Blocks of Text - Python Tkinter GUI Tutorial #165
Lien : https://www.youtube.com/watch?v=frNj1E-MA14

Dans ce programme on apprend à utiliser le widget Message qui permet de faire de la saisie sur plusieurs lignes sans
recourir à l'instruction '\n' qu'on utilise avec le widget Label

Pour une seule ligne -> Label // Entry
Pour plusieurs lignes -> Message // Text

Éditeur : Laurent REYNAUD
Date : 03-02-21
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('400x900')


def change():
    """Fonction permettant de changer le texte"""
    my_message1.config(text='Et maintenant le texte a été complètement modifié !',
                       aspect=200  # changement de la largeur du widget
                       )


"""Premier cadre"""
frame1 = LabelFrame(root, text='Justifié à droite')
frame1.pack(pady=20)

my_message1 = Message(frame1, text="C'est un long texte parce que je veux regarder ce que j'écris, ce n'est pas cool ?",
                      font='helvetica 18',
                      aspect=150,  # largeur du widget
                      justify=RIGHT  # alignement du texte
                      )
my_message1.pack(pady=10, padx=10)

"""Deuxième cadre"""
frame2 = LabelFrame(root, text='Justifié à gauche')
frame2.pack(pady=20)

my_message2 = Message(frame2, text="C'est un long texte parce que je veux regarder ce que j'écris, ce n'est pas cool ?",
                      font='helvetica 18',
                      aspect=100,  # largeur du widget
                      justify=LEFT  # alignement du texte
                      )
my_message2.pack(pady=10, padx=10)

"""Troisième cadre"""
frame3 = LabelFrame(root, text='Centré')
frame3.pack(pady=20)

my_message3 = Message(frame3, text="C'est un long texte parce que je veux regarder ce que j'écris, ce n'est pas cool ?",
                      font='helvetica 18',
                      aspect=200,  # largeur du widget
                      justify=CENTER  # alignement du texte
                      )
my_message3.pack(pady=10, padx=10)

"""Bouton"""
my_button = Button(root, text='Changer le text', command=change)
my_button.pack(pady=20)

root.mainloop()
