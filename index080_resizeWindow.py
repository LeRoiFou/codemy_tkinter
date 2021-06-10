"""
Tkinter - Codemy.com #80 : How To Resize A Window Dynamically 
Lien : https://www.youtube.com/watch?v=NytF3pJSMc8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=80 

Dans ce programme on apprend à redimensionner une fenêtre de manière dynamique 

Éditeur : Laurent REYNAUD 
Date : 11-12-20 
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('800x800')
        self.widgets()
        
    def widgets(self):
        
        """Configuration étiquette et champ de saisie pour saisir la largeur de la fenêtre"""
        width_label = tkinter.Label(root, text='Largeur : ')
        width_label.pack(pady=20)
        self.width_entry = tkinter.Entry(root, justify='center')
        self.width_entry.pack()

        """Configuration étiquette et champ de saisie pour saisir la hauteur de la fenêtre"""
        height_label = tkinter.Label(root, text='Hauteur : ')
        height_label.pack(pady=20)
        self.height_entry = tkinter.Entry(root, justify='center')
        self.height_entry.pack()

        """Configution du bouton d'exécution"""
        my_button = tkinter.Button(root, text='Redimensionner', command=self.resize)
        my_button.pack(pady=20)
        
    def resize(self):
        """Méthode permettant de redimensionner la fenêtre"""
        
        w = self.width_entry.get()
        h = self.height_entry.get()
        root.geometry(f'{w}x{h}')

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
