"""
Tkinter - Codemy.com #152 : 
Dependent Drop Downs and List Boxes - Python Tkinter GUI Tutorial #152
Lien : https://www.youtube.com/watch?v=bH9r3wM9Idw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=152

Dans ce programme on apprend à rendre dépendant :
-> Un deuxième menu déroulant (dropdown) par rapport 
au premier menu déroulant
-> Une deuxième zone de liste (listbox) par rapport 
à la première zone de liste

Exemple :
Dans le 1er menu déroulant figure les départements d'une région
Dans le 2ème menu déroulant figure les communes du département 
sélectionné dans le 1er menu déroulant

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

import tkinter
from tkinter import ttk

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x400')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Assignation d'un liste de tailles"""
        sizes = ['Petit', 'Moyen', 'Grand']

        """Assignation d'une liste de couleurs"""
        self.small_colors = ['Rouge', 'Vert', 'Bleu', 'Noir']
        self.medium_colors = ['Rouge', 'Vert']
        self.large_colors = ['Bleu', 'Noir']

        """Configuration de la liste déroulante 
        pour les différentes tailles"""
        self.my_combo = ttk.Combobox(root, value=sizes)
        self.my_combo.current(0)  # valeur par défaut en affichage : 'Petit'
        self.my_combo.pack(pady=20)

        """Liaison du menu déroulant des différentes tailles 
        avec le menu déroulant des différentes couleurs"""
        self.my_combo.bind('<<ComboboxSelected>>', self.pick_color)

        """Configuration de la liste déroulante 
        pour les différentes couleurs"""
        self.color_combo = ttk.Combobox(root, value=[' '])
        self.color_combo.pack(pady=20)

        """Cadre pour les zones de liste"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=50)

        """Configuration des zones de liste"""
        self.my_list1 = tkinter.Listbox(my_frame)
        self.my_list1.grid(row=0, column=0)
        self.my_list2 = tkinter.Listbox(my_frame)
        self.my_list2.grid(row=0, column=1, padx=20)

        """Ajout des éléments à la zone de liste 1"""
        for item in sizes:
            self.my_list1.insert('end', item)

        """Liaison de la 1ère zone de liste avec la 2ème zone de liste"""
        self.my_list1.bind('<<ListboxSelect>>', self.list_color)
        
    def pick_color(self, e):
        """Méthode pour les menus déroulants permettant d'afficher 
        les différentes couleurs selon la taille choisie"""
        
        if self.my_combo.get() == 'Petit':
            self.color_combo.config(value=self.small_colors)
            self.color_combo.current(0)
        
        elif self.my_combo.get() == 'Moyen':
            self.color_combo.config(value=self.medium_colors)
            self.color_combo.current(0)
        
        elif self.my_combo.get() == 'Grand':
            self.color_combo.config(value=self.large_colors)
            self.color_combo.current(0)

    def list_color(self, e):
        """Méthode pour les zones de listes permettant d'afficher 
        les différentes couleurs selon la taille choisie"""
        
        self.my_list2.delete(0, 'end')  # réinitialisation des données
        
        if self.my_list1.get('anchor') == 'Petit':
            for item in self.small_colors:
                self.my_list2.insert('end', item)
        
        elif self.my_list1.get('anchor') == 'Moyen':
            for item in self.medium_colors:
                self.my_list2.insert('end', item)
        
        elif self.my_list1.get('anchor') == 'Grand':
            for item in self.large_colors:
                self.my_list2.insert('end', item)


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
