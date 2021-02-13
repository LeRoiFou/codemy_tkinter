"""
Tkinter - Codemy.com #48 : Paned Windows
Lien : https://www.youtube.com/watch?v=9Hyltpk2tSM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=48

Ce programme permet d'agrandir ou de diminuer des cadres dans une fenêtre

Éditeur : Laurent REYNAUD
Date : 29-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")

# Configuration du panneau de fenêtre qui s'étendra sur toute la fenêtre
panel_1 = PanedWindow(bd=4, relief='raised', bg='red')
panel_1.pack(fill=BOTH, expand=1)  # extension sur toute la longueur et la largeur de la fenêtre
left_label = Label(panel_1, text='Panneau gauche')
panel_1.add(left_label)

# Configuration de deux panneaux qui sont à l'intérieur du panneau ci-dessus
# Panneau haut
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief='raised', bg='blue')
panel_1.add(panel_2)
top = Label(panel_2, text='Panneau du haut')
panel_2.add(top)
# Panneau bas
bottom = Label(panel_2, text='Panneau du bas')
panel_2.add(bottom)

root.mainloop()
