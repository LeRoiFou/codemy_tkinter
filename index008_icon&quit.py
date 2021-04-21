"""
Tkinter - Codemy.com #8 : icones, images et bouton 'exit'
Lien : https://www.youtube.com/watch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8

Dans ce programme on apprend à insérer un icône dans la barre d'outils de la fenêtre et à insérer une image

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

import tkinter
from PIL import ImageTk, Image  # Module pour importer des images dans tkinter : package à télécharger -> Pillow
import datetime


class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title('Apprendre à coder avec Codemy.com')
        # self.root.iconbitmap('images/homer.ico')  # Icone inséré dans la fenêtre
        self.widgets()

    def widgets(self):
        self.my_image = ImageTk.PhotoImage(Image.open('images/shrek.png'))
        now = datetime.datetime.now()
        tictac = datetime.datetime(2020, 11, 2, 8, 56, 30, 666666)
        if now >= tictac:
            my_label = tkinter.Label(root, image=self.my_image)  # L'image est insérée en tant qu'étiquette
            my_label.pack()
        button_quite = tkinter.Button(root, text='Quitter le programme', command=root.quit)
        button_quite.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()