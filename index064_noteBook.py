"""
Tkinter - Codemy.com #64 : Create tabs in your GUI interface using Notebook
Lien : https://www.youtube.com/watch?v=kqbkUKIc1Gk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=64

Ce widget Notebook permet d'avoir des onglets à la fenêtres qui sont situés en haut à l'inverse d'Excel et de Calc

Éditeur : Laurent REYNAUD
Date : 08-12-20
"""

import tkinter
from tkinter import ttk

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('500x500')
        self.widgets()

    def widgets(self):

        # Configuration des onglets
        self.my_notebook = ttk.Notebook(root)
        self.my_notebook.pack()

        # Configuration des cadres"""
        my_frame1 = tkinter.Frame(self.my_notebook, width=500, height=500, bg='blue')
        self.my_frame2 = tkinter.Frame(self.my_notebook, width=500, height=500, bg='red')

        # Affichage des cadres sur toute la longueur et la largeur configurée ci-avant
        my_frame1.pack(fill='both', expand=1)
        self.my_frame2.pack(fill='both', expand=1)

        # Ajout des onglets
        self.my_notebook.add(my_frame1, text='Onglet bleu')
        self.my_notebook.add(self.my_frame2, text='Onglet rouge')

        # Configuration de boutons
        my_button = tkinter.Button(
            my_frame1,
            text="Cacher l'onglet n° 2", 
            command=self.hide).pack(pady=15)
        my_button2 = tkinter.Button(
            my_frame1, 
            text="Montrer l'onglet n° 2", 
            command=self.show).pack(pady=15)
        my_button3 = tkinter.Button(
            my_frame1, 
            text="Aller à l'onglet n° 2", 
            command=self.select).pack(pady=15)

    def hide(self):
        # Permet de cacher l'onglet 2 situé à l'index 1

        # (1) -> index 1 qui est l'onglet n° 2 (l'onglet n° 1 est à l'index 0)
        self.my_notebook.hide(1)  

    def show(self):
        # Permet de remontrer l'onglet 2 caché

        self.my_notebook.add(self.my_frame2, text='Onglet rouge')

    def select(self):
        # Permet d'accéder à l'onglet n° 2 situé à l'index 1

        self.my_notebook.select(1)

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
