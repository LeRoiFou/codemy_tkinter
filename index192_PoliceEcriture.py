"""
Tkinter - Codemy.com #192 : Create Font Chooser App
Lien : https://www.youtube.com/watch?v=QG0_RSNkMCo

Dans ce programme on apprend à choisir sa police d'écriture avec
un programment relativement simple

Éditeur : Laurent REYNAUD
Date : 21-09-21
"""

import tkinter as tk
from tkinter import font

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Choisir sa police d'écriture")
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Police d'écriture par défaut
        self.our_font = font.Font(family='Helvetica', size='32')
        
        # Configuration du cadre pour la zone de texte
        my_frame = tk.Frame(root, width=480, height=275)
        my_frame.pack(pady=10)  
        my_frame.grid_propagate(False) # Taille limitée
        my_frame.columnconfigure(0, weight=10) # retour chariot
        
        # Configuration de la zone de texte
        my_text = tk.Text(my_frame, font=self.our_font)
        my_text.grid(row=0, column=0)
        # my_text.grid_rowconfigure(0, weight=1)
        # my_text.grid_columnconfigure(0, weight=1)
        
        # Configuration de la zone de liste
        self.my_listbox = tk.Listbox(root, selectmode='single', width=80)
        self.my_listbox.pack()
        
        # Insertion dans la zone de liste de
        # toutes les polices d'écritures possibles
        for f in font.families():
            self.my_listbox.insert('end', f)
        
        # Action effectuée selon la police d'écriture sélectionnée    
        self.my_listbox.bind('<ButtonRelease-1>', self.font_chooser)
        
    def font_chooser(self, e):
        "Mise à jour de la police d'écriture dans la zone de texte"
        
        self.our_font.config(
            family=self.my_listbox.get(self.my_listbox.curselection()))
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
