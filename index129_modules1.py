"""
Tkinter - Codemy.com #129 : 
Using Other Python Programs In Your Tkinter App 
- Python Tkinter GUI Tutorial #129
Lien : https://www.youtube.com/watch?v=KCWWL54He_g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=129

Dans ce programme on apprend à créer des modules personnalisés 
pour alléger le programme établi sur un seul fichier

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

import tkinter
# import du module personnalisé
from index129_modules2 import name_it

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Titre !')
        root.geometry('500x350')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Champ de saisi"""
        self.my_box = tkinter.Entry(root, justify='center')
        self.my_box.pack(pady=20)

        """Affichage du message"""
        self.my_label = tkinter.Label(root, text='', font='Helvetica 18')
        self.my_label.pack(pady=20)

        """Bouton"""
        my_button = tkinter.Button(
            root, 
            text='Afficher nom', 
            command=self.submit)
        my_button.pack(pady=20)
        
    def submit(self):
        """Méthode appelant la fonction du fichier index129_modules2, 
        qui complète la phrase avec le texte rédigé dans le champ de saisi"""
        
        # assignation de la phrase à afficher avec la fonction nameit()
        greet = name_it(self.my_box.get())  
        
        # configuration du message à afficher
        self.my_label.config(text=greet)  
        
        
if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
