"""
Tkinter - Codemy.com #191 : Center Widgets With Place()
Lien : https://www.youtube.com/watch?v=SYrjAUFqPZU

Dans ce programme on apprend à centrer des widgets avec l'instruction
place() qui équivaut à pack() et grid()

Éditeur : Laurent REYNAUD
Date : 15-09-21
"""

import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Place !')
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        button_1 = tk.Button(root, text="Bouton 1", font="Helvetica 32")
        button_2 = tk.Button(root, text="Bouton 2", font="Helvetica 32")
        button_1.grid(column=0, row=0)
        button_2.grid(column=1, row=0)
        
        my_button = tk.Button(root, text="Clique-moi !", font="Helvetica 32")
        my_button.place(relx=0.5, rely=0.5, anchor='center') # centrage ;)
        # my_button.place(x=100, y=50) # pb d'emplacement avec cette instruction
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
