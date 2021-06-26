"""
Tkinter - Codemy.com #146 : 
How To Dynamically Resize Button Text - Python Tkinter GUI Tutorial #146
Lien : https://www.youtube.com/watch?v=m4Oo1crYZTM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=146

Dans ce programme en plus de changer dynamiquement les dimensions 
d'un bouton par rapport aux dimensions de la fenêtre,
on change également de manière dynamique le texte du bouton

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        'Constructeur de la classe'
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration du bouton avec la méthode grid()"""
         # configuration de la ligne 0
        tkinter.Grid.rowconfigure(root, index=0, weight=1) 
        # configuration de la colonne 0
        tkinter.Grid.columnconfigure(root, index=0, weight=1)  

        """Configuration du bouton"""
        self.button_1 = tkinter.Button(root, text='Bouton n° 1 !')
        self.button_1.grid(row=0, column=0, sticky='nsew')

        """Liaison avec l'application"""
        # 'configure' permet de prendre en compte les dimensions du widget
        root.bind('<Configure>', self.resize)  
        
    def resize(self, e):
        """Méthode permettant de lier les dimensions du texte 
        avec le bouton associé"""

        """Taille de la fenêtre divisé par 10 pixels"""
        size = e.width / 10

        """Changement de la taille de l'écriture du bouton"""
        self.button_1.config(font=('Helvetica', int(size)))


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
