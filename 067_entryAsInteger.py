"""
Tkinter - Codemy.com #67 : How to Validate an Entry Widget as an Integer
Lien : https://www.youtube.com/watch?v=IbpInH4q4Sg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=67

Programme permettant de convertir une chaîne de caractères en un entier à partir du champ de saisie

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('400x400')


def number():
    """Fonction permettant de valider ou non si la saisie dans l'entry est un entier ou non"""
    try:
        int(my_box.get())
        answer.config(text="C'est un chiffre ! Félicitations !")

    except ValueError:
        answer.config(text="Ce n'est pas un chiffre ! hoooooooooouuuuuuuu !!!!!!")


"""Configuration étiquette titre"""
my_label = Label(root, text='Entrez un chiffre')
my_label.pack(pady=20)

"""Configuration champ de saisie"""
my_box = Entry(root)
my_box.pack(pady=10)

"""Configuration bouton à actionner"""
my_button = Button(root, text='Entre un chiffre', command=number)
my_button.pack(pady=5)

"""Configuration étiquette résultat"""
answer = Label(root, text='')
answer.pack(pady=20)

root.mainloop()
