"""
Tkinter - Codemy.com #51 : Unicode Characters & Special Characters
Lien : https://www.youtube.com/watch?v=b_8sPENjHw4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=51

Dans ce programme on insère des caractères spéciaux à partir de la table des caractères Unicode
Voir : https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode_(0000-0FFF) pour la liste des caractères

Éditeur : Laurent REYNAUD
Date : 30-11-2020
"""

import tkinter

root = tkinter.Tk()
root.geometry('400x400')
root.title("Titre !")

my_label = tkinter.Label(root, text='41' + u'\u00A9', font='Helvetica 22').pack(pady=10)  # affichage : 41©
my_label2 = tkinter.Label(root, text='41' + u'\u00AE', font='Helvetica 22').pack(pady=10)  # affichage : 41®
my_button = tkinter.Button(root, text=u'\u00BB', font='Helvetica 22').pack(pady=10)

root.mainloop()
