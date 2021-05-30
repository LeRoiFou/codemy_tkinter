"""
Tkinter - Codemy.com #70 : How To Move Images On Canvas
Lien : https://www.youtube.com/watch?v=2rF8-jbTL-8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=70

Dans ce programme on déplace une image avec canvas

Problème avec PhotoImage : on ne peut pas l'insérer dans une POO...

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

import tkinter

root = tkinter.Tk()
root.title('Mon titre !')
root.geometry('800x600')

"""Tailles et coordonnées en variables"""
w = 600
h = 400
x = w // 2
y = h // 2

"""Configuration d'un canvas sous fond blanc"""
my_canvas = tkinter.Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

"""Chargement de l'image au format .png et ajout au canvas"""
img = tkinter.PhotoImage(file='Images/shrek.png')
my_image = my_canvas.create_image(260, 125, anchor='nw', image=img)


def left(event):
    """Déplacement de 10 pixels à la gauche"""
    x = -10
    y = 0
    my_canvas.move(my_image, x, y)


def right(event):
    """Déplacement de 10 pixels à la droite"""
    x = 10
    y = 0
    my_canvas.move(my_image, x, y)


def up(event):
    """Déplacement de 10 pixels en haut"""
    x = 0
    y = -10
    my_canvas.move(my_image, x, y)


def down(event):
    """Déplacement de 10 pixels en bas"""
    x = 0
    y = 10
    my_canvas.move(my_image, x, y)


def pressing(event):
    """Déplacement avec les touches 'qsdz'"""
    x = 0
    y = 0
    if event.char == 'q': x = -10  # déplacement à gauche
    if event.char == 's': y = 10  # déplacement en bas
    if event.char == 'd': x = 10  # déplacement à droite
    if event.char == 'z': y = -10  # déplacement en haut
    my_canvas.move(my_image, x, y)


"""Configuration des touches 'qsdz' du clavier pour déplacer le cercle"""
root.bind("<Key>", pressing)

"""Configuration des touches directionnelles du clavier pour déplacer le cercle"""
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

root.mainloop()
