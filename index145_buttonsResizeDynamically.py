"""
Tkinter - Codemy.com #145 : 
Dynamically Resize Buttons When Resizing a Window - 
Python Tkinter GUI Tutorial #145
Lien : https://www.youtube.com/watch?v=rZxOe1kVF8Q&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=145

Dans ce programme on apprend à redimensionner dynamiquement 
les boutons avec les dimensions de la fenêtre

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration des boutons avec la méthode grid()"""
        
        # configuration de la ligne 0 pour le bouton n° 1
        # Grid.rowconfigure(root, index=0, weight=1)  
        
        # configuration de la ligne 1 pour le bouton n° 2
        # Grid.rowconfigure(root, index=1, weight=1)   
        
        # configuration de la colonne 0 pour les boutons
        tkinter.Grid.columnconfigure(root, index=0, weight=1)  

        """Création des boutons"""
        button_1 = tkinter.Button(root, text='Bouton n° 1')
        button_2 = tkinter.Button(root, text='Bouton n° 2')
        button_3 = tkinter.Button(root, text='Bouton n° 3')
        button_4 = tkinter.Button(root, text='Bouton n° 4')

        """Assignation des boutons dans une liste"""
        button_list = [button_1, button_2, button_3, button_4]

        """Assignation d'un compteur"""
        row_number = 0

        """Parcours de la liste et configuration 
        automatique de chaque ligne"""
        for button in button_list:
            tkinter.Grid.rowconfigure(
                root, 
                index=row_number, 
                weight=1)  # configuration de chaque ligne
            row_number += 1  # incrémentation

        """Affichage des boutons"""
        # sticky = étalement du bouton sur toute la longueur et la largeur
        button_1.grid(row=0, column=0, sticky='nsew')  
        button_2.grid(row=1, column=0, sticky='nsew')
        button_3.grid(row=2, column=0, sticky='nsew')
        button_4.grid(row=3, column=0, sticky='nsew')
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
