"""
Tkinter - Codemy.com #3 : création de boutons
Lien : https://www.youtube.com/watch?v=yuuDJ3-EdNQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=3

Dans ce programme on apprend à afficher un bouton d'exécution

À titre d'information :
-> padx : le widget fait la largeur de la fenêtre
-> pady : le widget fait la hauteur de la fenêtre

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

import tkinter


class GUI:

    def __init__(self, root):
        self.root = root
        self.widgets()

    def widgets(self):
        # Fonction pour l'affichage d'un bouton d'exécution
        self.myButton = tkinter.Button(
            root,
            text='Clique moi !', 
            command=self.myClick, 
            fg='blue',
            bg='#000000')
        self.myButton.pack()

    def myClick(self):
        # Fonction pour l'affichage du message
        self.myLabel = tkinter.Label(
            root,
            text="Regarde ! J'ai cliqué sur le bouton !")
        self.myLabel.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
