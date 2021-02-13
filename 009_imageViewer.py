"""
Tkinter - Codemy.com #9 : Build an Image Viewer App With Python and TKinter
Lien : https://www.youtube.com/watch?v=zg4c92pNFeo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=9

Dans ce programme on apprend à défiler les images

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

from tkinter import *
from PIL import ImageTk, Image  # Module pour importer des images dans tkinter : package à télécharger -> Pillow

root = Tk()
root.title('Apprendre à coder avec Codemy.com')

"""Téléchargement des images"""
my_image = ImageTk.PhotoImage(Image.open('pic/pic1.png'))
my_image2 = ImageTk.PhotoImage(Image.open('pic/pic2.png'))
my_image3 = ImageTk.PhotoImage(Image.open('pic/pic3.png'))
my_image4 = ImageTk.PhotoImage(Image.open('pic/pic4.png'))

"""Assignation d'une variable sous forme d'une liste des images téléchargées"""
images_list = [my_image, my_image2, my_image3, my_image4]

"""Affichage des images sous la forme du widget Label"""
my_label = Label(image=my_image)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    """Fonction permettant d'afficher l'image suivante"""

    global my_label
    global button_forward
    global button_back

    """Réinitialisation des widgets"""
    my_label.grid_forget()
    my_label = Label(image=images_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 4:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def back(image_number):
    """Fonction permettant d'afficher l'image précédente"""

    global my_label
    global button_forward
    global button_back

    """Réinitialisation des widgets"""
    my_label.grid_forget()
    my_label = Label(image=images_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


"""Boutons d'exécution"""
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Sortie', command=quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

"""Affichages des boutons"""
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
