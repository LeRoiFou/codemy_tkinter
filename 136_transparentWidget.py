"""
Tkinter - Codemy.com #136 : New Transparent Widget Hack With Tkinter - Python Tkinter GUI Tutorial #136
Lien : https://www.youtube.com/watch?v=75jbNpc8vN4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=136

Dans ce programme on apprend à rendre transparent les widgets de la fenêtre sans que cette dernière soit transparente

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')

"""Tous les fonds de couleur rouge des widgets rattachés à cette fenêtre, auront un fond transparent"""
# root.wm_attributes('-transparentcolor', 'red')  # 1ère possibilité
root.wm_attributes('-transparentcolor', root['bg'])  # 2ème possibilité pour que les écritures soient lisibles

"""Cadre"""
my_frame = Frame(root, width=200, height=200, bg='red')
my_frame.pack(pady=20, ipady=20, ipadx=20)

"""Etiquette"""
my_label = Label(my_frame, text='Salut !', bg='red', fg='white', font='Helvetica 16')
my_label.pack(pady=20)

root.mainloop()
