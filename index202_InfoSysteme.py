"""
Tkinter - Codemy.com #202 : Create A Mortgage Calculator
Lien : https://www.youtube.com/watch?v=WK8vEvw2HIM

Programme permettant de connaître le système de l'ordinateur portable

Éditeur : Laurent REYNAUD
Date : 14-12-21
"""

import tkinter as tk
import platform # information sur le système du portable

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Information système")
        root.geometry('700x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        info = f"Systeme : {platform.system()}\n \
        Nom d'utilisteur : {platform.node()}\n \
        Version Windows : {platform.release()}\n \
        Version : {platform.version()}\n \
        Machine : {platform.machine()}\n \
        Processeur : {platform.processor()}\n \
        Version de Python : {platform.python_version()}\n \
        "
        
        my_label = tk.Label(
            root,
            text=info,
            font='Helvetica 14')
        my_label.pack(pady=20)
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
