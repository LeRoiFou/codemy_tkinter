"""
Tkinter - Codemy.com #148 : Dynamically Resize Background Images - Python Tkinter GUI Tutorial #148
Lien : https://www.youtube.com/watch?v=xiGQD2J47nA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=148

Dans ce programme on continue à mettre une image au fond de la fenêtre, mais cette fois-ci on redimensionne
dynamiquement l'image par rapport aux dimensions de la fenêtre

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('800x500')

"""Chargement de l'image"""
bg = ImageTk.PhotoImage(file='images/mario.png')

"""Création d'un canvas"""
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill='both', expand=True)

"""Affichage de l'image dans le canvas"""
my_canvas.create_image(0, 0, image=bg, anchor='nw')  # l'instruction anchor permet d'afficher pleinement l'image

"""Ajout du titre"""
my_canvas.create_text(400, 250, text='Bienvenue !', font='Helvetica 50', fill='white')  # fill : couleur d'écriture

"""Ajout de boutons"""
button1 = Button(root, text='Sortie')
button2 = Button(root, text='Commencer')
button3 = Button(root, text='Effacer')

"""Ajout des boutons au canvas"""
button1_window = my_canvas.create_window(10, 10, anchor='nw', window=button1)
button2_window = my_canvas.create_window(55, 10, anchor='nw', window=button2)
button3_window = my_canvas.create_window(137, 10, anchor='nw', window=button3)


def resizer(e):
    """Fonction permettant de redynamiser la taille de l'image avec la fenêtre"""

    global bg1, resized_bg, new_bg

    """Chargement de l'image"""
    bg1 = Image.open('images/mario.png')

    """Redimensionner l'image"""
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)

    """Redéfinir à nouveau l'image"""
    new_bg = ImageTk.PhotoImage(resized_bg)

    """Ajout au canvas"""
    my_canvas.create_image(0, 0, image=new_bg, anchor='nw')

    """Ajout du titre"""
    my_canvas.create_text(400, 250, text='Bienvenue !', font='Helvetica 50', fill='white')  # fill : couleur d'écriture


# """Affichage de l'image dans la fenêtre"""
# my_label = Label(root, image=bg)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)  # relwidth/relheight -> l'image accrochée au centre de la fenêtre
#
# """Ajout d'un titre en haut de l'image"""
# my_text = Label(root, text='Bienvenue !', font='Helvetica 50', fg='white', bg='#6b88fe')
# my_text.pack(pady=50)
#
# """Ajout d'un cadre"""
# my_frame = Frame(root, bg='#6b88fe')
# my_frame.pack(pady=20)
#
# """Ajout de boutons"""
# my_button1 = Button(my_frame, text='Sortie')
# my_button1.grid(row=0, column=0, padx=10)
# my_button2 = Button(my_frame, text='Commencer')
# my_button2.grid(row=0, column=1, padx=10)
# my_button3 = Button(my_frame, text='Effacer')
# my_button3.grid(row=0, column=2, padx=10)

root.bind('<Configure>', resizer)

root.mainloop()
