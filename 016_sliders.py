"""
Tkinter - Codemy.com #16 : sliders
Lien : https://www.youtube.com/watch?v=knUHd8ZGyiM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=16

Dans ce programme on apprend à afficher des barres des défilement chiffrés

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

from tkinter import *

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.geometry('400x400')

vertical = Scale(root, from_=0, to_=400)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get())
    my_label.pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))


horizontal = Scale(root, from_=0, to_=400, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text='Clique moi !', command=slide)
my_btn.pack()

root.mainloop()
