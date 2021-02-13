"""
Tkinter - Codemy.com #157 : Color Changing Number Guessing Game - Python Tkinter GUI Tutorial #157
Lien : https://www.youtube.com/watch?v=6Bky5KsM2mg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=157

Dans ce programme on créé un jeu de devinette sur un nombre à choisir entre 1 et 10 : plus on est proche du chiffre à
obtenir et plus la couleur de fenêtre passe du bleu (froid) au rouge (chaud)

Éditeur : Laurent REYNAUD
Date : 29-12-20
"""

from tkinter import *
from random import randint

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')

"""Titre de la fenêtre"""
num_label = Label(root, text='Choisis un chiffre\nentre 1 et 10', font=('Brush Script MT', 32))
num_label.pack(pady=20)


def guesser():
    """Fonction permettant de recouper entre le chiffre saisi et le chiffre attendu"""

    if guess_box.get().isdigit():
        """Si le champ de saisi a un chiffre... 

        Message à afficher"""
        num_label.config(text="Choisis un chiffre\nentre 1 et 10")

        """Assignation de l'écart entre le chiffre saisi et le chiffre attendu en nombre absolu (pas de négatif)"""
        dif = abs(num - int(guess_box.get()))

        """Recoupement du chiffre saisi avec le chiffre attendu"""
        if int(guess_box.get()) == num:

            """Assignation de l'erreur affichée dès que le chiffre saisi est égal au chiffre attendu : mise en place 
            de la couleur par défaut"""
            bc = 'SystemButtonFace'

            """Si le chiffre saisi est égal au chiffre attendu..."""
            num_label.config(text='Correct !')
        elif dif == 5:
            """Si l'écart entre le chiffre saisi et le chiffre attendu est égal à 5 : assignation d'une couleur  
            blanche"""
            bc = 'white'
        elif dif < 5:
            """Si l'écart entre le chiffre saisi et le chiffre attendu est inférieur à 5 : assignation d'une couleur 
            rouge dégradée selon l'écart"""
            bc = f"#ff{dif}{dif}{dif}{dif}"
        else:
            """Sinon si l'écart entre le chiffre saisi et le chiffre attendu est supérieur à 5 : assignation d'une 
            couleur bleue dégradée selon l'écart"""
            bc = f"#{dif}{dif}{dif}{dif}ff"

        """Reconfiguration de la couleur de fond de la fenêtre"""
        root.config(bg=bc)

        """Reconfiguration de la couleur du titre de la fenêtre"""
        num_label.config(bg=bc)

    else:
        """Si le champ a autre qu'un chiffre (lettre...)... 

        Réinitialisation des données dans le champs de saisi"""
        guess_box.delete(0, END)

        """Information que le caractère saisi n'est pas un chiffre"""
        num_label.config(text="Hé ! Ce n'est pas un chiffre !")


def rando():
    """Fonction permettant de générer au hasard un chiffre en entier entre 1 et 10"""

    global num

    """Assignation d'un chiffre au hasard entre 1 et 10"""
    num = randint(1, 10)

    """Réinitialisation de la couleur de fond de fenêtre"""
    root.config(bg='SystemButtonFace')

    """Réinitialisation du titre de la fenêtre et de la couleur de fond"""
    num_label.config(text="Choisis un chiffre\nentre 1 et 10", bg='SystemButtonFace')

    """Réinitialisation du champ de saisi"""
    guess_box.delete(0, END)


"""Champ de saisi"""
guess_box = Entry(root, font='Helvetica 100', justify='center', width=2)
guess_box.pack(pady=20)

"""Bouton d'exécution pour recouper le chiffre saisi et le chiffre attendu"""
guess_button = Button(root, text='Soumettre', command=guesser)
guess_button.pack(pady=20)

"""Bouton d'exécution pour rejouer"""
random_button = Button(root, text='Nouveau chiffre', command=rando)
random_button.pack(pady=20)

"""Générer un chiffre au hasard dès le lancement du jeu"""
rando()

root.mainloop()
