"""
Tkinter - Codemy.com #167 : 
How To Resize Your App With The Sizegrip Widget 
- Python Tkinter GUI Tutorial #167
Lien : https://www.youtube.com/watch?v=8lkyOGUhK8Q

Dans ce programme on apprend à redimensionner la fenêtre principale
avec un nouveau widget : sizegrip
Cela permet de pouvoir redimensionner à l'intérieur de la fenêtre... 
pas trop d'utilité...

Éditeur : Laurent REYNAUD
Date : 19-02-2021
"""

import tkinter
from tkinter import ttk  # pour le nouveau widget sizegrip

root = tkinter.Tk()
root.title('Resize the app with the sizegrip widget')
root.geometry('400x300')
root.resizable(True, True)  # pour qu'on puisse redimensionner la fenêtre

"""Création d'un cadre pour les widgets ci-après"""
my_frame2 = tkinter.Frame(root,
                  highlightbackground='gray',  # couleur du contour du cadre
                  highlightthickness=1  # épaisseur du contour du cadre
                  )
my_frame2.pack(pady=20)

"""Configuration de l'étiquette"""
my_label = tkinter.Label(my_frame2, text='Hello world !', font='Helvetica 32')
my_label.pack(pady=50, padx=20)

"""Configuration du nouveau widget sizegrip 
sous la forme d'un petit triangle"""
my_sizegrip2 = ttk.Sizegrip(my_frame2)
my_sizegrip2.pack(
    side='right',  # widget situé à droite de la barre de statut
    anchor='se'  # widget ancré en bas à droite de la barre de statut
                  )

# """Reconfiguration des lignes et des colonnes de l'instruction .grid()"""
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

"""Création d'une barre de statut"""
my_frame = tkinter.Frame(root,
                 highlightbackground='gray',  # couleur du contour du cadre
                 highlightthickness=1  # épaisseur du contour du cadre
                 )
my_frame.pack(
    side='bottom',  # cadre situé en bas de la fenêtre principale
    fill='x'  # cadre 'étalé' sur toute la longueur de la fenêtre principale
              )

"""Configuration du nouveau widget sizegrip sous la forme 
d'un petit triangle"""
my_sizegrip = ttk.Sizegrip(my_frame)
my_sizegrip.pack(
    side='right',  # widget situé à droite de la barre de statut
    anchor='se'  # widget ancré en bas à droite de la barre de statut
                 )
# my_sizegrip.grid(row=1, sticky=SE)


root.mainloop()
