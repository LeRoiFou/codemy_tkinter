"""
Tkinter - Codemy.com #168 : 
Build A Foreign Language Flashcard App - Python Tkinter GUI Tutorial #168
Lien : https://www.youtube.com/watch?v=Pd3XoLSQ5wg

Dans ce programme on apprend à afficher un mot en français 
et à le traduire en anglais.
Pour cela, un mot en français s'affiche, 
l'utilisateur saisi le mot en anglais et il a 3 boutons :
. 'Réponse' pour afficher si le mot traduit est correct
. 'Suivant' pour afficher un nouveau mot à traduire
. 'Indice' : à chaque fois qu'on appuye sur le bouton, 
lettre par lettre le mot à traduire en anglais s'affiche

Éditeur : Laurent REYNAUD
Date : 26-02-21
"""

import tkinter
from random import randint

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.title('Build A Foreign Language Flashcard App')
        root.geometry('550x410')
        
        # Assignation des variables
        self.my_variables()
        # Configuration des widgets
        self.widgets()
        # Appel de la méthode suivante
        self.next()
        
    def my_variables(self):
        "Assignation des variables"
        
        """Assignation d'une liste de tuples des mots
        à convertir en anglais"""
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
        
        # str de lettres
        self.hinter = ""
        
        # compteur de lettres  
        self.hint_count = 0  
        
        # Nombre total de composants dans la liste 'self.words' = 12
        self.count = len(self.words)  
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration des widgets"""
        
        # mot en français à traduire
        self.french_word = tkinter.Label(
            root, 
            text='', 
            font='Helvetica 36')  
        self.french_word.pack(pady=50)

        # mot en anglais attendu
        self.answer_label = tkinter.Label(root, text='')  
        self.answer_label.pack(pady=20)

        # champ de saisi du mot français en anglais
        self.my_entry = tkinter.Entry(root, font='Helvetica 18')  
        self.my_entry.pack(pady=20)

        # cadre pour les boutons
        button_frame = tkinter.Frame(root)  
        button_frame.pack(pady=20)

        # bouton pour donner la réponse
        answer_button = tkinter.Button(
            button_frame, 
            text='Réponse', 
            command=self.answer)  
        answer_button.grid(row=0, column=0, padx=20)

        # bouton pour afficher un nouveau mot
        next_button = tkinter.Button(
            button_frame, 
            text='Suivant', 
            command=self.next)  
        next_button.grid(row=0, column=1, padx=20)

        # bouton pour afficher lettre par lettre le mot en RU
        hint_button = tkinter.Button(
            button_frame, 
            text='Indice', 
            command=self.hint)  
        hint_button.grid(row=0, column=2, padx=20)

        # affichage lettre par lettre du mot en anglais
        self.hint_label = tkinter.Label(root, text='')  
        self.hint_label.pack(pady=20)
        
    def next(self):
        """Méthode pour le bouton 'Suivant' permettant d'afficher 
        au hasard un mot en français"""

        """Réinitialisation des données"""
        
        # réinitialisation de la réponse attendue
        self.answer_label.config(text='')  
        
        # réinitialisation du champ de saisie
        self.my_entry.delete(0, 'end')  
        
        # réinitialisation de l'indice du mot en anglais
        self.hint_label.config(text='')  
        
        # réinitialisation de la str de lettres
        self.hinter = ''  
        
        # réinitialisation du compteur de lettres
        self.hint_count = 0  

        """Assignation d'un nombre compris entre 0 et le nbre total
        de composants dans la liste 'self.words' - 1 soit 11"""
        self.random_word = randint(0, self.count-1)

        """Mise à jour du mot affiché en français : 
        prendre au hasard un indice compris entre 0 et 11 
        et prendre le mot à l'indice 0 du tuple de cet indice"""
        self.french_word.config(text=self.words[self.random_word][0])

    def answer(self, *args):
        """Méthode pour le bouton 'Réponse' comparant 
        le mot français affiché et le mot anglais saisi"""

        """Si le mot saisi est le mot affiché au hasard 
        et correspondant au mot anglais..."""
        if (self.my_entry.get().capitalize() == 
            self.words[self.random_word][1]):
            
            self.answer_label.config(
                text=(f"Correct ! {self.words[self.random_word][0]} \
est {self.words[self.random_word][1]}"))
            
        else:
            self.answer_label.config(
                text=(f"Faux ! {self.words[self.random_word][0]} \
n'est pas {self.my_entry.get().capitalize()}"))

    def hint(self):
        """Méthode donnant un indice du mot français affiché à traduire 
        en anglais en affichant lettre par lettre à chaque
        fois qu'on appuye sur le bouton 'indice'"""

        """Si le nombre de lettres est inférieur au nombre total de lettres
        attendues en anglais..."""
        if self.hint_count < len(self.words[self.random_word][1]):
            
            # incrémentation de la str de lettres du mot en anglais
            self.hinter = (self.hinter + 
                           self.words[self.random_word][1][self.hint_count])  
            
            # affichage lettre par lettre du mot en anglais
            self.hint_label.config(text=self.hinter)  
            
            # incrémentation du nombre de lettres
            self.hint_count += 1  


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
