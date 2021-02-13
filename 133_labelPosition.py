"""
Tkinter - Codemy.com #133 : How To Position Label Text The Right Way - Python Tkinter GUI Tutorial #133
Lien : https://www.youtube.com/watch?v=05wbBHY3YMc&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=133

Dans ce programme on apprend à positionner une étiquette : centrée, alignée à droite, alignée à gauche

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')

"""Etiquette 1 centrée"""
my_label1 = Label(root,
                  text='Machin\nMachin Machin\nMachin Machin Machin',
                  font='Helvetica 18',
                  bd=1,
                  relief='sunken')
my_label1.pack(pady=20, ipady=10, ipadx=10)

"""Etiquette 2 alignée à gauche"""
my_label2 = Label(root,
                  text='Machin\nMachin Machin\nMachin Machin Machin',
                  font='Helvetica 18',
                  bd=1,
                  relief='sunken',
                  justify='left')
my_label2.pack(pady=20, ipady=10, ipadx=10)

"""Etiquette 3 alignée à droite"""
my_label3 = Label(root,
                  text='Machin\nMachin Machin\nMachin Machin Machin',
                  font='Helvetica 18',
                  bd=1,
                  relief='sunken',
                  justify='right')
my_label3.pack(pady=20, ipady=10, ipadx=10)

root.mainloop()
