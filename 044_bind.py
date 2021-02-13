"""
Tkinter - Codemy.com #44 : Keyboard Event Binding With tKinter
Lien : https://www.youtube.com/watch?v=GLnNPjL1U2g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=44

L'instruction bind permet de recourir aux touches du clavier ou aux fonctions de la souris. Elle est paramétrée de deux
arguments : <évènement>, action

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")


def clicker(event):
    # myLabel = Label(root, text='Tu as cliqué sur le bouton ' + str(   event.x) + ' ' + str(event.y))  # coord x, y
    # myLabel = Label(root, text='Tu as tappé la touche ' + event.char)  # caractères uniquement pour l'event <Key>
    myLabel = Label(root, text='Tu as tappé la touche ' + event.keysym)  # Toutes les touches pour l'event <Key>
    myLabel.pack()


myButton = Button(root, text='Clique-moi !')
# myButton.bind('<Button-3>', clicker)  # action réalisée lors du clique droit de la souris sur le bouton
# myButton.bind('<Enter>', clicker)  # action réalisée lors du passage de la souris sur le bouton
# myButton.bind('<Leave>', clicker)  # action réalisée au moment où le bouton est laché après avoir cliqué dessus
# myButton.bind('<FocusIn>', clicker)  # action réalisée clique gauche de la souris : documentation widget affiché
# myButton.bind('<Return>', clicker)  # action avec TAB + ENTREE du clavier : coordonnée de la souris sur la fenêtre
myButton.bind('<Key>', clicker)  # action avec touche du clavier : affichage de la touche appuyée
myButton.pack(pady=20)

root.mainloop()
