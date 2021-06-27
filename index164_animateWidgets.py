"""
Tkinter - Codemy.com #164 : 
How To Animate Widgets - Python Tkinter GUI Tutorial #164
Lien : https://www.youtube.com/watch?v=kvd6i1mXec8

Dans ce programme on apprend à animer des widgets -> 
similaire à kivy dans le tuto 36_Animation.
Mais avec tkinter, animer des widgets est plus compliqué que sur kivy...
question self.posé sur youtube : self.possibilité de
rajouter une deuxième commande pour un même widget ?

Éditeur : Laurent REYNAUD
Date : 27-01-21
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('700x600')
        
        """Assignation d'une variable pour : 
        -> le nombre d'évènements  
        -> la taille de police d'écriture"""
        self.count = 0
        self.size = 26
        self.pos = 100
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Création d'un bouton"""
        self.my_button = tkinter.Button(
            root, 
            text='Clique-moi !', 
            command=self.expand, 
            font='Helvetica 24', 
            fg='red')
        self.my_button.pack(pady=100)
        
    def contract(self):
        """Méthode permettant de rediminuer la police d'écriture du bouton : 
        elle s'exécute après la fonction expand()"""

        # self.count = 9, self.size = 36, self.pos = 109

        if 10 >= self.count > 0:
            
            # tant que le nombre d'évènements <= 10 
            # la taille d'écriture s'incrémente de -2
            self.size -= 2  
            
            # changement de la taille d'écriture du bouton
            self.my_button.config(font=('Helvetica', self.size))  
            
            # changement de la self.position du bouton
            self.my_button.pack_configure(pady=self.pos) 
            
            # incrémentation du nombre d'évènements de -1 
            self.count -= 1  
            
            # incrémentation de la self.position du widget de -20
            self.pos -= 20  
            
            # changement de la fenêtre principale toute les milli-secondes
            root.after(10, self.contract)  

    def expand(self):
        """Méthode permettant d'agrandir la police d'écriture du bouton"""
        
        # self.count = 0, self.size = 26, self.pos = 100

        if self.count < 10:
            
            # tant que le nombre d'évènements < 10 
            # la taille d'écriture s'incrémente de +2
            self.size += 2  
            
            # changement de la taille d'écriture du bouton
            self.my_button.config(font=('Helvetica', self.size))  
            
            # changement de la self.position du bouton
            self.my_button.pack_configure(pady=self.pos)  
            
            # incrémentation du nombre d'évènements de +1
            self.count += 1  
            
            # incrémentation de la self.position du widget de +20
            self.pos += 20  
            
            # changement de la fenêtre principale toute les milli-secondes
            root.after(10, self.expand)  

        elif self.count == 10:
            self.contract()
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
