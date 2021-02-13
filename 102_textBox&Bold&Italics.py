"""
Tkinter - Codemy.com #102 : Text Widget Bold and Italics Text
Lien : https://www.youtube.com/watch?v=X6zqePBPDVU&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=102

Toujours avec le widget text box, cette fois-ci on apprend à :
-> afficher le texter sélectionné
-> mise en gras du texte sélectionné avec la classe du module de tkinter : font
-> mise en italique du texte séléctionné

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

from tkinter import *
from tkinter import filedialog
from tkinter import font  # pour la police d'écriture gras et italique détaillée ci-après

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x600')


def open_text():
    """Fonction permettant de récupérer un fichier texte et de l'afficher dans le widget textbox"""
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Ouvrir un fichier texte',
                                           filetypes=(('Fichiers .txt', '*.txt'), ('Tous fichiers', '*.*')))
    text_file = open(text_file, 'r')  # ouverture du fichier, lecture du fichier
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def save_txt():
    """Fonction permettant de sauvegarder les modifications faites dans le widget textbox dans le fichier ouvert"""
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Enregistrer sous',
                                           filetypes=(('Fichiers .txt', '*.txt'),))
    text_file = open(text_file, 'w')  # ouverture du fichier, écriture du fichier
    text_file.write(my_text.get(1.0, END))


def add_image():
    """Ajout d'une image dans le text box"""
    global my_image
    my_image = PhotoImage(file='images/shrek.png')  # chargement de l'image
    position = my_text.index(INSERT)  # insertion à la position du curseur de la souris
    my_text.image_create(position, image=my_image)  # insertion de l'image dans le widget textbox


def select():
    """Affichage du texte surligné"""
    selected = my_text.selection_get()
    my_label.config(text=selected)


def bold():
    """Mise en gras du texte sélectionné"""
    bold_font = font.Font(my_text, my_text.cget('font'))  # récupération de la police d'écriture du texte sélectionné
    bold_font.config(weight='bold')  # configuration pour la mise en gras du texte sélectionné
    my_text.tag_config('bold', font=bold_font)
    current_tags = my_text.tag_names('sel.first')
    if 'bold' in current_tags:
        "Si le texte est déjà en gras... supprimer cette mise en forme"
        my_text.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        """sinon ajouter cette mise en forme"""
        my_text.tag_add('bold', 'sel.first', 'sel.last')


def italics_it():
    """Mise en italique du texte sélectionné"""
    italics_font = font.Font(my_text, my_text.cget('font'))
    italics_font.config(slant='italic')
    my_text.tag_config('italic', font=italics_font)
    current_tags = my_text.tag_names('sel.first')
    if 'italic' in current_tags:
        "Si le texte est déjà en italique... supprimer cette mise en forme"
        my_text.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        """sinon ajouter cette mise en forme"""
        my_text.tag_add('italic', 'sel.first', 'sel.last')


"""Création d'un cadre pour le textbox et la barre de défilement"""
my_frame = Frame(root)
my_frame.pack(pady=10)

"""Création d'une barre de défilement pour le texbox"""
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

"""Configuration de la boîte à texte"""
my_text = Text(my_frame, width=40, height=10, font='helvetica 16',
               selectbackground='red',  # surbrillance en rouge du texte sélectionné
               selectforeground='black',  # écriture en noir du texte en surbrillance de couleur rouge
               yscrollcommand=text_scroll.set  # liaison avec la barre de défilement
               )
my_text.pack(pady=20)

"""Configuration de la barre de défilement"""
text_scroll.config(command=my_text.yview)

"""Configuration du bouton d'exécution permettant d'ouvrir un fichier texte"""
open_button = Button(root, text='Ouvrir un fichier texte', command=open_text)
open_button.pack(pady=20)

"""Configuration du bouton de sauvegarde des données saisies dans le widget text box"""
save_button = Button(root, text='Sauvegarder', command=save_txt)
save_button.pack(pady=20)

"""Configuration du bouton d'exécution pour insérer une image dans le text box"""
image_button = Button(root, text='Ajouter une image', command=add_image)
image_button.pack(pady=5)

"""Configuration du bouton d'exécution pour afficher le texte sélectionné"""
select_button = Button(root, text='Sélectionner le texte', command=select)
select_button.pack(pady=5)

"""Affichage du texte surligné dont la configuration de l'étiquette se trouve dans la fonction select()"""
my_label = Label(root, text='')
my_label.pack()

"""Configuration du bouton d'exécution pour mettre en gras le texte sélectionné"""
bold_button = Button(root, text='Gras', command=bold)
bold_button.pack(pady=5)

"""Configuration du bouton d'exécution pour mettre en italique le texte sélectionné"""
italics_button = Button(root, text='Italique', command=italics_it)
italics_button.pack(pady=5)

root.mainloop()
