"""
Tkinter - Codemy.com #38 : Entry et hauteur
Lien : https://www.youtube.com/watch?v=XuNKxXS3Sdc&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=38

Dans ce programme on apprend à augmenter la hauteur d'un champ de saisi (widget Entry)

L'instruction 'height' (hauteur) ne fonctionne pas pour le widget Entry : on ne peut que modifier la largeur d'un Entry
Solutions :
-> Augmenter la taille de la police avec l'instruction 'font'
-> Recourir à l'instruction 'ipady'

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter

root = tkinter.Tk()
root.geometry('400x200')
root.title("Titre !")


def myClick():
    hello = 'Bonjour ' + myEntry.get()
    myLabel = tkinter.Label(root, text=hello)
    myEntry.delete(0, 'end')
    myLabel.pack(pady=10)


myEntry = tkinter.Entry(root, width=50, font='Arial 20', justify='center')
myEntry.pack(padx=10, pady=10, ipady=20)

myButton = tkinter.Button(root, text='Entrez votre nom', command=myClick)
myButton.pack(pady=10)

root.mainloop()