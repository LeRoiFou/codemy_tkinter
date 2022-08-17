"""
All About The Button Widget - Tkinter Widget Library 1
Lien : https://www.youtube.com/watch?v=uJBFYyn12V4

Tout ! Tout ! Tout ! Vous serez tout sur le bouton !

Éditeur : Laurent REYNAUD
Date : 17-08-22
"""

import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Widget Button")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Define an image
        self.login = tk.PhotoImage(file='images/Login.png')
        
        self.my_button = tk.Button(root, 
            text="Click Me!",
            activebackground='black', # change de couleur de fond lorsqu'on clique sur le bouton
            activeforeground='red', # change la couleur du texte du bouton lorsqu'on clique dessus
            anchor='se', # direction du texte du bouton
            background ='yellow', # couleur du bouton
            bd=10, # largeur de la bordure du bouton
            command=self.clicker,
            font='helvetica 32',
            foreground='green', # couleur du texte
            height=2, # hauteur du bouton
            # image=self.login, # ne marche que si l'instruction 'height' est neutralisée
            justify='left', # à utiliser avec l'instruction 'wraplength'
            overrelief='flat', # change le relief du bouton lors du passage de la souris sur le bouton
            relief='ridge',
            state=tk.NORMAL,
            underline=4, # n° du caractère souligné
            width=20, # largeur du bouton
            wraplength=0 # ajustement du texte dans le widget button
        )
        self.my_button.pack(pady=50)
        
    def clicker(self):
        
        self.my_button.config(text="You clicked the button!")

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
