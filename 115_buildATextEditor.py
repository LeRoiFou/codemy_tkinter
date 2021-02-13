"""
Tkinter - Codemy.com #115 : Night Mode - Build A Text Editor Part 10
Lien : https://www.youtube.com/watch?v=35V5r6S2_FA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=115

Dans ce programme on apprend :
-> À activer / désactiver le mode sombre avec les fonctions night_on() et night_off()
On ne peut pas par contre modifier la couleur de la barre de menu...

Éditeur : Laurent REYNAUD
Date : 20-12-20
"""

from tkinter import *
from tkinter import filedialog  # pour l'ouverture et l'enregistrement des fichiers
from tkinter import font  # pour la police d'écriture en gras et en italique
from tkinter import colorchooser  # pour la couleur d'écriture
import win32api  # pour l'impression d'un texte

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Éditeur de texte ;)')
root.geometry('1200x710')

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


def bold_it():
    """Fonction permettant de mettre en gras l'écriture"""

    """Création de la police d'écriture"""
    bold_font = font.Font(my_text, my_text.cget('font'))
    bold_font.config(weight='bold')

    """Configuration du texte sélectionné"""
    my_text.tag_config('bold', font=bold_font)

    current_tags = my_text.tag_names('sel.first')  # assignation d'une variable du texte sélectionné
    if 'bold' in current_tags:
        "Si le texte est déjà en gras... supprimer cette mise en forme"
        my_text.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        """sinon ajouter cette mise en forme"""
        my_text.tag_add('bold', 'sel.first', 'sel.last')


def italics_it():
    """Fonction permettant de mettre en italique l'écriture"""

    """Création de la police d'écriture"""
    italics_font = font.Font(my_text, my_text.cget('font'))
    italics_font.config(slant='italic')

    """Configuration du texte sélectionné"""
    my_text.tag_config('italic', font=italics_font)

    current_tags = my_text.tag_names('sel.first')  # assignation d'une variable du texte sélectionné
    if 'italic' in current_tags:
        "Si le texte est déjà en italique... supprimer cette mise en forme"
        my_text.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        """sinon ajouter cette mise en forme"""
        my_text.tag_add('italic', 'sel.first', 'sel.last')


def text_color():
    """Change la couleur de l'écriture du texte sélectionné"""

    """Choisir une couleur"""
    my_color = colorchooser.askcolor()[1]  # code couleur hexadecimal

    if my_color:
        """La mise en place de cette condition permet d'éviter annuler la couleur sélectionnée lorsqu'on appuie sur le  
        bouton 'annuler' de la boîte de dialogue des couleurs présentées"""

        """Création de la couleur d'écriture"""
        color_font = font.Font(my_text, my_text.cget('font'))

        """Configuration du texte sélectionné"""
        my_text.tag_config('colored', font=color_font, foreground=my_color)

        current_tags = my_text.tag_names('sel.first')  # assignation d'une variable du texte sélectionné
        if 'colored' in current_tags:
            "Si le texte est déjà colorié ... supprimer cette mise en forme"
            my_text.tag_remove('colored', 'sel.first', 'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            my_text.tag_add('colored', 'sel.first', 'sel.last')


def all_text_color():
    """Change la couleur de tout le texte"""

    """Choisir une couleur"""
    my_color = colorchooser.askcolor()[1]  # code couleur hexadecimal

    if my_color:
        my_text.config(fg=my_color)


def bg_color():
    """Change la couleur du fond d'écran"""

    """Choisir une couleur"""
    my_color = colorchooser.askcolor()[1]  # code couleur hexadecimal

    if my_color:
        my_text.config(bg=my_color)


def print_file():
    """Fonction permettant d'imprimer un fichier"""
    file_to_print = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                               title='Ouvrir un fichier',
                                               filetypes=(('Fichier texte', '*.txt'),
                                                          ('Fichier HTML', '*.html'),
                                                          ('Fichier Python', '*.py'),
                                                          ('Tous fichiers', '*.*')))  # ouverture du fichier

    if file_to_print:
        win32api.ShellExecute(0, 'print', file_to_print, None, '.', 0)  # fonctionnalité à connaître pour imprimer


