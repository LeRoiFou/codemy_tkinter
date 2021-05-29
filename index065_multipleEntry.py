"""
Tkinter - Codemy.com #65 : Creating Multiple Entry Boxes Automatically - Python Tkinter GUI Tutorial #65
Lien : https://www.youtube.com/watch?v=H3Cjtm6NuaQ

Dans ce programme on apprend à afficher plusieurs champs de saisis avec une boucle

Éditeur : Laurent REYNAUD
Date : 06-02-21
"""

import tkinter

class GUI:

    def __init__(self, root):
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('700x500')
        self.widgets()

    def widgets(self):
        
        # Assignation d'une liste
        self.my_entries = []

        # Configuration des champs de saisis en recourant à la boucle  'for in range'
        # nombre de libnes = 5
        for x in range(5):  
            # nombre de colonnes = 5
            for y in range(5):  
                my_entry = tkinter.Entry(root)
                my_entry.grid(row=x, column=y, pady=20, padx=5)
                # ajout des données écrites dans les champs de saisis dans la liste 'self.my_entries'
                self.my_entries.append(my_entry)  

        # Configuration du bouton d'exécution
        my_button = tkinter.Button(root, text='Appuie !', command=self.something)
        my_button.grid(row=6, column=0, pady=20)

        # Configuration du l'étiquette
        self.my_label = tkinter.Label(root, text='')
        self.my_label.grid(row=7, column=0, pady=20)

    def something(self):
    # méthode permettant d'afficher ce que l'on saisit dans les champs de saisis

        # Assignation d'une str
        entry_list = ''

        # Affichage des données de la liste 'self.my_entries' en tant que str
        # pour chaque donnée dans la liste 'self.my_entries'..
        for data in self.my_entries:  
            # conversion des données de la liste 'self.my_entries' en str
            entry_list = entry_list + str(data.get()) + '\n'  
            self.my_label.config(text=entry_list)

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
