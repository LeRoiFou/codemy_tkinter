"""
Tkinter - Codemy.com #106 : Build A Text Editor Part 3 - Save Files
Lien : https://www.youtube.com/watch?v=yG0fAUn2uB0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=106

Dans ce programme on apprend à enregistrer un fichier déjà ouvert : si le fichier n'existe pas, l'enregistrement va se
faire automatiquement avec l'instruction 'enregistrer sous'

Éditeur : Laurent REYNAUD
Date : 18-12-20
"""

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('1200x660')

"""Déclaration d'une variable pour le nom du fichier ouvert 
Il est préconisé de déclarer toute variable globale à l'extérieure des fonctions"""
global open_status_name  # initialisation d'une variable globale
open_status_name = False  # variable globale à utiliser pour les fonctions suivantes


def new_file():
    """Fonction qui permet d'ouvrir un nouveau fichier
    La variable globale open_status_name est déclarée dans cette fonction, car à défaut, lorsqu'on ouvre un nouveau
    fichier et qu'on sélectionne 'Enregistrer', alors l'enregistrement va se faire automatiquement sur le fichier
    sample.txt et écraser les données saisies sur ce fichier, alors que l'enregistrement doit se diriger automatiquement
    sur l'instruction 'Enregistrer sous'"""
    my_text.delete('1.0', END)  # suppression de l'ancien texte de textbox
    root.title('Nouveau fichier')  # mise à jour du titre de la fenêtre
    status_bar.config(text='Nouveau fichier        ')  # mise à jour de la barre de statut
    global open_status_name  # appel de la variable globale
    open_status_name = False


def open_file():
    """Fonction qui permet d'ouvrir un fichier existant"""
    my_text.delete('1.0', END)  # suppression de l'ancien texte de textbox
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Ouvrir un fichier',
                                           filetypes=(('Fichier texte', '*.txt'),
                                                      ('Fichier HTML', '*.html'),
                                                      ('Fichier Python', '*.py'),
                                                      ('Tous fichiers', '*.*')))  # ouverture du fichier
    if text_file:  # vérifie s'il existe un nom de fichier
        global open_status_name  # initialisation d'une variable globale
        open_status_name = text_file  # déclaration de la variable d'ouverture du fichier en variable globale
    name = text_file  # variable pour la barre de statut
    status_bar.config(text=f"{name}        ")  # mise à jour de la barre de statut
    name = name.replace('C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  # variable pour le titre de la fenêtre
    root.title(f'{name}')  # mise à jour du titre de la fenêtre

    """Ouverture du fichier existant"""
    text_file = open(text_file, 'r')  # chargement du fichier
    stuff = text_file.read()  # ouverture du fichier
    my_text.insert(END, stuff)  # ajout du fichier au textbox
    text_file.close()  # fermeture du fichier ouvert


def save_as_file():
    """Fonction permettant d'enregistrer sous"""
    text_file = filedialog.asksaveasfilename(defaultextension='*.*',
                                             initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                             title='Fichier sauvegardé',
                                             filetypes=(('Fichier texte', '*.txt'),
                                                        ('Fichier HTML', '*.html'),
                                                        ('Fichier Python', '*.py'),
                                                        ('Tous fichiers', '*.*')))  # sauvegarde du fichier

    """Mise en commentaire ci-dessous, car on ne voit pas la différence avec ou sans la condition if..."""
    # if text_file:  # si le fichier existe
    #     name = text_file  # variable pour la barre de statut
    #     status_bar.config(text=f"Sauvegardé sous {name}        ")  # mise à jour de la barre de statut
    #     name = name.replace('C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  # var pour le titre de la fenêtre
    #     root.title(f'{name}')  # mise à jour du titre de la fenêtre
    #     text_file = open(text_file, 'w')  # écriture du fichier
    #     text_file.write(my_text.get(1.0, END))  # sauvegarde du fichier
    #     text_file.close()  # fermeture du fichier

    """Rectification des instructions ci-avant : ici on n'a pas appliqué la condition if..."""
    name = text_file  # variable pour la barre de statut
    status_bar.config(text=f"Sauvegardé sous {name}        ")  # mise à jour de la barre de statut
    name = name.replace('C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  # variable pour le titre de la fenêtre
    root.title(f'{name}')  # mise à jour du titre de la fenêtre
    text_file = open(text_file, 'w')  # écriture du fichier
    text_file.write(my_text.get(1.0, END))  # sauvegarde du fichier
    text_file.close()  # fermeture du fichier


def save_file():
    """Fonction permettant d'enregistrer un fichier"""
    global open_status_name  # recours à la variable globale déclarée initialement hors fonctions en début de programme
    if open_status_name:  # si la variable globale est True, à savoir que le fichier est déjà ouvert...
        text_file = open(open_status_name, 'w')  # écriture du fichier
        text_file.write(my_text.get(1.0, END))  # sauvegarde du fichier
        text_file.close()  # fermeture du fichier
        status_bar.config(text=f"Sauvegardé sous {open_status_name}        ")  # mise à jour de la barre de statut
    else:  # si le fichier n'existe pas...
        save_as_file()  # appel de cette fonction pour 'enregistrer sous'


"""Création d'un cadre pour le textbox et pour la barre de défilement"""
my_frame = Frame(root)
my_frame.pack(pady=5)

"""Création d'une barre de défilement pour le textbox"""
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

"""Création d'un textbox"""
my_text = Text(my_frame, width=97, height=25, font='helevetica 16', selectbackground='green', selectforeground='black',
               undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

"""Configuration de la barre de défilement"""
text_scroll.config(command=my_text.yview())

"""Création d'un menu"""
my_menu = Menu(root)
root.config(menu=my_menu)

"""Ajout du menu Fichier"""
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Fichier', menu=file_menu)
file_menu.add_command(label='Nouveau', command=new_file)
file_menu.add_command(label='Ouvrir', command=open_file)
file_menu.add_command(label='Enregistrer', command=save_file)
file_menu.add_command(label='Enregistrer sous', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Quitter', command=root.quit)

"""Ajout du menu Editer"""
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Éditer', menu=edit_menu)
edit_menu.add_command(label='Couper')
edit_menu.add_command(label='Copier')
edit_menu.add_command(label='Coller')
edit_menu.add_command(label='Annuler')
edit_menu.add_command(label='Rétablir')

"""Création d'une barre d'état en bas de la fenêtre"""
status_bar = Label(root, text='Prêt        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
