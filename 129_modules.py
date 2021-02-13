"""
Tkinter - Codemy.com #129 : Using Other Python Programs In Your Tkinter App - Python Tkinter GUI Tutorial #129
Lien : https://www.youtube.com/watch?v=KCWWL54He_g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=129

Dans ce programme on apprend à créer des modules personnalisées pour alléger le programme établi sur un seul fichier

Peut-on faire pareil avec la POO ? avec une fenêtre tkinter distincte d'une autre fenêtre ?

Dans le fichier essai1, ci-dessous le programme saisi :
def nameit(name):
    greetings = f"Salut {name} !"
    return greetings

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *
import main  # import du module personnalisé

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x350')


def submit():
    """Fonction appelant la fonction du fichier essay1, qui complète la phrase avec le texte rédigé dans le champ de
    saisi"""
    # greet = nameit(my_box.get())  # assignation de la phrase à afficher avec la fonction nameit()
    # my_label.config(text=greet)  # configuration du message à afficher


"""Champ de saisi"""
my_box = Entry(root, justify='center')
my_box.pack(pady=20)

"""Affichage du message"""
my_label = Label(root, text='', font='Helvetica 18')
my_label.pack(pady=20)

"""Bouton"""
my_button = Button(root, text='Afficher nom', command=submit)
my_button.pack(pady=20)

root.mainloop()
