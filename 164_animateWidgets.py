"""
Tkinter - Codemy.com #164 : How To Animate Widgets - Python Tkinter GUI Tutorial #164
Lien : https://www.youtube.com/watch?v=kvd6i1mXec8

Dans ce programme on apprend à animer des widgets -> similaire à kivy dans le tuto 36_Animation.
Mais avec tkinter, animer des widgets est plus compliqué que sur kivy... question posé sur youtube : possibilité de
rajouter une deuxième commande pour un même widget ?

Éditeur : Laurent REYNAUD
Date : 27-01-21
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('700x600')

"""Assignation d'une variable pour : 
-> le nombre d'évènements  
-> la taille de police d'écriture"""
count = 0
size = 26
pos = 100


def contract():
    """Fonction permettant de rediminuer la police d'écriture du bouton : elle s'exécute après la fonction expand()"""

    global count, size, pos  # count = 9, size = 36, pos = 109

    if 10 >= count > 0:
        size -= 2  # tant que le nombre d'évènements <= 10 la taille d'écriture s'incrémente de -2
        my_button.config(font=('Helvetica', size))  # changement de la taille d'écriture du bouton
        my_button.pack_configure(pady=pos)  # changement de la position du bouton
        count -= 1  # incrémentation du nombre d'évènements de -1
        pos -= 20  # incrémentation de la position du widget de -20
        root.after(10, contract)  # changement de la fenêtre principale toute les milli-secondes


def expand():
    """Fonction permettant d'agrandir la police d'écriture du bouton"""

    global count, size, pos  # count = 0 , size = 26, pos = 100

    if count < 10:
        size += 2  # tant que le nombre d'évènements < 10 la taille d'écriture s'incrémente de +2
        my_button.config(font=('Helvetica', size))  # changement de la taille d'écriture du bouton
        my_button.pack_configure(pady=pos)  # changement de la position du bouton
        count += 1  # incrémentation du nombre d'évènements de +1
        pos += 20  # incrémentation de la position du widget de +20
        root.after(10, expand)  # changement de la fenêtre principale toute les milli-secondes

    elif count == 10:
        contract()


"""Création d'un bouton"""
my_button = Button(root, text='Clique-moi !', command=expand, font='Helvetica 24', fg='red')
my_button.pack(pady=100)

root.mainloop()
