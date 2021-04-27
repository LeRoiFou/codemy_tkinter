"""
Tkinter - Codemy.com #117 : Add And Remove Records From Treeview - Python Tkinter GUI Tutorial #117
Lien : https://www.youtube.com/watch?v=rtR5wHXPKZ4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=117

Dans ce programme on apprend à ajouter et à supprimer des données de l'arborescence

Éditeur : Laurent REYNAUD
Date : 21-12-20
"""

import tkinter
from tkinter import ttk

class GUI:

    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('images/Logo.ico')
        self.root.title('Titre !')
        self.root.geometry('500x600')
        self.widget_treeview()
        self.widgets_data()
        self.widgets_button()

    def widget_treeview(self):
        # Configuration de l'arborescence

        self.my_tree = ttk.Treeview(root)

        # Configuration des colonnes
        self.my_tree['columns'] = ('Name', 'ID', 'Favorite pizza')

        # Formatage des colonnes
        self.my_tree.column('#0', width=0, stretch='no')  # colonne fantôme
        self.my_tree.column('Name', anchor='w', width=140)
        self.my_tree.column('ID', anchor='center', width=100)
        self.my_tree.column('Favorite pizza', anchor='w', width=140)

        # Configuration des en-têtes
        self.my_tree.heading('#0', text='', anchor='w')
        self.my_tree.heading('Name', text='Nom', anchor='w')
        self.my_tree.heading('ID', text='ID', anchor='center')
        self.my_tree.heading('Favorite pizza', text='Pizza préférée', anchor='w')

        # Ajout des données à partir d'une liste
        data = [['John', 1, 'Calzone'],
                ['Albert', 2, 'Fromages'],
                ['Marius', 3, 'Champignons'],
                ['Bob', 4, 'Anchois'],
                ['Clint', 5, 'Fruits de mer'],
                ['Erin', 6, 'Ananas']]

        # Recours à une boucle for pour alimenter les données de la liste ci-dessus dans l'arborescence
        self.count = 0
        for record in data:
            self.my_tree.insert(parent='', index='end', iid=self.count, text='', 
                values=(record[0], record[1], record[2]))
            self.count += 1

        # Affichage des données
        self.my_tree.pack(pady=20)

    def widgets_data(self):
        # configuration des données à intervenir

        # Cadre
        add_frame = tkinter.Frame(root)
        add_frame.pack(pady=20)

        # Etiquettes
        nl = tkinter.Label(add_frame, text='Nom')
        nl.grid(row=0, column=0)

        il = tkinter.Label(add_frame, text='ID')
        il.grid(row=0, column=1)

        tl = tkinter.Label(add_frame, text='Pizza préférée')
        tl.grid(row=0, column=2)

        # Champs de saisi
        self.name_box = tkinter.Entry(add_frame)
        self.name_box.grid(row=1, column=0)

        self.id_box = tkinter.Entry(add_frame, justify='center')
        self.id_box.grid(row=1, column=1)

        self.topping_box = tkinter.Entry(add_frame)
        self.topping_box.grid(row=1, column=2)

    def widgets_button(self):
        # Configuration des boutons

        add_record = tkinter.Button(root, text='Ajouter une donnée', command=self.add_record)
        add_record.pack(pady=10)

        remove_all = tkinter.Button(root, text='Effacer toute les données', command=self.remove_all)
        remove_all.pack(pady=10)

        remove_one = tkinter.Button(root, text='Effacer la donnée sélectionnée', command=self.remove_one)
        remove_one.pack(pady=10)

        remove_many = tkinter.Button(root, text='Effacer plusieurs données sélectionnées', command=self.remove_many)
        remove_many.pack(pady=10)

    def add_record(self):
        # Ajout des données dans l'arborescence
        
        self.my_tree.insert(parent='', index='end', iid=self.count, text='', 
            values=(self.name_box.get(), self.id_box.get(), self.topping_box.get()))
        self.count += 1
        self.name_box.delete(0, 'end')
        self.id_box.delete(0, 'end')
        self.topping_box.delete(0, 'end')


    def remove_all(self):
        # Suppression de toutes les données de l'arborescence
        
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)


    def remove_one(self):
        # Suppression d'une donnée de l'arborescence
       
        x = self.my_tree.selection()[0]  # assignation d'une variable de la ligne sélectionnée
        self.my_tree.delete(x)  # suppression des données de la liste


    def remove_many(self):
        # Suppression de plusieurs données sélectionnées
        
        x = self.my_tree.selection()  # assignation d'une variable de la ligne sélectionnée
        for record in x:
            """Recours à une boucle pour supprimer un par un les données sélectionnées"""
            self.my_tree.delete(record)  # suppression des données de la liste


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()