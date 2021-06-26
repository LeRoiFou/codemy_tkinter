"""
Tkinter - Codemy.com #154 : 
Todo List App Part 1 - Python Tkinter GUI Tutorial #154
Lien : https://www.youtube.com/watch?v=xB68I2fMAuU&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=154

Dans ce programme on apprend à faire une liste des points à faire, 
tout en effaçant certains points de la liste, ou
tous les points de la liste, ou à rayer les points effectués, 
ou à sauvegarder les points de la liste

Les exemples des différents types d'écritures se trouvent sur C:/Windows/Fonts

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

import tkinter
from tkinter.font import Font

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Ma liste !')
        root.geometry('500x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration de la police d'écriture"""
        my_font = Font(
            family='Brush Script MT',  # 
            size=30,
            weight='bold')

        """Cadre pour la zone de liste et la barre de défilement"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=10)

        """Configuration et affichage d'une zone de liste
        -> bg='SystemButtonFace' : couleur par défaut de la fenêtre
        -> highlightthickness=0 :  suppression de la bordure du cadre
        -> selectbackground='#a6a6a6' : 
         de fond de la donnée sélectionnée
        -> activestyle='none' : 
        suppression du soulignement de la donnée sélectionnée        
        """
        self.my_list = tkinter.Listbox(my_frame,
                        font=my_font,
                        width=25,
                        height=5,
                        bg='SystemButtonFace',
                        bd=0,
                        fg='#464646',
                        highlightthickness=0,
                        selectbackground='#a6a6a6',
                        activestyle='none',
                        justify='center')
        self.my_list.pack(side='left', fill='both')

        """Assignation d'une liste des choses à faire"""
        stuff = [
            'Jeux', 
            'Cours', 
            'Documentation', 
            'Dossiers', 
            'Manger', 
            'Sport', 
            'Travaux divers', 
            'Administratif']

        """Ajout des données de la liste des choses 
        à faire dans la zone de liste"""
        for item in stuff:
            self.my_list.insert('end', item)

        """Configuration et affichage de la barre de défilement"""
        my_scrollbar = tkinter.Scrollbar(my_frame)
        my_scrollbar.pack(side='right', fill='both')

        """Ajout de la barre de défilement à la zone de liste"""
        self.my_list.config(yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=self.my_list.yview)

        """Configuration et affichage d'un champ de saisie 
        pour ajouter les données dans la zone de liste"""
        self.my_entry = tkinter.Entry(
            root, 
            font='Helvetica 24', 
            justify='center')
        self.my_entry.pack(pady=20)

        """Cadre pour les boutons d'exécution"""
        button_frame = tkinter.Frame(root)
        button_frame.pack(pady=20)
        
        """Ajout des boutons"""
        delete_button = tkinter.Button(
            button_frame, 
            text='Effacer', 
            command=self.delete_item)
        add_button = tkinter.Button(
            button_frame, 
            text='Ajouter', 
            command=self.add_item)
        cross_off_button = tkinter.Button(
            button_frame, 
            text='Rayer', 
            command=self.cross_off_item)
        uncross_button = tkinter.Button(
            button_frame, 
            text='Réactiver', 
            command=self.uncross_item)

        """Affichage des boutons"""
        delete_button.grid(row=0, column=0, padx=20)
        add_button.grid(row=0, column=1, padx=20)
        cross_off_button.grid(row=0, column=2, padx=20)
        uncross_button.grid(row=0, column=3, padx=20)
        
    def delete_item(self):
        """Méthode permettant de supprimer un élément de la liste"""
        
        self.my_list.delete('anchor')

    def add_item(self):
        """Méthode permettant d'ajouter un élément de la liste"""
        
        self.my_list.insert('end', self.my_entry.get())
        self.my_entry.delete(0, 'end')

    def cross_off_item(self):
        """"""

    def uncross_item(self):
        """"""
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
