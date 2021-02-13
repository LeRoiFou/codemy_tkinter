"""
Tkinter - Codemy.com #15 : boîte de dialogue (dialog box)
Lien : https://www.youtube.com/watch?v=Aim_7fC-inw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=15

Dans ce programme, on apprend à ouvrir un fichier de type .png

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Apprendre à coder avec Codemy.com')


def open():
    """Ouverture d'une boîte de dialogue pour charger un fichier sous format.jpg"""
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/codemy_tkinter/images',
                                               title='Sélectionner un fichier',
                                               filetypes=(('Fichiers .png', '*.png'), ('Tous fichiers', '*.*')))
    my_label = Label(root, text=root.filename)
    my_image = ImageTk.PhotoImage(Image.open(root.filename))  # Chargement de l'image
    my_image_label = Label(image=my_image).pack()  # Affichage de l'image sous la forme d'une étiquette


my_btn = Button(root, text='Ouvrir le fichier', command=open).pack()

root.mainloop()
