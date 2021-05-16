"""
Tkinter - Codemy.com #43 : Classes & tkinter
Lien : https://www.youtube.com/watch?v=Jl1xsH6MR1g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=43

Recourir à la POO avec tkinter permet mieux structurer son programme...

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")


class John(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.widgets()

    def clicker(self):
        print('Regarde ... tu as cliqué !!!')

    def widgets(self):
        myButton = Button(self, text='Clique-moi !', command=self.clicker)
        myButton.pack(pady=20)


john = John(root)
root.mainloop()
