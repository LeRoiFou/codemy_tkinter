"""
Tkinter - Codemy.com #98 : Spinboxes With TKinter
Lien : https://www.youtube.com/watch?v=FfYDWBdX-_s&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=98

Dans ce programme on créé un nouveau widget qui dispose d'un champ de saisie d'une ligne avec au bout de cette ligne,
des flêches haut et bas

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x400')


def grab():
    """Fonction permettant d'afficher le nom apparaissant dans le spinbox n° 2"""
    my_label.config(text=my_spin2.get())


"""Création d'un spinbox : l'instruction 'from_' dispose d'un '_' pour ne pas être confondu avec le 'from' dont on a un 
exemple ci-dessus : 'from tkinter import *'"""
my_spin = Spinbox(root,
                  from_=0,  # départ de 0
                  to=10,  # arrivée à 10
                  increment=2,  # incrémentation de 2
                  justify='center',
                  font='Helvetica 20')
my_spin.pack(pady=20)

"""Création d'un 2ème spinbox"""
names = ('John', 'Albert', 'Machin')  # déclaration d'une variable en tuple
my_spin2 = Spinbox(root,
                   values=names,  # Affichage du tuple
                   justify='center',
                   font='Helvetica 20')
my_spin2.pack(pady=20)

"""Configuration d'un bouton d'exécution"""
my_button = Button(root, text='Soumettre', command=grab)  # grab = saisir
my_button.pack(pady=20)

"""Affichage du nom figurant dans le spinbox n° 2 : configuration de l'étiquette dans la fonction grab()"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
