"""
Tkinter - Codemy.com #11 : les cadres (frame)
Lien : https://www.youtube.com/watch?v=_auZ8TTkojQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11

Dans ce programme on apprend à insérer des widgets dans un cadre

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.iconbitmap('images/homer.ico')

frame = LabelFrame(root, text="C'est mon cadre...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text='Ne pas cliquer !')
b2 = Button(frame, text='... ni sur ce bouton !')
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
