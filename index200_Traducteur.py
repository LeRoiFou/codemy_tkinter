"""
Tkinter - Codemy.com #200 : 
Lien : https://www.youtube.com/watch?v=64f5fKBM3-o

Modules installés : 
googletrans
textblob

Dans ce programme on créé une application pour les traductions

Éditeur : Laurent REYNAUD
Date : 01-12-21
"""

import tkinter as tk
import googletrans
import textblob
from tkinter import Text, ttk, messagebox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Traducteur")
        root.geometry('880x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Liste des langues présentes dans google
        self.languages = googletrans.LANGUAGES
        
        # Conversion en liste
        language_list = list(self.languages.values())
        
        self.original_text = tk.Text(
            root,
            height=10, 
            width=40)
        self.original_text.grid(
            row=0, column=0, pady=20, padx=10)
        
        translate_button = tk.Button(
            root,
            text="Traduire !",
            font='Helvetica 24',
            command=self.translate_it)
        translate_button.grid(
            row=0, column=1, padx=10)
        
        self.translated_text = tk.Text(
            root,
            height=10, 
            width=40)
        self.translated_text.grid(
            row=0, column=2, pady=20, padx=10)
        
        self.original_combo = ttk.Combobox(
            root,
            width=50,
            value=language_list)
        self.original_combo.current(26)
        self.original_combo.grid(
            row=2, column=0)
        
        self.translated_combo = ttk.Combobox(
            root,
            width=50,
            value=language_list)
        self.translated_combo.current(21)
        self.translated_combo.grid(
            row=2, column=2)
        
        clear_button = tk.Button(
            root,
            text="Effacer",
            command=self.clear)
        clear_button.grid(row=2, column=1)
        
        
    def translate_it(self):
        "Traduction du texte"
        
        # Réinitialisation du texte
        self.translated_text.delete(1.0, 'end')
        
        try:
            # Obtenir la langue du dictionnaire
            
            # Language du mot à traduire
            for key, value in self.languages.items():
                if (value == self.original_combo.get()):
                    from_language_key = key
            
            # Language du mot traduit
            for key, value in self.languages.items():
                if (value == self.translated_combo.get()):
                    to_language_key = key
                    
            #
            # words = textblob.TextBlob(self.original_text.get(1.0, 'end'))
            
            # Traduction du texte
            words = words.translate(
                from_lang=from_language_key,
                to=to_language_key)
            
            # Affichage du texte traduit
            self.translated_text.insert(1.0, words)

        except Exception as e:
            messagebox.showerror(
                "Traduction", e)
    
    def clear(self):
        "Texte effacé"
        
        self.original_text.delete(1.0, 'end')
        self.translated_text.delete(1.0, 'end')

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
