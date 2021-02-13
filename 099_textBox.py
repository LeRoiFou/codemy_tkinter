"""
Tkinter - Codemy.com #99 : Text Box Widgets in Tkinter
Lien : https://www.youtube.com/watch?v=Qrmab6lSzU4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=99

Le widget Text Box permet de saisir du texte sur plusieurs lignes à la différence du champ de saisi Entry

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x450')


def clear():
    """Fonction permettant d'effacer le texte dans le widget text box"""
    my_text.delete(1.0, END)  # attention : au lieu de 0 dans la plupart des widgets, c'est 1.0 pour le text box !


def get_text():
    """Fonction permettant de récupérer le texte saisi dans le widget text box et d'afficher le texte saisi"""
    my_label.config(text=my_text.get(1.0, 5.0))  # récupération de la 1ère ligne à la 4ème ligne


"""Configuration de la boîte de texte"""
my_text = Text(root, width=40, height=10, font='Helvetica 16')
my_text.pack(pady=20)

"""Création d'un cadre pour les boutons détaillés ci-après"""
button_frame = Frame(root)
button_frame.pack()

"""Création d'un bouton d'exécution permetttant d'effacer le texte dans le widget text box"""
clear_button = Button(button_frame, text='Effacer le texte', command=clear)
clear_button.grid(row=0, column=0)

"""Création d'un bouton d'exécution permettant de récupérer et d'afficher le texte saisi dans le widget text box"""
get_text_buttuon = Button(button_frame, text='Récup texte saisi', command=get_text)
get_text_buttuon.grid(row=0, column=1, padx=20)

"""Affichage du texte saisi dans le widget text box : cette étiquette est configurée dans la fonction get_text()"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
