"""
Tkinter - Codemy.com #69 : Move Canvas Shapes With Arrow Keys
Lien : https://www.youtube.com/watch?v=xifcE6xvnyg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=69

Dans ce programme on déplace un cercle créé dans canvas soit avec les touches 'qsdz' soit avec les touches
directionnelles du clavier

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('800x600')

"""Tailles et coordonnées en variables"""
w = 600
h = 400
x = w // 2
y = h // 2

"""Configuration d'un canvas sous fond blanc"""
my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

"""Configuration d'un cercle"""
my_circle = my_canvas.create_oval(x, y, x + 10, y + 10)


def left(event):
    """Déplacement de 10 pixels à la gauche"""
    x = -10
    y = 0
    my_canvas.move(my_circle, x, y)


def right(event):
    """Déplacement de 10 pixels à la droite"""
    x = 10
    y = 0
    my_canvas.move(my_circle, x, y)


def up(event):
    """Déplacement de 10 pixels en haut"""
    x = 0
    y = -10
    my_canvas.move(my_circle, x, y)


def down(event):
    """Déplacement de 10 pixels en bas"""
    x = 0
    y = 10
    my_canvas.move(my_circle, x, y)


def pressing(event):
    """Déplacement avec les touches 'qsdz'"""
    x = 0
    y = 0
    if event.char == 'q': x = -10  # déplacement à gauche
    if event.char == 's': y = 10  # déplacement en bas
    if event.char == 'd': x = 10  # déplacement à droite
    if event.char == 'z': y = -10  # déplacement en haut
    my_canvas.move(my_circle, x, y)


"""Configuration des touches 'qsdz' du clavier pour déplacer le cercle"""
root.bind("<Key>", pressing)

"""Configuration des touches directionnelles du clavier pour déplacer le cercle"""
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

root.mainloop()
