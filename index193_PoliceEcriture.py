"""
Tkinter - Codemy.com #193 : Change Font Size and Font Style
Lien : https://www.youtube.com/watch?v=wItYLrPnsYA

Dans ce programme, en complément du précédent, on rajoute
la taille et le style de police d'écriture

Éditeur : Laurent REYNAUD
Date : 28-09-21
"""

import tkinter as tk
from tkinter import font

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Choisir sa police d'écriture")
        root.geometry('550x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Police d'écriture par défaut
        self.our_font = font.Font(family='Helvetica', size='32')
        
        # Configuration du cadre pour la zone de texte
        my_frame = tk.Frame(root, width=510, height=275)
        my_frame.pack(pady=10)  
        my_frame.grid_propagate(False) # Taille limitée
        my_frame.columnconfigure(0, weight=10) # retour chariot
        
        # Configuration de la zone de texte
        my_text = tk.Text(my_frame, font=self.our_font)
        my_text.grid(row=0, column=0)
        # my_text.grid_rowconfigure(0, weight=1)
        # my_text.grid_columnconfigure(0, weight=1)
        
        # Cadre pour les zones de listes
        bottom_frame = tk.Frame(root)
        bottom_frame.pack()
        
        # Ajout de titres
        font_label = tk.Label(bottom_frame, 
                              text="Police", 
                              font='Helvetica 14')
        font_label.grid(row=0, column=0, padx=10, sticky='W')
        
        size_label  = tk.Label(bottom_frame, 
                              text="Taille", 
                              font='Helvetica 14')
        size_label.grid(row=0, column=1, sticky='W')
        
        style_label = tk.Label(bottom_frame, 
                              text="Style", 
                              font='Helvetica 14')
        style_label.grid(row=0, column=2, padx=10, sticky='W')
        
        
        # Zone de liste pour la police d'écriture
        self.my_listbox = tk.Listbox(
            bottom_frame, 
            selectmode='single', 
            width=40)
        self.my_listbox.grid(row=1, column=0, padx=10)
        
        # Zone de liste pour la taille d'écriture
        self.font_size_listbox = tk.Listbox(
            bottom_frame, 
            selectmode='single', 
            width=20)
        self.font_size_listbox.grid(row=1, column=1)
        
        # Zone de liste pour le style d'écriture
        self.font_style_listbox = tk.Listbox(
            bottom_frame, 
            selectmode='single', 
            width=20)
        self.font_style_listbox.grid(row=1, column=2, padx=10)
        
        # Insertion dans la zone de liste de la police d'écritures
        # toutes les polices d'écritures possibles
        for f in font.families():
            self.my_listbox.insert('end', f)
            
        # Insertion dans la zone de taille de la police d'écritures
        # toutes les tailles de police possibles
        self.font_sizes = [8, 10, 12, 14, 16, 18, 20, 36, 48]
        for size in self.font_sizes:
            self.font_size_listbox.insert('end', size)
        
        # Insertion dans la zone de style de la police d'écritures
        # toutes les styles de police possibles
        self.font_styles = ["Normal",
                            "Gras",
                            "Italique",
                            "Gras et italique",
                            "Souligné",
                            "Barré"]
        for style in self.font_styles:
            self.font_style_listbox.insert('end', style)
        
        # Action effectuée selon la police d'écriture sélectionnée    
        self.my_listbox.bind(
            '<ButtonRelease-1>', 
            self.font_chooser)
        
        # Action effectuée selon la taille d'écriture sélectionnée
        self.font_size_listbox.bind(
            '<ButtonRelease-1>', 
            self.font_size_chooser)
        
        # Action effectuée selon le style d'écriture sélectionné
        self.font_style_listbox.bind(
            '<ButtonRelease-1>', 
            self.font_style_chooser)
        
    def font_chooser(self, e):
        "Mise à jour de la police d'écriture dans la zone de texte"
        
        self.our_font.config(
            family=self.my_listbox.get(self.my_listbox.curselection()))
        
    def font_size_chooser(self, e):
        "Mise à jour de la taille de police d'écriture dans la zone de texte"
        
        self.our_font.config(
            size=self.font_size_listbox.get(
                self.font_size_listbox.curselection()))
        
    
    def font_style_chooser(self, e):
        "Mise à jour du style de police d'écriture dans la zone de texte"
        
        style = self.font_style_listbox.get(
            self.font_style_listbox.curselection()).lower()
        
        if style == 'gras':
            self.our_font.config(weight='bold')
        if style == 'italique':
            self.our_font.config(slant='italic')
        if style == 'gras et italique':
            self.our_font.config(weight='bold', slant='italic')
        if style == 'souligné':
            self.our_font.config(underline=1)
        if style == 'barré':
            self.our_font.config(overstrike=1)
        if style == 'normal':
            self.our_font.config(
                weight='normal', 
                slant='roman',
                underline=0,
                overstrike=0)
           

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
