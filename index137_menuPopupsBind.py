"""
Tkinter - Codemy.com #137 : 
Right Click Menu Popups With Tkinter - Python Tkinter GUI Tutorial #137
Lien : https://www.youtube.com/watch?v=KRuUtNxOb_k&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=137

Dans ce programme on apprend à afficher le menu n'importe où 
dans la fenêtre en appuyant sur le bouton de droite de la souris

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x550')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Menu"""
        self.my_menu = tkinter.Menu(root, tearoff=0)
        self.my_menu.add_command(
            label='Dire bonjour', 
            command=self.hello)
        self.my_menu.add_command(
            label='Dire au revoir', 
            command=self.goodbye)
        self.my_menu.add_separator()
        self.my_menu.add_command(
            label='Quitter', 
            command=root.quit)

        """Bind avec le bouton de droite de la souris"""
        root.bind('<Button-3>', self.my_popup)

        """Etiquette"""
        self.my_label = tkinter.Label(
            root, 
            text='', 
            font='Helvetica 20')
        self.my_label.pack(pady=20)
        
    def hello(self):
        """Méthode affichant un message"""
        
        self.my_label.config(text='Salut !')

    def goodbye(self):
        """Méthode affichant un message"""
        
        self.my_label.config(text='Ciao !')

    def my_popup(self, e):
        """Méthode permettant d'afficher le menu dans la fenêtre 
        selon l'endroit où on a cliqué avec le bouton de droite de
        la souris"""
        
        self.my_menu.tk_popup(e.x_root, e.y_root)

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
