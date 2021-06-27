"""
Tkinter - Codemy.com #161 : 
On/Off Button Switch - Python Tkinter GUI Tutorial #161
Lien : https://www.youtube.com/watch?v=n1ucrkly2nc

Dans ce programme on apprend à afficher un bouton interrupteur
'on' / 'off'. Pour cela, on a recours au booléen.

Éditeur : Laurent REYNAUD
Date : 12-01-21
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x300')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Assignation d'un booléen pour le bouton lorsqu'il est sur 'on'"""
        self.is_on = True  # à l'origine, le bouton 'on' est 'True'
        
        """"Configuration de l'étiquette"""
        self.my_label = tkinter.Label(
            root, 
            text="L'interrupteur allumé !", 
            fg='green', 
            font='Helvetica 32')
        self.my_label.pack(pady=20)

        """Configuration de l'image"""
        self.on = tkinter.PhotoImage(file='images/on.png')
        self.off = tkinter.PhotoImage(file='images/off.png')

        """Configuration du bouton"""
        self.on_button = tkinter.Button(
            root, 
            image=self.on, 
            bd=0, 
            command=self.switch)
        self.on_button.pack(pady=50)
        
    def switch(self):
        """Méthode permettant de changer l'interrupteur on / off"""

        """Déterminé si c'est sur 'on' ou sur 'off'"""
        
        # si c'est sur 'on'
        if self.is_on:  
            
            # en appuyant sur le bouton celui-ci est sur 'off'
            self.on_button.config(image=self.off)  
            
            # cette fois-ci le bouton 'on' est 'False'
            self.is_on = False  
            
            # on change le texte
            self.my_label.config(text='Interrupteur éteint !', fg='grey')  
        
        else:
            
            # sinon le bouton est sur 'on'
            self.on_button.config(image=self.on)  
            
            # cette fois-ci le bouton 'on' est 'True'
            self.is_on = True  
            
            # on change le texte
            self.my_label.config(text='Interrupteur allumé !', fg='green')  


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
