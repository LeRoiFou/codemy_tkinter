"""
Titre : File Dialog Boxes - Object Oriented Tkinter 3
Lien : https://www.youtube.com/watch?v=ouO_QRJtvNE

POO avec ouverture d'une boîte de dialogue

Date : 06-02-24
"""

import tkinter as tk
from tkinter import filedialog

class App(tk.Tk) :
    
    def __init__(self):
        
        # Héritage de la sous-librairie Tk de tkinter
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("Dialog Boxes!")
        self.geometry('700x450')

        # Create widgets
        self.my_text = tk.Text(self, width=80, height=20)
        self.my_text.pack(pady=20)
        
        self.my_button = tk.Button(self, text="Open File", command=self.file)
        self.my_button.pack(pady=20)
        
    def file(self):
        
        self.my_file = filedialog.askopenfilename(
            initialdir='', title='Select a file', 
            filetypes=(('txt files', '*.txt'), ('All files', '*.*')))
        
        if self.my_file:
            
            # Lecture du fichier à charger
            get_contents = open(self.my_file, 'r')
            
            # Insertion du contenu du fichier chargé
            self.my_text.insert(tk.END, get_contents.read())
        

if __name__ == '__main__':
    
    # Intanciation de la classe App et lancement de l'application
    app =  App()
    app.mainloop()
