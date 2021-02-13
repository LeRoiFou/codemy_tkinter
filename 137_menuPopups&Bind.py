"""
Tkinter - Codemy.com #137 : Right Click Menu Popups With Tkinter - Python Tkinter GUI Tutorial #137
Lien : https://www.youtube.com/watch?v=KRuUtNxOb_k&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=137

Dans ce programme on apprend à afficher le menu n'importe où dans la fenêtre en appuyant sur le bouton de droite de la
souris

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')


def hello():
    """Fonction affichant un message"""
    my_label.config(text='Salut !')


def goodbye():
    """Fonction affichant un message"""
    my_label.config(text='Ciao !')


def my_popup(e):
    """Fonction permettant d'afficher le menu dans la fenêtre selon l'endroit où on a cliqué avec le bouton de droite de
    la souris"""
    my_menu.tk_popup(e.x_root, e.y_root)


"""Menu"""
my_menu = Menu(root, tearoff=0)
my_menu.add_command(label='Dire bonjour', command=hello)
my_menu.add_command(label='Dire au revoir', command=goodbye)
my_menu.add_separator()
my_menu.add_command(label='Quitter', command=root.quit)

"""Bind avec le bouton de droite de la souris"""
root.bind('<Button-3>', my_popup)

"""Etiquette"""
my_label = Label(root, text='', font='Helvetica 20')
my_label.pack(pady=20)

root.mainloop()
