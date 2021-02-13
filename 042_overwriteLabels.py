"""
Tkinter - Codemy.com #42 : overwrite grid labels
Lien : https://www.youtube.com/watch?v=Q-rRF6c8kJM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=42

Dans ce programme, on supprime le bouton effacer, il n'y a qu'un seul bouton qui permet d'afficher la saisie et pour
toute nouvelle saisie, le widget étiquette remplace la donnée affichée précedemment par la nouvelle donnée

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")

myLabel = Label(root)  # déclaration de la variable sinon la variable myLabel est considérée comme non définie


def myClick():
    """Affichage des données saisies"""
    global myLabel
    myLabel.destroy()  # cette instruction permet d'effacer intégralement les données précédemment affichées
    hello = 'Bonjour ' + myEntry.get()
    myLabel = Label(root, text=hello)
    myEntry.delete(0, END)  # lorsqu'on appuie sur le bouton 'Entrez votre nom' le champ de saisie est réinitialisé
    myLabel.grid(row=3, column=0, pady=10)


# def myDelete():
#     """Suppression des données saisies"""
#     myLabel.grid_forget()
#     myButton['state'] = NORMAL


myEntry = Entry(root, width=17, font='Helvetica 30', justify='center')
myEntry.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text='Entrez votre nom', command=myClick)
myButton.grid(row=1, column=0, pady=10)

# deleteButton = Button(root, text='Supprimer le texte', command=myDelete)
# deleteButton.grid(row=2, column=0,pady=10)

root.mainloop()
