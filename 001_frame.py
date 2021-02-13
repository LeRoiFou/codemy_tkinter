"""
Tkinter - Codemy.com #1 : 1ère fenêtre
Lien : https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1

Dans ce programme on apprend à afficher une message (étiquette)

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

from tkinter import *

root = Tk()


class Window(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.widgets()

    def widgets(self):
        self.myLabel = Label(root, text='Hello World !').pack()


window = Window(root)
root.mainloop()