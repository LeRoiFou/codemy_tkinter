"""
Tkinter - Codemy.com #1 : 1ère fenêtre
Lien : https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1

Dans ce programme on apprend à afficher une message (étiquette)

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

import tkinter




class GUI:

    def __init__(self, root):
        self.root = root
        self.widgets()

    def widgets(self):
        self.myLabel = tkinter.Label(root, text='Hello World !').pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()