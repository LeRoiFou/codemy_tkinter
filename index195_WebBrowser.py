"""
Tkinter - Codemy.com #195 : Open Web Browser From Tkinter
Lien : https://www.youtube.com/watch?v=fPjMgtlsvnc

Dans ce programme on apprend à ouvrir une page web

Éditeur : Laurent REYNAUD
Date : 27-10-21
"""

import tkinter as tk
import webbrowser

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Web Browser')
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Méthode lambda appliquée car on utilise l'instruction 'bind' 
        # pour le widget label 
        my_button = tk.Button(
            root, text="Ouvrir Web Browser !",
            font="Helvetica 34",
            command=lambda:self.open_browser('stuff'))
        my_button.pack(pady=50)
        
        my_label = tk.Label(
            root, 
            text="Ouvrir Browser",
            font="Helvetica 24",
            fg='blue')
        my_label.pack(pady=20)
        
        # Accès au site en cliquant sur le titre
        my_label.bind(
            '<Button-1>', 
            self.open_browser)
        
    def open_browser(self, e):
        "Accès au site codemy.com"
        
        webbrowser.open_new('https://codemy.com')

    
if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
