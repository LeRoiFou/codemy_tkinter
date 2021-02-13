"""
Tkinter - Codemy.com #14 : Toplevel
Lien : https://www.youtube.com/watch?v=qC3FYdpJI5Y&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=14

Ce programme permet d'afficher une nouvelle fenêtre

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Apprendre à coder avec Codemy.com')


def open_window():
    """La variable my_image est déclarée en tant que 'global' afin que l'image puisse être affiché dans la 2ème fenêtre
    L'instruction 'destroy' permet d'éviter de fermer automatiquement la 1ère fenêtre à la différence de 'quit'"""
    global my_image  # pour afficher l'image dans la 2ème fenêtre
    top = Toplevel()
    top.title('Ma seconde fenêtre')
    top.iconbitmap('images/Logo.ico')
    my_image = ImageTk.PhotoImage(Image.open('images/shrek.png'))
    my_label = Label(top, image=my_image)
    my_label.pack()
    btn2 = Button(top, text='Fermer la fenêtre', command=top.destroy)  # destroy : évite de fermer la 1ère fenêtre
    btn2.pack()


btn = Button(root, text='Ouvrir une nouvelle fenêtre', command=open_window)
btn.pack()

root.mainloop()
