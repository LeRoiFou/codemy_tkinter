"""
Tkinter - Codemy.com #196 : Connect One Scrollbar To Multiple TextBoxes
Lien : https://www.youtube.com/watch?v=s9OswEmRmgU

Dans ce programme on créé une barre de défilement connectée avec 2 widgets

Éditeur : Laurent REYNAUD
Date : 03/11/21
"""

import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Connecter la barre de défilement')
        root.geometry('600x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Cadre
        my_frame = tk.Frame(root)
        my_frame.pack(pady=20)
        
        # Barre de défilement
        text_scroll = tk.Scrollbar(my_frame)
        text_scroll.pack(
            side='right', fill='y')
        
        # 2 zones de textes
        self.my_text1 = tk.Text(
            my_frame, width=20, 
            height=25, 
            font='Helvetica 16',
            yscrollcommand=text_scroll.set,
            wrap='none')
        self.my_text1.pack(
            side='right', padx=5)
        self.my_text2 = tk.Text(
            my_frame, width=20,
            height=25, 
            font='Helvetica 16',
            yscrollcommand=text_scroll.set,
            wrap='none')
        self.my_text2.pack(
            side='left', padx=5)
        
        # Configuration de la barre de défilement
        text_scroll.config(command=self.multiple_yview)
        
    def multiple_yview(self, *args):
        "Lien de la barre de défilement avec les zones de textes"
        
        # Lien de la barre avec les 2 zones de textes
        self.my_text1.yview(*args)
        self.my_text2.yview(*args)
        # print(*args) -> *args donne la coordonnée de la zone de texte

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
