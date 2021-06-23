"""
Tkinter - Codemy.com #127 : 
How To Disable Or Delete A Menu Item 
- Python Tkinter GUI Tutorial #127
Lien : https://www.youtube.com/watch?v=s1WDk9-jJ6A&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=127

Dans ce programme on apprend à déconnecter ou à supprimer un menu

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.title('Titre !')
        root.geometry('500x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Barre de menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Menu Fichier"""
        self.file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=self.file_menu)
        self.file_menu.add_command(label='Nouveau', command=self.new_file)
        self.file_menu.add_command(label='Ouvrir', command=self.open_file)

        """Boutons"""
        disable_button = tkinter.Button(
            root, 
            text="Désactiver la commande 'Nouveau'", 
            command=self.disable_new)
        disable_button.pack(pady=50)
        enable_button = tkinter.Button(
            root, 
            text="Activer la commande 'Nouveau'", 
            command=self.enable_new)
        enable_button.pack(pady=10)
        delete_button = tkinter.Button(
            root, 
            text="Supprimer la commande 'Nouveau'", 
            command=self.delete_new)
        delete_button.pack(pady=20)
        
    def new_file(self):
        pass

    def open_file(self):
        pass

    def disable_new(self):
        """Méthode permettant de désactiver la commande 'Nouveau'
        du menu 'Fichier'"""
        
        self.file_menu.entryconfig('Nouveau', state='disabled')

    def enable_new(self):
        """Méthode permettant d'activer la commande 'Nouveau' 
        du menu 'Fichier'"""
        
        self.file_menu.entryconfig('Nouveau', state='active')

    def delete_new(self):
        """Méthode permettant de supprimer la commande 'Nouveau' 
        du menu 'Fichier'"""
        
        self.file_menu.delete('Nouveau')


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
