"""
Tkinter - Codemy.com #8 : icones, images et bouton 'exit'
Lien : https://www.youtube.com/watch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8

Dans ce programme on apprend à insérer un icône dans la barre d'outils de la fenêtre et à insérer une image

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

from tkinter import *
from PIL import ImageTk, Image  # Module pour importer des images dans tkinter : package à télécharger -> Pillow
from datetime import *

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.iconbitmap('images/homer.ico')  # Icone inséré dans la fenêtre


class Window(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.widgets()

    def widgets(self):
        self.my_image = ImageTk.PhotoImage(Image.open('images/shrek.png'))
        self.now = datetime.now()
        self.tictac = datetime(2020, 11, 2, 8, 56, 30, 666666)
        if self.now >= self.tictac:
            self.my_label = Label(image=self.my_image)  # L'image est insérée en tant qu'étiquette
            self.my_label.pack()
        self.button_quite = Button(self, text='Quitter le programme', command=self.quit)
        self.button_quite.pack()


window = Window(root)
root.mainloop()
