"""
Tkinter - Codemy.com #100 : Read And Write To Text Files
Lien : https://www.youtube.com/watch?v=Z_0ISFfT_eM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=100

Dans ce programme on continue avec le widget text box mais cette fois-ci on apprend à récuper un texte issue d'un
fichier texte et de l'afficher dans le widget text box et pouvoir également rectifier le texte et l'enregistrer dans le
fichier d'origine

Ci-dessous les différentes instructions après avoir cibler le fichier à prendre en compte :
-> r : lire
-> r+ : lire et écrire
-> w : écrire
-> w+ : écrire et lire
-> a : ajouter
-> a+ : ajouter et lire

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

from tkinter import *
from tkinter import filedialog

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x450')


def open_text():
    """Fonction permettant de récupérer un fichier texte et de l'afficher dans le widget textbox"""
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Ouvrir un fichier texte',
                                           filetypes=(('Fichiers .txt', '*.txt'),))  # voir tuto n° 15_DialogBox.py
    text_file = open(text_file, 'r')  # ouverture du fichier, lecture du fichier
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def save_txt():
    """Fonction permettant de sauvegarder les modifications faites dans le widget textbox dans le fichier ouvert"""
    text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                           title='Enregistrer sous',
                                           filetypes=(('Fichiers .txt', '*.txt'),))  # voir tuto n° 15_DialogBox.py
    text_file = open(text_file, 'w')  # ouverture du fichier, écriture du fichier
    text_file.write(my_text.get(1.0, END))


"""Configuration de la boîte à texte"""
my_text = Text(root, width=40, height=10, font='helvetica 16')
my_text.pack(pady=20)

"""Configuration du bouton d'exécution permettant d'ouvrir un fichier texte"""
open_button = Button(root, text='Ouvrir un fichier texte', command=open_text)
open_button.pack(pady=20)

"""Configuration du bouton de sauvegarde des données saisies dans le widget text box"""
save_button = Button(root, text='Sauvegarder', command=save_txt)
save_button.pack(pady=20)

root.mainloop()
