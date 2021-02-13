"""
Tkinter - Codemy.com #158 : Window Resizer Control Panel - Python Tkinter GUI Tutorial #158
Lien : https://www.youtube.com/watch?v=tRC5Yi50WM8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=158

Dans ce programme on apprend à contrôler la taille d'une nouvelle fenêtre avec des curseurs de la fenêtre principale

Éditeur : Laurent REYNAUD
Date : 01/01/21
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('300x650')


def launch():
    """Fonction permettant d'ouvrir une nouvelle fenêtre"""
    global second
    second = Toplevel()
    second.geometry('200x200')


def width_slide(*args):
    """Fonction permettant de redimensionner la largeur de la nouvelle fenêtre"""
    second.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")


def height_slide(*args):
    """Fonction permettant de redimensionner la hauteur de la nouvelle fenêtre"""
    second.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")


def both_slide(*args):
    """Fonction permettant de redimensionner la largeur ET la hauteur de la nouvelle fenêtre"""
    second.geometry(f"{int(both_slider.get())}x{int(both_slider.get())}")


"""Bouton d'exécution pour ouvrir une nouvelle fenêtre"""
launch_button = Button(root, text='Ouvrir une fenêtre', command=launch)
launch_button.pack(pady=20)

"""Cadre pour la largeur de la nouvelle fenêtre"""
width_frame = LabelFrame(root, text='Largeur')
width_frame.pack(pady=20)

"""Curseur pour la largeur"""
width_slider = ttk.Scale(width_frame, from_=100, to=500, orient=HORIZONTAL, length=200, command=width_slide, value=100)
width_slider.pack(pady=20, padx=20)

"""Cadre pour la hauteur de la nouvelle fenêtre"""
height_frame = LabelFrame(root, text='Hauteur')
height_frame.pack(pady=20)

"""Curseur pour la hauteur"""
height_slider = ttk.Scale(height_frame, from_=100, to=500, orient=VERTICAL, length=200, command=height_slide, value=100)
height_slider.pack(pady=20, padx=20)

"""Cadre pour la largeur ET la hauteur de la nouvelle fenêtre"""
both_frame = LabelFrame(root, text='Largeur et hauteur')
both_frame.pack(pady=20)

"""Curseur pour la largeur ET la hauteur"""
both_slider = ttk.Scale(both_frame, from_=100, to=500, orient=HORIZONTAL, length=200, command=both_slide, value=100)
both_slider.pack(pady=20, padx=20)

root.mainloop()
