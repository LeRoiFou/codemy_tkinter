"""
Tkinter - Codemy.com #130 : How To Reset A Spinbox With Tkinter - Python Tkinter GUI Tutorial #130
Lien : https://www.youtube.com/watch?v=GjVZUIayxQg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=130

Dans ce programme on apprend à réinitialiser une valeur par défaut du widget spinbox (champ de saisi avec à l'extrêmité
une barre de défilement -> voir tuto n° 98)

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x350')


def reset():
    """Fonction permettant de réinitialiser la valeur par défaut du widget spinbox"""
    var = IntVar(root)
    var.set(0)
    my_spin.config(textvariable=var)


def reset2():
    """Fonction permettant de réinitialiser la valeur par défaut du widget spinbox"""
    var2 = StringVar(root)
    var2.set('Erin')
    my_spin2.config(textvariable=var2)


"""Variable de contrôle permettant d'afficher une valeur par défaut du spinbox : ici la valeur par défaut est 20"""
var = IntVar(root)
var.set(20)

"""Spinbox'"""
my_spin = Spinbox(root, from_=0, to=100, justify='center', font='Helvetica 20', textvariable=var)
my_spin.pack(pady=20)

"""Bouton"""
my_button = Button(root, text='Réinitialiser les données', command=reset)
my_button.pack(pady=20)

"""Deuxième variable de contrôle mais cette fois-ci avec une str utilisée pour le 2ème spinbox"""
var2 = StringVar(root)
var2.set('John')

"""Spinbox n° 2"""
my_spin2 = Spinbox(root, values=('John', 'Albert', 'Erin', 'Dean', 'Walter'),
                   justify='center', font='Helvetica 20', textvariable=var2)
my_spin2.pack(pady=20)

"""Bouton n° 2"""
my_button2 = Button(root, text='Réinitialiser les données', command=reset2)
my_button2.pack(pady=20)

root.mainloop()
