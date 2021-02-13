"""
Tkinter - Codemy.com #85 : Button Mouse On-Hover Popup Message
Lien : https://www.youtube.com/watch?v=o_YumT2iWBc&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=85

Dans ce programme, qu'on la souris survole le bouton, celui-ci change de couleur et un message (explicatif du bouton)
apparaît en bas à droite de la fenêtre

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('500x400')


def button_hover(event):
    """Fonction s'exécutant lorsque la souris survole le bouton d'exécution"""
    my_button['bg'] = 'white'  # le bouton change de couleur
    status_label.config(text='Je suis en train de survoler le bouton !')  # un message popup s'affiche en bas à droite


def button_hover_leave(event):
    """Fonction permettant de réinitialiser la couleur du bouton ainsi que la suppression du message popup"""
    my_button['bg'] = 'SystemButtonFace'  # réinitialisation de la couleur du bouton
    status_label.config(text='')  # suppression du message popup


"""Configuration du bouton d'exécution"""
my_button = Button(root, text='Survole moi !', font='Helvetica 28')
my_button.pack(pady=50)

"""Configuration du renvoi de texte situé en bas à droite de la fenêtre"""
status_label = Label(root, text='', bd=1, relief=SUNKEN, anchor=E)  # bordure avec ancrage à droite
status_label.pack(fill=X, side=BOTTOM, ipady=2)  # expansion sur toute la largeur en bas de la fenêtre

"""Lien avec la souris et tkinter"""
my_button.bind('<Enter>', button_hover)  # souris survolant le bouton
my_button.bind('<Leave>', button_hover_leave)  # souris ne survolant plus le bouton

root.mainloop()
