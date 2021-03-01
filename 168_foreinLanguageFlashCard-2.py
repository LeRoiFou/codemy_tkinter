"""
Tkinter - Codemy.com #168 : Build A Foreign Language Flashcard App - Python Tkinter GUI Tutorial #168
Lien : https://www.youtube.com/watch?v=Pd3XoLSQ5wg

Dans ce programme on apprend à afficher un mot en français et à le traduire en anglais.
Pour cela, un mot en français s'affiche, l'utilisateur saisi le mot en anglais et il a 3 boutons :
. 'Réponse' pour afficher si le mot traduit est correct
. 'Suivant' pour afficher un nouveau mot à traduire
. 'Indice' : à chaque fois qu'on appuye sur le bouton, lettre par lettre le mot à traduire en anglais s'affiche

Cette fois-ci on a recours à la POO, ce qui permet d'éviter les variables globales qui mènent à une 'confusion' dans la
déclaration des variables, et rend un programme 'plus propre'

Éditeur : Laurent REYNAUD
Date : 26-02-21
"""

from tkinter import *
from random import randint

root = Tk()
root.title('Build A Foreign Language Flashcard App')
root.geometry('550x410')


class MyProject(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.widgets()

    def next(self):
        """Fonction pour le bouton 'Suivant' permettant d'afficher au hasard un mot en français"""

        """Réinitialisation des données"""
        self.answer_label.config(text='')  # réinitialisation de la réponse attendue
        self.my_entry.delete(0, END)  # réinitialisation du champ de saisie
        self.hint_label.config(text='')  # réinitialisation de l'indice du mot en anglais
        self.hinter = ''  # réinitialisation de la str de lettres
        self.hint_count = 0  # réinitialisation du compteur de lettres

        """Assignation d'un nombre compris entre 0 et le nbre total de composants dans la liste 'words' - 1 soit 11"""
        self.random_word = randint(0, self.count - 1)

        """Mise à jour du mot affiché en français : prendre au hasard un indice compris entre 0 et 11 et prendre le 
        mot à l'indice 0 du tuple de cet indice """
        self.french_word.config(text=self.words[self.random_word][0])

    def answer(self, *args):
        """Fonction pour le bouton 'Réponse' comparant le mot français affiché et le mot anglais saisi"""

        """Si le mot saisi est le mot affiché au hasard et correspondant au mot anglais..."""
        if self.my_entry.get().capitalize() == self.words[self.random_word][1]:
            self.answer_label.config(
                text=f"Correct ! {self.words[self.random_word][0]} est {self.words[self.random_word][1]}")
        else:
            self.answer_label.config(text=f"Faux ! {self.words[self.random_word][0]} n'est pas "
                                          f"{self.my_entry.get().capitalize()}")

    def hint(self):
        """Fonction donnant un indice du mot français affiché à traduire en anglais en affichant lettre par lettre à
        chaque fois qu'on appuye sur le bouton 'indice' """

        """Si le nombre de lettres est inférieur au nombre total de lettres attendues en anglais..."""
        if self.hint_count < len(self.words[self.random_word][1]):
            self.hinter = self.hinter + self.words[self.random_word][1][self.hint_count]  # incrémentation de la str de
            # lettres du mot en anglais
            self.hint_label.config(text=self.hinter)  # affichage lettre par lettre du mot en anglais
            self.hint_count += 1  # incrémentation du nombre de lettres

    def widgets(self):
        """Déclaration des variables & widgets"""

        """Assignation d'une liste de tuples des mots à convertir en anglais"""
        self.words = [
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
        self.hinter = ""  # str de lettres
        self.hint_count = 0  # compteur de lettres
        self.count = len(self.words)  # Nombre total de composants dans la liste 'words' = 12

        """Configuration des widgets"""
        self.french_word = Label(root, text='', font='Helvetica 36')  # mot en français à traduire
        self.french_word.pack(pady=50)

        self.answer_label = Label(root, text='')  # mot en anglais attendu
        self.answer_label.pack(pady=20)

        self.my_entry = Entry(root, font='Helvetica 18')  # champ de saisi du mot français en anglais
        self.my_entry.pack(pady=20)

        button_frame = Frame(root)  # cadre pour les boutons
        button_frame.pack(pady=20)

        answer_button = Button(button_frame, text='Réponse', command=self.answer)  # bouton pour donner la réponse
        answer_button.grid(row=0, column=0, padx=20)

        next_button = Button(button_frame, text='Suivant', command=self.next)  # bouton pour afficher un nouveau mot
        next_button.grid(row=0, column=1, padx=20)

        hint_button = Button(button_frame, text='Indice',
                             command=self.hint)  # bouton pour afficher lettre par lettre le mot en RU
        hint_button.grid(row=0, column=2, padx=20)

        self.hint_label = Label(root, text='')  # affichage lettre par lettre du mot en anglais
        self.hint_label.pack(pady=20)


my_project = MyProject(root)  # instanciation de la classe
my_project.next()  # appel de la fonction next() de la classe MyProject()
root.mainloop()
