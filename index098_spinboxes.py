"""
Tkinter - Codemy.com #98 : Spinboxes With TKinter
Lien : https://www.youtube.com/watch?v=FfYDWBdX-_s&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=98

Dans ce programme on créé un nouveau widget qui dispose d'un champ de saisie 
d'une ligne avec au bout de cette ligne, des flêches haut et bas

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x400')
        self.widgets()
        
    def widgets(self):
       
        """Création d'un spinbox : l'instruction 'from_' dispose d'un '_' 
        pour ne pas être confondu avec le 'from' dont on a un 
        exemple ci-dessus : 'from tkinter import *'"""
        my_spin = tkinter.Spinbox(root,
                        from_=0,  # départ de 0
                        to=10,  # arrivée à 10
                        increment=2,  # incrémentation de 2
                        justify='center',
                        font='Helvetica 20')
        my_spin.pack(pady=20)

        """Création d'un 2ème spinbox"""
        # déclaration d'une variable en tuple
        names = ('John', 'Albert', 'Machin')  
        self.my_spin2 = tkinter.Spinbox(root,
                        values=names,  # Affichage du tuple
                        justify='center',
                        font='Helvetica 20')
        self.my_spin2.pack(pady=20)

        """Configuration d'un bouton d'exécution"""
        # grab = saisir
        my_button = tkinter.Button(root, text='Soumettre', command=self.grab)  
        my_button.pack(pady=20)

        """Affichage du nom figurant dans le spinbox n° 2 : 
        configuration de l'étiquette dans la fonction grab()"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)
        
    def grab(self):
        """Méthode permettant d'afficher le nom apparaissant dans le spinbox n° 2"""
        
        self.my_label.config(text=self.my_spin2.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
