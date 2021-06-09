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

import tkinter
from tkinter import filedialog
import os

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('600x400')
        self.widgets()

    def widgets(self):

        """Configuration d'un bouton d'exécution"""
        my_button = tkinter.Button(root, text='Ouvrir un programme', command=self.open_program)
        my_button.pack(pady=20)

        """Configuration d'un autre bouton d'exécution"""
        my_button2 = tkinter.Button(root, text='Ouvrir Calc', command=self.open_calc)
        my_button2.pack(pady=20)

        """Configuration d'une étiquette résultat"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)

    def open_program(self):
        """Méthode permettant d'ouvrir un fichier dans l'ordinateur"""
        
        # ouverture de la boîte de dialogue
        my_program = filedialog.askopenfilename()

        # chemin d'accès au fichier sélectionné  
        self.my_label.config(text=my_program)

        # ouverture du fichier avec l'instruction '"%s"' %
        os.system('"%s"' % my_program)  

    def open_calc(self):
        """Méthode permettant d'ouvrir directement un fichier Calc"""
        
        # chemin d'acces pour l'exécutable Calc
        calc = 'C:/Program Files/LibreOffice/program/scalc.exe'

        # accès du fichier exécutable en prenant en considération les espaces dans les noms
        os.system('"%s"' % calc)  


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
