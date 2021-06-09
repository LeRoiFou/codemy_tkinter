"""
Tkinter - Codemy.com #77 : How To Resize Images With Tkinter
Lien : https://www.youtube.com/watch?v=w0mtuHsE7IM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=77

Dans ce programme on apprend à redimensionner des images affichées en tant qu'étiquettes

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('Mon titre !')
root.geometry('800x500')

"""Ouverture du fichier comprenant l'image souhaité"""
my_pic = Image.open('pic/pic2.png')  # taille d'origine : 290x174

"""Redimensionnement de l'image"""
resized = my_pic.resize((580, 360), Image.ANTIALIAS)

"""Image redimensionnée dans une nouvelle variable"""
new_pic = ImageTk.PhotoImage(resized)

"""Insertion dans la fenêtre en tant qu'étiquette de résultat"""
my_label = tkinter.Label(root, image=new_pic)
my_label.pack(pady=20)

root.mainloop()
