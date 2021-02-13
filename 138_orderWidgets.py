"""
Tkinter - Codemy.com #138 : How To Set Tab Order And Focus - Python Tkinter GUI Tutorial #138
Lien : https://www.youtube.com/watch?v=A5Tbh_8nscA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=138

Dans ce programme on apprend à choisir l'ordre des champs de saisis avec le bouton TAB.
À titre d'exemple avec 3 champs de saisis un en haut appelé Entry1, un au milieu appelé Entry2 et un en bas appelé
Entry3, par principe en appuyant la touche TAB et si on sélectionne en premier Entry1 on passe à Entry2 puis Entry3.
Or il y possibilité par exemple de passer d'Entry1 à Entry3 puis Entry2

1ère solution pour changer l'ordre : l'ordre d'initialisation des widgets n'est pas le même que celui de l'affichage
2ème solution pour changer l'ordre : créer une fonction avec l'instruction lift()

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')

"""Initialisation des champs de saisis : blanc / rouge / bleu"""
white = Entry(root, bg='white', font='Helvetica 20')
red = Entry(root, bg='red', font='Helvetica 20')
blue = Entry(root, bg='blue', font='Helvetica 20')

"""Affichage des champs de saisis: rouge / blanc / bleu"""
red.pack(pady=20)
white.pack(pady=20)
blue.pack(pady=20)

"""Choix préférentiel du champ de saisis : le 3ème champ de saisi de couleur bleu"""
blue.focus()


def tab_order():
    """Fonction permettant de désigner l'ordre de tabulation : bleu puis blanc puis rouge"""
    widgets = [blue, white, red]
    for w in widgets:
        w.lift()


"""Bouton permettant de changer l'ordre de tabulation"""
my_button = Button(root, text="Changer l'ordre de tabulation", command=tab_order)
my_button.pack(pady=20)

root.mainloop()
