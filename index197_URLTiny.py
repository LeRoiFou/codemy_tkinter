"""
Tkinter - Codemy.com #197 : Create An Url Link Shortener
Lien : https://www.youtube.com/watch?v=oBi16YJjf8w

Module installé : pyshorteners

TinyURL (tinyurl.com) est un service web de réduction d'URL 
créé par Kevin Gilbertson dans le but d'offrir de courts 
alias d'adresse web. Gilbertson, un développeur web, 
a lancé ce service en janvier 2002 car il souhaitait publier des hyperliens 
vers des post dans les forums Internet, post qui avaient souvent 
une longue URL difficile à lire et à retenir.

Éditeur : Laurent REYNAUD
Date : 09-11-21
"""

import tkinter as tk
import pyshorteners

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Create An Url Link Shortener')
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_label = tk.Label(
            root, 
            text="Entrer le lien vers le raccourci",
            font='Helveticat 24')
        my_label.pack(pady=20)
        
        self.my_entry = tk.Entry(
            root,
            font='Helveticat 24')
        self.my_entry.pack(pady=20)
        
        my_button = tk.Button(
            root,
            text="Raccourcir le lien",
            command=self.shorten,
            font='Helvetica 24')
        my_button.pack(pady=20)
        
        shorty_label = tk.Label(
            root,
            text="Lien raccourci ;)",
            font='Helveticat 14')
        shorty_label.pack(pady=50)
        
        self.shorty = tk.Entry(
            root,
            font='Helvetica 22',
            justify='center',
            width=30,
            bd=0,
            bg='systembuttonface')
        self.shorty.pack(pady=10)
        
    def shorten(self):
        ""
        
        # S'il y a déjà un lien 'tiny' déjà affiché...
        if self.shorty.get():
            self.shorty.delete(0, 'end')
         
        # S'il y a un lien @ saisie...
        if self.my_entry.get():
            # Convertir ce lien en un lien 'tiny'
            url = pyshorteners.Shortener().tinyurl.short(self.my_entry.get())
            # Et insérer le lien dans la zone de saisie concernée
            self.shorty.insert('end', url)
            
            # Affichage dans la console du lien "d'origine"
            print(pyshorteners.Shortener().tinyurl.expand(url))

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
