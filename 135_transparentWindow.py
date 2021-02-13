"""
Tkinter - Codemy.com #135 : Transparent Windows With TKinter - Python Tkinter GUI Tutorial #135
Lien : https://www.youtube.com/watch?v=qDVxLMuNs7E&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=135

Dans ce programme on apprend à rendre transparent une fenêtre. On ne peut que rendre transparent la fenêtre principale
et non les widgets individuellement

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')


def slide(*args):
    """Fonction permettant d'ajuster le d° de transparence de la fenêtre principale"""
    root.attributes('-alpha',
                    my_slider.get()  # niveau de transparence (niveau de 0 à 1 avec un d° de moins en moins élevé
                    )
    slide_label.config(text=round(my_slider.get(), 2))


def make_solid(e):
    """Fonction permettant d'annuler la transparence de la 2ème fenêtre"""
    new.attributes('-alpha',
                   1.0  # absence de transparence
                   )


def new_window():
    """Fonction permettant d'ouvrir une nouvelle fenêtre"""
    global new  # variable globale pour que celle-ci ne soit pas à redéfinir dans la fonction ci-avant
    new = Toplevel()
    new.attributes('-alpha',
                   0.5  # niveau de transparence (niveau de 0 à 1 avec un d° de moins en moins élevé
                   )
    new.bind('<Button-1>', make_solid)  # lorsqu'on clique sur cette nouvelle fenêtre, celle-ci n'est plus transparente


"""Etiquette titre"""
my_label = Label(root, text='Salut !', font='Helvetica 20')
my_label.pack(pady=20)

"""Curseur pour le d° de transparence de la fenêtre"""
my_slider = ttk.Scale(root, from_=0.1, to=1.0, value=0.7, orient=HORIZONTAL, command=slide)
my_slider.pack(pady=20)

"""Etiquette d'affichage du degré de transparence"""
slide_label = Label(root, text='')
slide_label.pack(pady=10)

"""Bouton pour ouvrir un nouvelle fenêtre"""
new_window = Button(root, text='Nouvelle fenêtre', command=new_window)
new_window.pack(pady=20)

root.mainloop()
