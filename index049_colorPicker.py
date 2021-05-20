"""
Tkinter - Codemy.com #49 : Color Picker
Lien : https://www.youtube.com/watch?v=NDCirUTTrhg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=49

Dans ce programme, on peut choisir la couleur de l'écriture

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""

import tkinter
from tkinter import colorchooser

class GUI:

    def __init__(self, root):
        self.root = root
        root.geometry('400x400')
        root.title("Titre !")
        self.widget()

    def widget(self):

        my_button = tkinter.Button(root, text='Choisir une couleur', command=self.color).pack()

    def color(self):
        """Cette méthode permet d'afficher la fenêtre à sélection de couleurs"""
        
        # my_color = colorchooser.askcolor()  # donne en liste : le code couleur RGB + le code couleur hexadecimal
        # my_color = colorchooser.askcolor()[0]  # code couleur RGB
        # my_color = colorchooser.askcolor()[0][0]  # couleur rouge du code RGB
        # my_color = colorchooser.askcolor()[0][1]  # couleur verte du code RGB
        # my_color = colorchooser.askcolor()[0][2]  # couleur bleue du code RGB
        my_color = colorchooser.askcolor()[1]  # code couleur hexadécimal

        my_label = tkinter.Label(root, text=my_color).pack(pady=10)
        
        # L'instruction ci-dessous ne marche qu'avec un code couleur hexadécimal...
        my_label2 = tkinter.Label(root, text='Tu as choisi une couleur !', font='Helvetica 22', fg=my_color).pack()

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()