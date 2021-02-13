"""
Tkinter - Codemy.com #74 : How To Open External Programs With Tkinter
Lien : https://www.youtube.com/watch?v=xu1ZKkgr-hE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=74

Dans ce programme on apprend à ouvrir un programme externe avec Tkinter en récupérant la boîte de dialogue affichant
répertoires et fichiers avec le sous-module tkinter filedialog et en ouvrant le fichier type avec le module os

On créé un deuxième bouton permettant d'ouvrir directement un fichier CALC

ATTENTION : avec le module os, on ne peut pas ouvrir de fichier dont le chemin comprend un espace dans le nom du
fichier/répertoire au lieu du caractère '_'. Pour éviter cette erreur, il suffit d'insérer dans l'instruction
d'ouverture du fichier avec le module os, les données suivantes : '"%s"' %

Éditeur : Laurent REYNAUD
Date : 10-12-20
"""

from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Mon titre !')
root.geometry('600x400')


def open_program():
    """Fonction permettant d'ouvrir un fichier dans l'ordinateur"""
    my_program = filedialog.askopenfilename()  # ouverture de la boîte de dialogue
    my_label.config(text=my_program)  # chemin d'accès au fichier sélectionné
    os.system('"%s"' % my_program)  # ouverture du fichier avec l'instruction '"%s"' %


def open_calc():
    """Fonction permettant d'ouvrir directement un fichier Calc"""
    calc = 'C:/Program Files (x86)/LibreOffice/program/scalc.exe'  # chemin d'acces pour l'exécutable Calc
    os.system('"%s"' % calc)  # accès du fichier exécutable en prenant en considération les espaces dans les noms


"""Configuration d'un bouton d'exécution"""
my_button = Button(root, text='Ouvrir un programme', command=open_program)
my_button.pack(pady=20)

"""Configuration d'un autre bouton d'exécution"""
my_button2 = Button(root, text='Ouvrir Calc', command=open_calc)
my_button2.pack(pady=20)

"""Configuration d'une étiquette résultat"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
