"""
Tkinter - Codemy.com #71 : Drag and Drop Images With The Mouse
Lien : https://www.youtube.com/watch?v=Z4zePg2M5H8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=71

Dans ce programme on déplace une image avec canvas à l'aide de la souris

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('800x600')

"""Tailles et coordonnées en variables"""
w = 600
h = 400
x = w // 2
y = h // 2

"""Configuration d'un canvas sous fond blanc"""
my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

"""Chargement de l'image au format .png et ajout au canvas"""
img = PhotoImage(file='Images/shrek.png')
my_image = my_canvas.create_image(260, 125, anchor=NW, image=img)  # centrage de l'image au canvas


def move(event):
    """Déplacement de l'image avec la souris + coordonnées de la souris"""
    global img  # si on ne passe pas la variable en globale, l'image ne se déplace pas avec la souris
    img = PhotoImage(file='Images/shrek.png')
    my_image = my_canvas.create_image(event.x, event.y, image=img)  # anchor enlevé pour éviter le décalage souris/image
    my_label.config(text='Coordonnées x : ' + str(event.x) + ' et y : ' + str(event.y))


"""Configuration étiquette résultat"""
my_label = Label(root, text='')
my_label.pack(pady=20)

"""Configuration de la souris"""
my_canvas.bind('<B1-Motion>', move)  # déplacement avec la souris en maintenant le bouton gauche
# my_canvas.bind('<Motion>', move)  # déplacement avec la souris
# my_canvas.bind('<B3-Motion>', move)  # déplacement avec la souris en maintenant le bouton de droite

root.mainloop()
