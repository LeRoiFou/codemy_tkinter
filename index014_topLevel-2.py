"""
Tkinter - Codemy.com #14 : Toplevel
Lien : https://www.youtube.com/watch?v=qC3FYdpJI5Y&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=14

Ce programme permet d'afficher une nouvelle fenêtre

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

import tkinter
from PIL import ImageTk, Image

class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title('Apprendre à coder avec Codemy.com')
        self.widgets()

    def widgets(self):
        btn = tkinter.Button(root, text='Ouvrir une nouvelle fenêtre', command=OpenWindow)
        btn.pack()

class OpenWindow:
        
    def __init__(self):
        self.top = tkinter.Toplevel()
        self.top.title('Ma seconde fenêtre')
        self.top.iconbitmap('images/Logo.ico')
        self.widgets()

    def widgets(self):
        global my_image
        my_image = ImageTk.PhotoImage(Image.open('images/shrek.png'))
        my_label = tkinter.Label(self.top, image=my_image)
        my_label.pack()
        # L'instruction 'destroy' permet d'éviter de fermer automatiquement la 1ère fenêtre à la différence de 'quit'
        btn2 = tkinter.Button(self.top, text='Fermer la fenêtre', command=self.top.destroy)
        btn2.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()