"""
Tkinter - Codemy.com #45 : Binding Dropdown Menus and Combo Boxes
Lien : https://www.youtube.com/watch?v=OPUSBBD2OJw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=45

Création d'un bouton avec une liste des données + barre de menu déroulant

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter
from tkinter import ttk

class GUI:

    def __init__(self, root):
        self.root = root
        root.geometry('400x400')
        root.title("Titre !")
        self.widgets()

    def widgets(self):

        options = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

        self.clicked = tkinter.StringVar()
        self.clicked.set(options[0])

        drop = tkinter.OptionMenu(root, self.clicked, *options, command=self.selected)
        drop.pack(pady=20)

        self.myCombo = ttk.Combobox(root, value=options)
        self.myCombo.current(0)
        # la fonction bind() remplace l'instruction command non applicable pour un Combobox
        self.myCombo.bind('<<ComboboxSelected>>', self.comboclick)  
        self.myCombo.pack()

    def selected(self, event):
        
        if self.clicked.get() == 'vendredi':
            myLabel = tkinter.Label(root, text="C'est vendredi !").pack()
        else:
            myLabel = tkinter.Label(root, text=self.clicked.get()).pack()

    def comboclick(self, event):
        
        if self.myCombo.get() == 'vendredi':
            myLabel = tkinter.Label(root, text="C'est vendredi !").pack()
        else:
            myLabel = tkinter.Label(root, text=self.myCombo.get()).pack()

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()