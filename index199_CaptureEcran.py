"""
Tkinter - Codemy.com #199 : Take Screenshots From Your Tkinter App
Lien : https://www.youtube.com/watch?v=h4GsyYvoLPM

Module importé : mss

Dans ce programme on apprend à faire des captures d'écran :)

Éditeur : Laurent REYNAUD
Date : 23-11-2021
"""

import tkinter as tk
from mss import mss

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Capture d'écran !")
        root.geometry('500x200')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_button = tk.Button(
            root, 
            text="Capture d'écran !",
            font='Helvetica 24',
            command=self.shoot)
        my_button.pack(pady=40)
        
        self.my_label = tk.Label(
            root,
            text='')
        self.my_label.pack(pady=10)
        
    def shoot(self):
        "Capture d'écran !"
        
        with mss() as sct:
            
            # Désigner un répertoire / nom de fichier
            filename = sct.shot(
                mon=1, # Nombre d'écrans à capturer
                output='pic/output.png')
            
            # Confirmation de la capture d'écran
            self.my_label.config(
                text="Capture d'écran sauvegardée ;)")
                     

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
