"""
Tkinter - Codemy.com #140 : One Sided Widget Padding - Python Tkinter GUI Tutorial #140
Lien : https://www.youtube.com/watch?v=gX8Sm4PEOWE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=140

Dans ce programme on apprend à afficher deux étiquettes non pas l'une au-dessus de l'autre mais à côté de l'une de
l'autre.

On apprend que les instructions padx et  pady peuvent être configurés avec un tuple.
Exemple : pady(0, 50) signifie que le widget à un écart de 0 pixel au-dessus de lui et 50 pixels en dessous de lui

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')
root.config(bg='blue')

"""Message"""
my_label = Label(root, text='Salut !', bg='white', fg='black', font='Helvetica 20')
my_label.grid(row=0, column=0, pady=50, padx=(50, 20))

"""Message"""
my_label2 = Label(root, text='Salut bis !', bg='white', fg='black', font='Helvetica 20')
my_label2.grid(row=0, column=1)

root.mainloop()
