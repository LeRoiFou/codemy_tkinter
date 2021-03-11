"""
Tkinter - Codemy.com #170 :
Lien : https://www.youtube.com/watch?v=XaVp2l6Z_Dc

Dans ce programme on apprend à générer un mot de passe 'difficile' en donnant uniquement le nombre de caractères
souhaités

Pour cela, on va recourir au module random pour générer des entiers au hasard et pour chaque entier généré est affecté
un caractère selon la table ASCII détaillée ci-après : https://www.asciitable.com/, à partir du code décimal n° 33 qui
pour ce code, génère comme caractère le '!', jusqu'au code décimal n° 126 qui pour ce code, génère comme caractère
le '~'

Éditeur : Laurent REYNAUD
Date : 11-03-21
"""

import tkinter
from random import randint  # pour générer un mot de passe avec des caractères sélectionnés au hasard

root = tkinter.Tk()
root.title('Mega-mot de passe !!!')
root.geometry('500x300')


def new_rand():
    """Fonction permettant de générer un mot de passe au hasard"""

    """Données saisies effacées"""
    pw_entry.delete(0, 'end')

    """Chiffre saisi dans le champ de saisi converti en entier"""
    pw_length = int(my_entry.get())

    """Assignation d'une str"""
    my_password = ''

    """Boucle for in range"""
    for x in range(pw_length):
        """Incrémentation des nombres au hasard compris entre l'entier 33 et l'entier 126 converti en caractères"""
        my_password += chr(randint(33, 126))

    """Insertion du mot de passe généré dans le champ de saisi"""
    pw_entry.insert(0, my_password)


def clipper():
    """Fonction permettant de copier dans le presse-papier le mot de passe généré"""

    """Effacement des données présentes dans le presse-papier"""
    root.clipboard_clear()

    """Alimentation dans le presse-papier des données copiées"""
    root.clipboard_append(pw_entry.get())


"""Champ de saisi pour saisir le nombre de caractère du mot de passe à générer et son cadre"""
lf = tkinter.LabelFrame(root, text='Combien de caractères ?')  # cadre
lf.pack(pady=20)
my_entry = tkinter.Entry(lf, font='Helvetica 24', justify='center')  # champ de saisi
my_entry.pack(pady=20, padx=20)

"""Champ de saisi 'déguisé' en étiquette pour afficher le mot de passe généré et pour qu'on puisse le copier"""
pw_entry = tkinter.Entry(root, text='', font='Helvetica 24', justify='center', bd=0,
                         bg="systembuttonface")  # champ de saisi
pw_entry.pack(pady=20)

"""Les boutons et son cadre"""
my_frame = tkinter.Frame(root)  # cadre
my_frame.pack(pady=20)
my_button = tkinter.Button(my_frame, text='Générer un MDP', command=new_rand)  # bouton
my_button.grid(row=0, column=0, padx=10)
clip_button = tkinter.Button(my_frame, text='Copier le MDP', command=clipper)  # bouton
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
