"""
Tkinter - Codemy.com #17 : checkboxes 
Lien : https://www.youtube.com/watch?v=4IsLwwb_yDs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=17  

Dans ce programme on apprend à afficher une coche d'option 

Éditeur : Laurent REYNAUD  
Date : 05-11-2020  
"""

from tkinter import *

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.geometry('400x400')

var = StringVar()

c = Checkbutton(root, text='Cochez cette case, je vous défie', variable=var, onvalue='Pizza', offvalue='Hamburger')
c.deselect()  # Réponse 'off' ou 'on' dès la première ligne
c.pack()


def show():
    my_label = Label(root, text=var.get())
    my_label.pack()


my_btn = Button(root, text='Montrer la sélection', command=show)
my_btn.pack()

root.mainloop()
