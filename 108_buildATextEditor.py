"""
Tkinter - Codemy.com #108 : Build A Text Editor Part 5 - Undo Redo and Horizontal Scrollbar
Lien : https://www.youtube.com/watch?v=XW65JTd8UgI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=108

Dans ce programme on apprend :
-> À aligner les mots 'ctrl+x' pour couper, ..., avec l'instruction accelerator
-> À annuler et à rétablir sans recourir aux fonctions comme pour couper/copier/coller
-> À créer une barre de défilement horizontale dont l'instruction wrap=None lors de l'initialisation du textbox, qui
permet de ne pas revenir en début de ligne dès qu'on est arrivé au bout du champ de saisi

Éditeur : Laurent REYNAUD
Date : 18-12-20
"""

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('1200x680')

"""Déclaration d'une variable pour le nom du fichier ouvert 
Il est préconisé de déclarer toute variable globale à l'extérieure des fonctions"""
global open_status_name  # initialisation de la variable globale assignée pour le nom du fichier ouvert
open_status_name = False  # False = rien ne se passe lorsque le programme lit cette instruction

"""Déclaration d'une variable pour le texte sélectionné dans le textbox 
Il est préconisé de déclarer toute variable globale à l'extérieure des fonctions"""
global selected  # initialisation de la variable globale assignée pour le texte sélectionné
selecte = False  # False = rien ne se passe lorsque le programme lit cette instruction


