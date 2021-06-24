"""
Tkinter - Codemy.com #136 : 
New Transparent Widget Hack With Tkinter - Python Tkinter GUI Tutorial #136
Lien : https://www.youtube.com/watch?v=75jbNpc8vN4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=136

Dans ce programme on apprend à rendre transparent les widgets de la fenêtre
sans que cette dernière soit transparente

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        'Constructeur de la classe'
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x550')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Tous les fonds de couleur rouge des widgets rattachés
        à cette fenêtre, auront un fond transparent"""
        
        # 1ère possibilité :
        # root.wm_attributes('-transparentcolor', 'red')  
        
        # 2ème possibilité pour que les écritures soient lisibles :
        root.wm_attributes('-transparentcolor', root['bg'])  

        """Cadre"""
        my_frame = tkinter.Frame(root, width=200, height=200, bg='red')
        my_frame.pack(pady=20, ipady=20, ipadx=20)

        """Etiquette"""
        my_label = tkinter.Label(
            my_frame, 
            text='Salut !', 
            bg='red', 
            fg='white', 
            font='Helvetica 16')
        my_label.pack(pady=20)
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
