"""
Tkinter - Codemy.com #41 : Remove labels
Lien : https://www.youtube.com/watch?v=2_qUokpB1fw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=41

Dans ce programme, on supprime les données affichées des étiquettes tout en évitant de lister toutes les données saisies

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")


def myClick():
    """Affichage des données saisies"""
    global myLabel
    hello = 'Bonjour ' + myEntry.get()
    myLabel = Label(root, text=hello)
    myEntry.delete(0, END)
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED  # le bouton 'Entrez votre nom' devient inactif après l'avoir appuyé


def myDelete():
    """Suppression des données saisies"""
    myLabel.pack_forget()
    myButton['state'] = NORMAL  # en appuyant sur le bouton supprimer, le bouton 'Entrez votre nom' redevient actif


myEntry = Entry(root, width=50, font='Helvetica 30', justify='center')
myEntry.pack(padx=10, pady=10)

myButton = Button(root, text='Entrez votre nom', command=myClick)
myButton.pack(pady=10)

deleteButton = Button(root, text='Supprimer le texte', command=myDelete)
deleteButton.pack(pady=10)

root.mainloop()
