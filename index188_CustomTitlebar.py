"""
Tkinter - Codemy.com #188 : Custom Titlebar Hack!
Lien :https://www.youtube.com/watch?v=s0cpxPSN4k4

Dans ce programme on change la couleur de la barre de titre
qui est par défaut de couleur blanche

Éditeur : Laurent REYNAUD
Date : 24-08-21
"""

import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Barre customisée ;)')
        root.geometry('500x300')
        
        # Suppression de la barre de titre par défaut
        root.overrideredirect(True)
        
        self.widgets()
        
    def move_app(self, e):
        "Déplacement de la fenêtre principale"
        
        root.geometry(f'+{e.x_root}+{e.y_root}')
        
    def quitter(self, e):
        "Fermeture de la fenêtre avec le faux icône 'X'"
        
        root.quit()
        # root.destroy()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Fausse cadre de la barre de titre
        title_bar = tk.Frame(root, bg='darkgreen', relief='raised', bd=0)
        title_bar.pack(expand=1, fill='x')
        
        # Déplacement de la fenêtre principale
        title_bar.bind('<B1-Motion>', self.move_app)
        
        # Titre de la fausse barre de titre
        title_label = tk.Label(title_bar, text='Mon titre voyons !', bg='darkgreen', fg='white')
        title_label.pack(side='left', pady=2)
        
        # Icône 'X' pour fermer la fenêtre sur la fausse barre de titre
        close_label = tk.Label(title_bar, text='      X      ', bg='darkgreen', fg='white', relief='raised', bd=1)
        close_label.pack(side='right', pady=4)
        close_label.bind('<Button-1>', self.quitter)
        
        # Bouton pour fermer la fenêtre
        my_button = tk.Button(
            root, 
            text='Fermer!', 
            font='Helevetica, 32', 
            command=root.quit)
        my_button.pack(pady=100)

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
