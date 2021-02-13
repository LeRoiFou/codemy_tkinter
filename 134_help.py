"""
Tkinter - Codemy.com #134 : How To Unlock The Hidden Keys Of A Widget - Python Tkinter GUI Tutorial #134
Lien : https://www.youtube.com/watch?v=68TIx0RJMow&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=134

Avec l'instruction 'widget'.keys on dispose de toutes les méthodes prédéfinies pour le widget concerné

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x550')

"""Etiquette"""
my_label = Label(root, text='Mon message', font='Helvetica 18')
my_label.pack(pady=20)

"""Affichage de toutes les méthodes prédéfinies pour le widget label"""
for key in my_label.keys():
    print(key)

root.mainloop()
