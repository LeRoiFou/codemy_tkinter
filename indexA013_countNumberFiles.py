"""
Tkinter - Codemy.com : Count Number Of Files In A Directory - Tkinter Projects 13
Lien : https://www.youtube.com/watch?v=m_FEUK0_Ryc

Dans ce programme, on apprend on calculer le nombre 
de fichier dans un répertoire

Date : 01/12/22
"""

import tkinter as tk
from tkinter import filedialog
import os

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Nombre de fichiers !")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_label = tk.Label(root, text="Nombre de fichiers : ",
                                 font='Helvetica 28')
        self.my_label.pack(pady=50)
        
        my_button = tk.Button(root, text='Vérifier le nombre de fichiers',
                              command=self.checker)
        my_button.pack()
        
    def checker(self):
        
        # Create counters
        file_count = 0
        dir_count = 0
        
        # Choose directory
        input_path = filedialog.askdirectory()
        
        # Loop and count files
        for root, dirs, files in os.walk(input_path):
            # Count files
            for file in files:
                file_count += 1
            # Count dirs
            for dir1 in dirs:
                dir_count += 1
            # Count files

            # Update our label
            self.my_label.config(text=(f"Nombre de fichiers : {file_count}\nNombre de répertoires : {dir_count}"))
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
