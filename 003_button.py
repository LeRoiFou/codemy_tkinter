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

from tkinter import *

root = Tk()


class Window(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.widgets()

    def widgets(self):
        """Fonction pour l'affichage d'un bouton d'exécution"""
        self.myButton = Button(self, text='Clique moi !', command=self.myClick, fg='blue', bg='#000000')
        self.myButton.pack()

    def myClick(self):
        """Fonction pour l'affichage du message"""
        self.myLabel = Label(self, text="Regarde ! J'ai cliqué sur le bouton !")
        self.myLabel.pack()


window = Window(root)
root.mainloop()
