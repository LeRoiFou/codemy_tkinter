"""
Tkinter - Codemy.com # 205 : Bind Text From Textbox
Lien : https://www.youtube.com/watch?v=DAGNhLOTGzc

Dans ce programme on apprend à copier dans l'étiquette les saisies 
faites dans la zone de texte

Éditeur : Laurent REYNAUD
Date : 12-01-22
"""

import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Zone de texte & instruction bind")
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_text = tk.Text(
            root, 
            width=50, 
            height=20,
            font='Helvetica 12')
        self.my_text.pack(pady=20)    
        self.my_text.bind('<Key>', self.labeler)
        
        self.my_label = tk.Label(
            root, 
            text="Saisir quelque chose", 
            font='Helvetica 14')
        self.my_label.pack(pady=20)
        
    def labeler(self, e):
        "Copie dans l'étiquette de la saisie de la zone de texte"
        
        self.my_label.config(
            text=self.my_text.get(1.0, 'end' + '-1c') + e.char)
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