def new_file():
    """Fonction qui permet d'ouvrir un nouveau fichier
    La variable globale open_status_name est déclarée dans cette fonction, car à défaut, lorsqu'on ouvre un nouveau
    fichier et qu'on sélectionne 'Enregistrer', alors l'enregistrement va se faire automatiquement sur le fichier
    sample.txt et écraser les données saisies sur ce fichier, alors que l'enregistrement doit se diriger automatiquement
    sur l'instruction 'Enregistrer sous'"""

    my_text.delete('1.0', END)  # suppression de l'ancien texte de textbox
    root.title('Nouveau fichier')  # mise à jour du titre de la fenêtre
    status_bar.config(text='Nouveau fichier        ')  # mise à jour de la barre de statut

    global open_status_name  # appel de la variable globale assignée pour l'ouverture du fichier
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

    name = text_file  # assignation d'une variable pour la barre de statut
    status_bar.config(text=f"{name}        ")  # mise à jour de la barre de statut
    name = name.replace('C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  # assignation variable pour titre fenêtre
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
    name = text_file  # assignation d'une variable pour la barre de statut
    status_bar.config(text=f"Sauvegardé sous {name}        ")  # mise à jour de la barre de statut
    name = name.replace('C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  # assignation variable remplacement chemin
    root.title(f'{name}')  # mise à jour du titre de la fenêtre
    text_file = open(text_file, 'w')  # écriture du fichier
    text_file.write(my_text.get(1.0, END))  # sauvegarde du fichier
    text_file.close()  # fermeture du fichier


def save_file():
    """Fonction permettant d'enregistrer un fichier"""

    global open_status_name  # appel de la variable globale assignée pour l'ouverture du fichier

    if open_status_name:  # si la variable globale est True, à savoir que le fichier est déjà ouvert...
        text_file = open(open_status_name, 'w')  # écriture du fichier
        text_file.write(my_text.get(1.0, END))  # sauvegarde du fichier
        text_file.close()  # fermeture du fichier
        status_bar.config(text=f"Sauvegardé sous {open_status_name}        ")  # mise à jour de la barre de statut
    else:  # si le fichier n'existe pas...
        save_as_file()  # appel de cette fonction pour 'enregistrer sous'


def cut_text(e):
    """Fonction permettant de couper le texte sélectionné dans le textbox"""

    global selected  # appel de la variable globale assignée pour le texte sélectionné

    if e:
        """Si le raccourci clavier CTRL + X a été utilisé..."""
        selected = root.clipboard_get()  # assignation d'une variable des données présentes dans le presse-papier
    else:
        """Les instructions ci-après permette de couper le texte sélectionner à partir du menu Fichier -> Couper"""
        if my_text.selection_get():  # si le texte est sélectionné...
            selected = my_text.selection_get()  # assignation d'une variable global du texte sélectionné
            my_text.delete('sel.first', 'sel.last')  # Suppression du texte sélectionné
            root.clipboard_clear()  # réinitialis. de toutes les données éventuellement présentes dans le presse-papier
            root.clipboard_append(selected)  # puis ajout du texte sélectionné dans le presse-papier


def copy_text(e):
    """Fonction permettant de copier le texte sélectionné dans le textbox"""

    global selected  # appel de la variable globale assignée pour le texte sélectionné

    """Verifie si nous avons utilisé les touches de raccourcis du clavier ainsi que les données présentes dans le 
    presse-papier : à chaque fois que l'on fait un copier/couper/coller, les données passent automatiquement dans le 
    presse-papier de windows.  
    Si on ne réinitialise pas toutes les données présentes dans le presse-papier, à un moment donné, on copiera quelque  
    chose qui était conservée dans le presse-papier, ce qui arrive de temps en temps dans LibreOffice..."""
    if e:
        """Si le raccourci clavier CTRL + C a été utilisé..."""
        selected = root.clipboard_get()  # assignation d'une variable des données présentes dans le presse-papier
    else:
        """Les instructions suivantes permettent de copier le texte sélectionné à partir du menu Fichier -> Copier"""
        if my_text.selection_get():  # si le texte est sélectionné...
            selected = my_text.selection_get()  # assignation d'une variable du texte sélectionné
            root.clipboard_clear()  # réinitialis. de toutes les données éventuellement présentes dans le presse-papier
            root.clipboard_append(selected)  # puis ajout du texte sélectionné dans le presse-papier


def paste_text(e):
    """Fonction permettant de coller le texte sélectionné dans le textbox"""

    global selected  # appel de la variable globale assignée pour le texte sélectionné

    if e:
        """Si le raccourci clavier CTRL + V a été utilisé..."""
        selected = root.clipboard_get()  # assignation d'une variable des données présentes dans le presse-papier
    else:
        """Les instructions suivantes permettent de copier le texte sélectionné à partir du menu Fichier -> Coller"""
        if selected:  # si le texte a été selectionné...
            position = my_text.index(INSERT)  # insertion à la position du curseur de la souris
            my_text.insert(position, selected)  # insertion du texte sélectionné dans le textbox


"""Création d'un cadre pour le textbox et pour la barre de défilement"""
my_frame = Frame(root)
my_frame.pack(pady=5)

"""Création d'une barre de défilement verticale pour le textbox"""
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

"""Création d'une barre de défilement horizontale pour le textbox"""
hor_scroll = Scrollbar(my_frame, orient=HORIZONTAL)
hor_scroll.pack(side=BOTTOM, fill=X)

"""Création d'un textbox"""
my_text = Text(my_frame, width=97, height=25, font='helevetica 16', selectbackground='green', selectforeground='black',
               undo=True, yscrollcommand=text_scroll.set, wrap='none', xscrollcommand=text_scroll.set)
my_text.pack()

"""Configuration de la barre de défilement verticale"""
text_scroll.config(command=my_text.yview)

"""Configuration de la barre de défilement horizontale"""
text_scroll.config(command=my_text.xview)

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
edit_menu.add_command(label='Couper', accelerator='(ctrl+x)', command=lambda: cut_text(False))
edit_menu.add_command(label='Copier', accelerator='(ctrl+c)', command=lambda: copy_text(False))
edit_menu.add_command(label='Coller', accelerator='(ctrl+v)', command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label='Annuler', accelerator='(ctrl+z)', command=my_text.edit_undo)
edit_menu.add_command(label='Rétablir', accelerator='(ctrl+y)', command=my_text.edit_undo)

"""Création d'une barre d'état en bas de la fenêtre"""
status_bar = Label(root, text='Prêt        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

"""Instructions bind pour les anomalies relevées dans le couper/copier/coller"""
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

root.mainloop()
