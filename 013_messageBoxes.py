"""
Tkinter - Codemy.com #13 : boîte à message (message boxes)
Lien : https://www.youtube.com/watch?v=S3AaSwpb5GE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=13

Ce programme permet d'afficher un message à titre informatif...
On peut également afficher un message d'alerte, d'interdiction, d'interrogation...

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Apprendre à coder avec Codemy.com')


def popup():
    response = messagebox.askquestion("C'est mon info ;)", 'Bonjour !')
    Label(root, text=response).pack()
    if response == 'yes':
        Label(root, text='Tu as cliqué oui !!!').pack()
    else:
        Label(root, text='Tu as cliqué non !!!').pack()


Button = Button(root, text='Information', command=popup).pack()

root.mainloop()
