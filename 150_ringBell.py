"""
Tkinter - Codemy.com #150 : How To Ring The System Bell - Python Tkinter GUI Tutorial #150
Lien : https://www.youtube.com/watch?v=jBhDWcQRyu4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=150

Dans ce programme on apprend à faire sonner le son d'une cloche lorsqu'on appuye sur le bouton d'exécution

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')


def ring():
    """Fonction permettant de faire sonner une cloche en appuyant sur le bouton d'exécution"""
    root.bell()


"""Définition de l'image"""
bell = PhotoImage(file='images/bell.png')

"""Ajout de l'image à la fenêtre"""
bell_label = Label(root, image=bell)
bell_label.pack(pady=20)

"""Ajout d'un bouton"""
my_button = Button(root, text='Sonner la cloche !', command=ring, font='Helvetica 24', fg='#4d4d4d')
my_button.pack(pady=20)

root.mainloop()