def select_all(e):
    """Permet de sélectionner tout le texte"""

    """Ajouter une balise 'sel' pour tout sélectionner"""
    my_text.tag_add('sel', '1.0', 'end')  # sélection de la 1ère à la dernière ligne


def clear_all():
    """Permet d'effacer tout le texte"""
    my_text.delete(1.0, END)


def night_on():
    """Fonction permettant d'activer le mode sombre"""

    main_color = '#000000'  # assignation couleur noire
    second_color = '#373737'  # assignation couleur grise foncée
    text_color = 'green'  # assignation couleur verte

    """Principaux widgets"""
    root.config(bg=main_color)  # fond de fenêtre
    status_bar.config(bg=main_color, fg=text_color)  # barre de statut en bas de la fenêtre
    my_text.config(bg=second_color)  # champ de texte
    toolbar_frame.config(bg=main_color)  # barre d'outils
    """Boutons de la barre d'outils"""
    bold_button.config(bg=second_color)
    italics_button.config(bg=second_color)
    redo_button.config(bg=second_color)
    undo_button.config(bg=second_color)
    color_text_button.config(bg=second_color)
    """Menu"""
    file_menu.config(bg=main_color, fg=text_color)
    edit_menu.config(bg=main_color, fg=text_color)
    color_menu.config(bg=main_color, fg=text_color)
    options_menu.config(bg=main_color, fg=text_color)


def night_off():
    """Fonction permettant de désactiver le mode sombre"""

    main_color = 'SystemButtonFace'  # assignation de la couleur par défaut
    second_color = 'SystemButtonFace'  # assignation de la couleur par défaut
    text_color = 'black'  # assignation couleur noire

    """Principaux widgets"""
    root.config(bg=main_color)  # fond de fenêtre
    status_bar.config(bg=main_color, fg=text_color)  # barre de statut en bas de la fenêtre
    my_text.config(bg='white')  # champ de texte
    toolbar_frame.config(bg=main_color)  # barre d'outils
    """Boutons de la barre d'outils"""
    bold_button.config(bg=second_color)
    italics_button.config(bg=second_color)
    redo_button.config(bg=second_color)
    undo_button.config(bg=second_color)
    color_text_button.config(bg=second_color)
    """Menu"""
    file_menu.config(bg=main_color, fg=text_color)
    edit_menu.config(bg=main_color, fg=text_color)
    color_menu.config(bg=main_color, fg=text_color)
    options_menu.config(bg=main_color, fg=text_color)


"""Création d'un cadre pour la barre d'outils"""
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

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
file_menu.add_command(label='Imprimer', command=print_file)
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
edit_menu.add_separator()
edit_menu.add_command(label='Sélectionner tout', accelerator='(ctrl+a)', command=lambda: select_all(True))
edit_menu.add_command(label='Effacer tout', command=clear_all)

"""Ajout du menu Couleur"""
color_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Couleur', menu=color_menu)
color_menu.add_command(label='Sur le texte sélectionné', command=text_color)
color_menu.add_command(label='Sur tout le texte', command=all_text_color)
color_menu.add_command(label="Fond d'écran", command=bg_color)

"""Ajout du menu Options"""
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Mode nuit activé', command=night_on)
options_menu.add_command(label='Mode nuit désactivé', command=night_off)

"""Création d'une barre d'état en bas de la fenêtre"""
status_bar = Label(root, text='Prêt        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

"""Instructions bind pour les anomalies relevées dans le couper/copier/coller"""
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

"""Liaison entre les touches de raccourcis 'ctrl+a' avec le menu Éditer -> Sélectionner tout"""
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)

"""Création des boutons de la barre d'outils"""
bold_button = Button(toolbar_frame, text='Gras', command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)
italics_button = Button(toolbar_frame, text='Italique', command=italics_it)
italics_button.grid(row=0, column=1, padx=5)
undo_button = Button(toolbar_frame, text='Annuler', command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
redo_button = Button(toolbar_frame, text='Rétablir', command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)
color_text_button = Button(toolbar_frame, text='Couleur du texte', command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()
