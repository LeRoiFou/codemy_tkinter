"""
Tkinter - Codemy.com #47 : Using Frames With Menus
Lien : https://www.youtube.com/watch?v=1cWWiXU02-g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=47

Combinaison des menus avec les frames

Éditeur : Laurent REYNAUD
Date : 29-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")


def our_command():
    myLabel = Label(root, text='Vous avez cliqué sur un menu déroulant !').pack()


def file_new():
    """Fonction pour la commande 'Nouveau' pour créer un cadre de couleur rouge"""
    hide_all_frames()  # récursivité ;p
    file_new_frame.pack(fill='both', expand=1)
    myLabel = Label(file_new_frame, text='Vous avez cliqué sur le menu Fichier -> Nouveau !').pack()


def edit_cut():
    """Fonction pour la commande 'Couper' pour créer un cadre de couleur bleue"""
    hide_all_frames()  # récursivité ;p
    edit_cut_frame.pack(fill='both', expand=1)
    myLabel = Label(edit_cut_frame, text='Vous avez cliqué sur le menu Édition -> Couper !').pack()


def hide_all_frames():
    """Cette fonction a pour but de 'cacher' le Frame appelé selon l'une des fonctions ci-avant"""
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# Configuration de la barre de menus
my_menu = Menu(root)
root.config(menu=my_menu)

# 1er titre de la barre de menus : 'Fichier'
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Fichier', menu=file_menu)

# Ajout des difféntes commandes du menu 'Fichier'
file_menu.add_command(label='Nouveau...', command=file_new)
file_menu.add_separator()
file_menu.add_command(label='Sortie', command=root.quit)

# 2ème titre de la barre de menus : 'Édition'
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Édition', menu=edit_menu)

# Ajout des difféntes commandes du menu 'Édition'
edit_menu.add_command(label='Couper', command=edit_cut)
edit_menu.add_command(label='Coller', command=our_command)

# 3ème titre de la barre de menus : 'Options'
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Options', menu=options_menu)

# Ajout des difféntes commandes du menu 'Options'
options_menu.add_command(label='Rechercher', command=our_command)
options_menu.add_command(label='Annuler', command=our_command)

#
file_new_frame = Frame(root, width=400, height=400, bg='red')
edit_cut_frame = Frame(root, width=400, height=400, bg='blue')
root.mainloop()
