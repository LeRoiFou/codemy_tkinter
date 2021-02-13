"""
Tkinter - Codemy.com #63 : Using .config() to Update Widgets
Lien : https://www.youtube.com/watch?v=tqKyMDqp-3E&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=63

Dans ce programme, on a recours à l'instruction config() pour mettre à jour les données des widgets

Éditeur : Laurent REYNAUD
Date : 07-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('400x400')


def truc():
    """Avec l'instruction config, le texte est automatiquement mis à jour, alors qu'avec l'instruction mise en
    commentaire ci-dessous (1ère ligne), le texte ne se met pas à jour"""
    # my_label = Label(root, text="C'est un nouveau texte !", font='Helvetica 10')
    my_label.config(text="C'est un nouveau texte !", font='Helvetica 8')  # mise à jour du texte et taille d'écriture
    root.config(bg='blue')  # mise à jour de la couleur de fond de la fenêtre
    my_button.config(text='Vous avez été configuré', state=DISABLED,
                     pady=30)  # mise à jour du texte du bouton désactivé et élargi


my_label = Label(root, text="C'est mon texte !", font='Helvetica 10')
my_label.pack(pady=10)

my_button = Button(root, text='Clique !', command=truc)
my_button.pack(pady=10)

root.mainloop()
