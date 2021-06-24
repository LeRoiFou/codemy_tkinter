"""
Tkinter - Codemy.com #132 : 
Secret Label Copying Hack - Python Tkinter GUI Tutorial #132
Lien : https://www.youtube.com/watch?v=JB7ZwypM9hk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=132

Dans ce programme on apprend à copier une étiquette : 
par principe on ne peut pas copier une étiquette, à la différence
d'un champ de saisi.
Pour cela, la 2ème étiquette dans ce programme sera en réalité 
un champ de saisi

Éditeur : Laurent REYNAUD
Date : 24-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x350')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Etiquette"""
        my_label = tkinter.Label(
            root, 
            text='Etiquette 1', 
            font='Helvetica 20')
        my_label.pack(pady=20)

        """Variable de contrôle"""
        my_text = tkinter.StringVar()
        my_text.set('Etiquette 2')

        """Champ de saisi"""
        # bd=0 : suppression de la bordure
        # state = readonly : suppression du champ de saisi de couleur blanc
        # textvariable=my_text : insertion du texte dans le champ de saisi
        my_entry = tkinter.Entry(root,
                        justify='center',
                        font='Helvetica 20',
                        bd=0,  
                        state='readonly',  
                        textvariable=my_text  
                        )
        my_entry.pack(pady=20)
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
    