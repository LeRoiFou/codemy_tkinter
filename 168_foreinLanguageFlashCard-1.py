"""
Tkinter - Codemy.com #168 : Build A Foreign Language Flashcard App - Python Tkinter GUI Tutorial #168
Lien : https://www.youtube.com/watch?v=Pd3XoLSQ5wg

Dans ce programme on apprend à afficher un mot en français et à le traduire en anglais.
Pour cela, un mot en français s'affiche, l'utilisateur saisi le mot en anglais et il a 3 boutons :
. 'Réponse' pour afficher si le mot traduit est correct
. 'Suivant' pour afficher un nouveau mot à traduire
. 'Indice' : à chaque fois qu'on appuye sur le bouton, lettre par lettre le mot à traduire en anglais s'affiche

Éditeur : Laurent REYNAUD
Date : 26-02-21
"""

from tkinter import *
from random import randint

root = Tk()
root.title('Build A Foreign Language Flashcard App')
root.geometry('550x410')

"""Assignation d'une liste de tuples des mots à convertir en anglais"""
words = [
    (("Salut"), ("Hello")),
    (("Au revoir"), ("Goodbye")),
    (("S'il te plaît"), ("Please")),
    (("Merci"), ("Thank you")),
    (("Désolé"), ("Sorry")),
    (("Soit béni"), ("Bless you")),
    (("Oui"), ("Yes")),
    (("Non"), ("No")),
    (("Qui"), ("Who")),
    (("Quoi"), ("What")),
    (("Pourquoi"), ("Why")),
    (("Où"), ("Where"))
]

"""Assignation de variables"""
hinter = ""  # str de lettres
hint_count = 0  # compteur de lettres
count = len(words)  # Nombre total de composants dans la liste 'words' = 12


def next():
    """Fonction pour le bouton 'Suivant' permettant d'afficher au hasard un mot en français"""

    """Etant donné que nous ne recourons pas à la POO, la variable 'random_word' utilisé dans cette fonction est
    également requise dans d'autres fonctions, celle-ci doit donc être une variable globale. Il en est de même pour les
    variables hinter et hint_count"""
    global random_word, hinter, hint_count

    """Réinitialisation des données"""
    answer_label.config(text='')  # réinitialisation de la réponse attendue
    my_entry.delete(0, END)  # réinitialisation du champ de saisie
    hint_label.config(text='')  # réinitialisation de l'indice du mot en anglais
    hinter = ''  # réinitialisation de la str de lettres
    hint_count = 0  # réinitialisation du compteur de lettres

    """Assignation d'un nombre compris entre 0 et le nbre total de composants dans la liste 'words' - 1 soit 11"""
    random_word = randint(0, count-1)

    """Mise à jour du mot affiché en français : prendre au hasard un indice compris entre 0 et 11 et prendre le mot à
    l'indice 0 du tuple de cet indice"""
    french_word.config(text=words[random_word][0])


def answer(*args):
    """Fonction pour le bouton 'Réponse' comparant le mot français affiché et le mot anglais saisi"""

    """Si le mot saisi est le mot affiché au hasard et correspondant au mot anglais..."""
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct ! {words[random_word][0]} est {words[random_word][1]}")
    else:
        answer_label.config(text=f"Faux ! {words[random_word][0]} n'est pas {my_entry.get().capitalize()}")


def hint():
    """Fonction donnant un indice du mot français affiché à traduire en anglais en affichant lettre par lettre à chaque
     fois qu'on appuye sur le bouton 'indice'"""

    """Etant donné que nous ne recourons pas à la POO, les variables 'hinter' et 'hint_count' se trouvent en dehors de
    la fonction hint() car si ces variables sont à l'intérieur de cette fonction, seule la 1ère lettre du mot en anglais
    sera affichée"""
    global hinter, hint_count

    """Si le nombre de lettres est inférieur au nombre total de lettres attendues en anglais..."""
    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]  # incrémentation de la str de lettres du mot en anglais
        hint_label.config(text=hinter)  # affichage lettre par lettre du mot en anglais
        hint_count += 1  # incrémentation du nombre de lettres


"""Configuration des widgets"""
french_word = Label(root, text='', font='Helvetica 36')  # mot en français à traduire
french_word.pack(pady=50)

answer_label = Label(root, text='')  # mot en anglais attendu
answer_label.pack(pady=20)

my_entry = Entry(root, font='Helvetica 18')  # champ de saisi du mot français en anglais
my_entry.pack(pady=20)

button_frame = Frame(root)  # cadre pour les boutons
button_frame.pack(pady=20)

answer_button = Button(button_frame, text='Réponse', command=answer)  # bouton pour donner la réponse
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text='Suivant', command=next)  # bouton pour afficher un nouveau mot
next_button.grid(row=0, column=1, padx=20)

hint_button = Button(button_frame, text='Indice', command=hint)  # bouton pour afficher lettre par lettre le mot en RU
hint_button.grid(row=0, column=2, padx=20)

hint_label = Label(root, text='')  # affichage lettre par lettre du mot en anglais
hint_label.pack(pady=20)

"""Appel des fonctions sur les boutons"""
next()

root.mainloop()
