"""
Tkinter - Codemy.com #105 : Build A Text Editor Part 2 - Open and Save As Files
Lien : https://www.youtube.com/watch?v=w5Nd4O76tDw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=105

Dans ce programme, on créé :
-> une fonction new_file() pour ouvrir un nouveau fichier
-> une fonction open_file() pour charger un fichier existant
-> une fonction save_as_file() pour enregistrer un fichier

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('1200x660')


def new_file():
    """Fonction qui permet d'ouvrir un nouveau fichier"""
    my_text.delete('1.0', END)  # suppression de l'ancien texte de textbox
    root.title('Nouveau fichier')  # mise à jour du titre de la fenêtre
    status_bar.config(text='Nouveau fichier        ')  # mise à jour de la barre de statut


def open_file():
    """Fonction qui permet d'ouvrir un fichier existant"""
    my_text.delete('1.0', END)  # suppression de l'ancien texte de textbox
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Ouvrir un fichier',
                                           filetypes=(('Fichier texte', '*.txt'),
                                                      ('Fichier HTML', '*.html'),
                                                      ('Fichier Python', '*.py'),
                                                      ('Tous fichiers', '*.*')))  # ouverture du fichier
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
    if text_file:  # si le fichier existe
        name = text_file  # variable pour la barre de statut
        status_bar.config(text=f"Sauvegardé sous {name}        ")  # mise à jour de la barre de statut
        name = name.replace('C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  # variable pour le titre de la fenêtre
        root.title(f'{name}')  # mise à jour du titre de la fenêtre
        text_file = open(text_file, 'w')  # écriture du fichier
        text_file.write(my_text.get(1.0, END))  # sauvegarde du fichier
        text_file.close()  # fermeture du fichier


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
file_menu.add_command(label='Enregistrer')
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
