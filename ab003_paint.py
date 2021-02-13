""""
Application de peinture avec tkinter

Pour sauvegarder pleinement l'image, il faut que le zoom d'affichage de windows soit à 100 %

Éditeur : Laurent REYNAUD
Date : 28-12-2020
"""

from tkinter import *
import tkinter.ttk as ttk  # pour le widget Scale (curseur pour l'épaisseur du pinceau)
from tkinter import colorchooser  # pour le changement de couleur du pinceau et du canvas
from tkinter import filedialog  # pour l'ouverture de la fenêtre des fichiers
from PIL import Image, ImageDraw, ImageGrab, ImageTk  # pour la sauvegarde du dessinZ dans le canvas
from tkinter import messagebox  # pour le message d'information que la sauvegarde a été effectuée

root = Tk()
root.title('Codemy.com - Application de peinture')
root.iconbitmap('images/Logo.ico')
root.geometry('800x800')

"""Assignation d'une couleur par défaut du pinceau"""
brush_color = 'black'


def paint(e):
    """Fonction permettant de dessiner avec la souris"""

    """Paramètres du pinceau"""
    brush_width = int(my_slider.get())
    # brush_color = 'green'
    brush_type2 = brush_type.get()  # type de pinceau : BUTT, ROUND, ou PROJECTING

    """Position de début"""
    x1 = e.x - 1  # - 1 -> permet de référencer une position pour lancer le dessin
    y1 = e.y - 1
    """Position de fin"""
    x2 = e.x + 1
    y2 = e.y + 1

    """Dessin d'une ligne dans le canvas avec la souris"""
    my_canvas.create_line(x1, y1, x2, y2,
                          fill=brush_color,
                          width=brush_width,
                          capstyle=brush_type2,
                          smooth=True)


def change_brush_size(*args):
    """Fonction permettant de configurer le texte de l'épaisseur du pinceau"""
    slider_label.config(text=int(my_slider.get()))


def change_brush_color():
    """Fonction permettant de changer la couleur du pinceau"""

    """Assignation d'une variable globale avec une couleur noire par défaut"""
    global brush_color
    brush_color = 'black'

    """Fenêtre de sélection de couleur"""
    brush_color = colorchooser.askcolor(color=brush_color)[1]  # code couleur hexadécimal


def change_canvas_color():
    """Fonction permettant de changer la couleur du canvas"""

    """Assignation d'une variable globale avec une couleur noire par défaut"""
    global bg_color
    bg_color = 'black'

    """Fenêtre de sélection de couleur + configuration de la couleur du canvas"""
    bg_color = colorchooser.askcolor(color=bg_color)[1]  # code couleur hexadécimal
    my_canvas.config(bg=bg_color)


def clear_screen():
    """Fonction permettant de tout effacer du canvas"""
    my_canvas.delete(ALL)
    my_canvas.config(bg='white')


def save_as_png(*args):
    """Fonction permettant de sauvegarder sous format .png"""

    """Assignation de l'ouverture de la fenêtre de sauvegarde du dessin"""
    result = filedialog.asksaveasfilename(
        initialdir='C:/Users/LRCOM/PycharmProjects/tests/images',
        title='Sauvegarde du dessin sous format .png',
        filetypes=(('Fichier .png', '*.png'), ('Tous fichiers', '*.*')))

    """Sauvegarde par défaut sous format .png"""
    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'

    """Prise d'une 'photo' dans le dessin du canvas"""
    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)

    """Message d'information que la sauvegarde a été effectuée"""
    messagebox.showinfo('Image sauvegardée', 'Image sauvegardée avec succès')


"""Assignation des dimensions"""
w = 600
h = 400

"""Configuration du canvas"""
my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

# """Création de deux lignes dans le canvas formant une croix"""
# my_canvas.create_line(0, 100, 300, 100, fill='red')
# my_canvas.create_line(150, 0, 150, 200, fill='red')

"""Lien avec la souris"""
my_canvas.bind('<B1-Motion>', paint)

"""Cadre pour les options pour le dessin"""
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

"""Cadre pour l'épaisseur du pinceau"""
brush_size_frame = LabelFrame(brush_options_frame, text='Épaisseur')
brush_size_frame.grid(row=0, column=0, padx=50)

"""Curseur pour l'épaisseur du pinceau"""
my_slider = ttk.Scale(brush_size_frame, from_=0, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

"""Message affiché en dessous du curseur pour l'épaisseur du pinceau"""
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

"""Cadre pour le type de pinceau"""
brush_type_grame = LabelFrame(brush_options_frame, text='Type', height=400)
brush_type_grame.grid(row=0, column=1, padx=50)

"""Liste d'option pour les types de pinceau"""
brush_type = StringVar()  # variable de contrôle
brush_type.set('round')  # valeur par défaut
brush_type_radio1 = Radiobutton(brush_type_grame, text='Rond', variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(brush_type_grame, text='Entaille', variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(brush_type_grame, text='Diamant', variable=brush_type, value='projecting')
brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

"""Cadre pour la couleur du pinceau"""
change_colors_frame = LabelFrame(brush_options_frame, text='Couleurs')
change_colors_frame.grid(row=0, column=2, padx=50)

"""Bouton pour changer la couleur du pinceau"""
brush_color_button = Button(change_colors_frame, text='Couleur du pinceau', command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

"""Bouton pour changer la couleur de fond du canvas"""
canvas_color_button = Button(change_colors_frame, text='Couleur du canvas', command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

"""Cadre pour les options"""
options_frame = LabelFrame(brush_options_frame, text='Options')
options_frame.grid(row=0, column=3, padx=50)

"""Bouton pour tout effacer le dessin"""
clear_button = Button(options_frame, text="Effacer tout", command=clear_screen)
clear_button.pack(padx=10, pady=10)

"""Bouton pour sauvegarder le dessin"""
save_image_button = Button(options_frame, text='Sauvegarde .png', command=save_as_png)
save_image_button.pack(padx=10, pady=10)

root.mainloop()
