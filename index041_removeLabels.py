"""
Tkinter - Codemy.com #41 : Remove labels
Lien : https://www.youtube.com/watch?v=2_qUokpB1fw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=41

Dans ce programme, on supprime les données affichées des étiquettes tout en évitant de lister toutes les données saisies

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter

class GUI:

    def __init__(self, root):
        self.root = root
        root.geometry('400x400')
        root.title("Titre !")
        self.widgets()

    def widgets(self):

        self.myEntry = tkinter.Entry(root, width=50, font='Helvetica 30', justify='center')
        self.myEntry.pack(padx=10, pady=10)

        self.myButton = tkinter.Button(root, text='Entrez votre nom', command=self.myClick)
        self.myButton.pack(pady=10)

        deleteButton = tkinter.Button(root, text='Supprimer le texte', command=self.myDelete)
        deleteButton.pack(pady=10)

    def myClick(self):
        # Affichage des données saisies
        
        hello = 'Bonjour ' + self.myEntry.get()
        self.myLabel = tkinter.Label(root, text=hello)
        self.myEntry.delete(0, 'end')
        self.myLabel.pack(pady=10)
        self.myButton['state'] = 'disabled'  # le bouton 'Entrez votre nom' devient inactif après l'avoir appuyé

    def myDelete(self):
        # Suppression des données saisies
        
        self.myLabel.pack_forget()
        self.myButton['state'] = 'normal'  # en appuyant sur le bouton supprimer, le bouton 'Entrez votre nom' redevient actif


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()