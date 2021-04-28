"""
Tkinter - Codemy.com #121 : Treeview Update self.records - Python Tkinter GUI Tutorial #121
Lien : https://www.youtube.com/watch?v=lKiNlSs_cms&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=121

Dans ce programme on sélectionne une ligne de données saisies en recourant à la fonction select_self.record() et on met à
jour les données avec la fonction update_self.record()

Éditeur : Laurent REYNAUD
Date : 22-12-20
"""

import tkinter
from tkinter import ttk

class GUI:

    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('images/Logo.ico')
        self.root.title('Titre !')
        self.root.geometry('500x700')
        self.widget_treeview()
        self.widgets_data()
        self.widgets_button()

    def widget_treeview(self):
        
        """Configuration du style de l'arborescence"""
        style = ttk.Style()

        """Style préconfiguré de l'arborescence"""
        style.theme_use('clam')

        """Style personnalisé de l'arborescence"""
        style.configure('Treeview',
                        background='silver',  # fond de couleur des lignes saisies dans l'arborescence
                        rowheight=25,  # 'épaisseur' des lignes saisies dans l'arborescence
                        fieldbackground='silver',  # fond de couleur des lignes non saisies dans l'arborescence
                        )
        style.map('Treeview', background=[('selected', 'green')])  # Couleur des lignes sélectionnées

        """Cadre pour l'arborescence"""
        tree_frame = tkinter.Frame(root)
        tree_frame.pack(pady=20)

        """Barre de défilement pour l'arborescence"""
        tree_scroll = tkinter.Scrollbar(tree_frame)
        tree_scroll.pack(side='right', fill='y')

        """Configuration de l'arborescence"""
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

        """Affichage des données"""
        self.my_tree.pack()

        """Configuration de la barre de défilement"""
        tree_scroll.config(command=self.my_tree.yview)

        """Configuration des colonnes"""
        self.my_tree['columns'] = ('Name', 'ID', 'Favorite pizza')

        """Formatage des colonnes"""
        self.my_tree.column('#0', width=0, stretch='no')  # colonne fantôme
        self.my_tree.column('Name', anchor='w', width=140)
        self.my_tree.column('ID', anchor='center', width=100)
        self.my_tree.column('Favorite pizza', anchor='w', width=140)

        """Configuration des en-têtes"""
        self.my_tree.heading('#0', text='', anchor='w')
        self.my_tree.heading('Name', text='Nom', anchor='w')
        self.my_tree.heading('ID', text='ID', anchor='center')
        self.my_tree.heading('Favorite pizza', text='Pizza préférée', anchor='w')

        """Ajout des données à partir d'une liste"""
        data = [['John', 1, 'Calzone'],
                ['Albert', 2, 'Fromages'],
                ['Marius', 3, 'Champignons'],
                ['Bob', 4, 'Anchois'],
                ['Clint', 5, 'Fruits de mer'],
                ['Erin', 6, 'Ananas'],
                ['Link', 7, 'Poivrons'],
                ['Dean', 8, 'Oeuf'],
                ['Heisenberg', 9, 'Crème fraîche'],
                ['John', 1, 'Calzone'],
                ['Albert', 2, 'Fromages'],
                ['Marius', 3, 'Champignons'],
                ['Bob', 4, 'Anchois'],
                ['Clint', 5, 'Fruits de mer'],
                ['Erin', 6, 'Ananas'],
                ['Link', 7, 'Poivrons'],
                ['Dean', 8, 'Oeuf'],
                ['John', 1, 'Calzone'],
                ['Albert', 2, 'Fromages'],
                ['Marius', 3, 'Champignons'],
                ['Bob', 4, 'Anchois'],
                ['Clint', 5, 'Fruits de mer'],
                ['Erin', 6, 'Ananas'],
                ['Link', 7, 'Poivrons'],
                ['Dean', 8, 'Oeuf']]

        """Configuration du coloriage des lignes saisies dans l'arborescence"""
        self.my_tree.tag_configure('oddrow', background='white')  # couleur de la rangée impaire
        self.my_tree.tag_configure('evenrow', background='lightblue')  # couleur de la même rangée

        """Recours à une boucle for pour alimenter les données de la liste ci-dessus dans l'arborescence et en attribuant une  
        couleur selon si la ligne de rangée est paire ou impaire"""
        self.count = 0
        for self.record in data:
            if self.count % 2 == 0:
                """Si la rangée est paire, la couleur de la lgine est de couleur blanche"""
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2]),
                               tags='evenrow')
            else:
                """Sinon la rangée est impaire et la couleur de la ligne est de couleur bleu claire"""
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2]),
                               tags='oddrow')
            self.count += 1

    def widgets_data(self):
        
        """Cadre"""
        add_frame = tkinter.Frame(root)
        add_frame.pack(pady=20)

        """Etiquettes"""
        nl = tkinter.Label(add_frame, text='Nom')
        nl.grid(row=0, column=0)

        il = tkinter.Label(add_frame, text='ID')
        il.grid(row=0, column=1)

        tl = tkinter.Label(add_frame, text='En-tête')
        tl.grid(row=0, column=2)

        """Champs de saisi"""
        self.name_box = tkinter.Entry(add_frame)
        self.name_box.grid(row=1, column=0)

        self.id_box = tkinter.Entry(add_frame, justify='center')
        self.id_box.grid(row=1, column=1)

        self.topping_box = tkinter.Entry(add_frame)
        self.topping_box.grid(row=1, column=2)

    def widgets_button(self):
        
        """Boutons"""
        select_button = tkinter.Button(root, text='Sélectionner', command=self.select_record)
        select_button.pack(pady=10)

        update_button = tkinter.Button(root, text='Mise à jour', command=self.update_record)
        update_button.pack(pady=10)

        add_record = tkinter.Button(root, text='Ajouter une donnée', command=self.add_record)
        add_record.pack(pady=10)

        remove_all = tkinter.Button(root, text='Effacer toute les données', command=self.remove_all)
        remove_all.pack(pady=10)

        remove_one = tkinter.Button(root, text='Effacer la donnée sélectionnée', command=self.remove_one)
        remove_one.pack(pady=10)

        remove_many = tkinter.Button(root, text='Effacer plusieurs données sélectionnées', command=self.remove_many)
        remove_many.pack(pady=10)

    def add_record(self):
        """Ajout des données dans l'arborescence"""

        """Configuration du coloriage des lignes saisies dans l'arborescence"""
        self.my_tree.tag_configure('oddrow', background='white')  # couleur de la rangée impaire
        self.my_tree.tag_configure('evenrow', background='lightblue')  # couleur de la même rangée

        if self.count % 2 == 0:
            """Si la rangée est paire, la couleur de la lineg est de couleur blanche"""
            self.my_tree.insert(parent='', index='end', iid=self.count, text='',
                values=(self.name_box.get(), self.id_box.get(), self.topping_box.get()), tags='evenrow')
        else:
            """Sinon la rangée est impaire et la couleur de la ligne est de couleur bleu claire"""
            self.my_tree.insert(parent='', index='end', iid=self.count, text='', 
                values=(self.name_box.get(), self.id_box.get(), self.topping_box.get()), tags='oddrow')
        self.count += 1
        self.name_box.delete(0, 'end')
        self.id_box.delete(0, 'end')
        self.topping_box.delete(0, 'end')

    def remove_all(self):
        """Suppression de toutes les données de l'arborescence"""
        for self.record in self.my_tree.get_children():
            self.my_tree.delete(self.record)

    def remove_one(self):
        """Suppression d'une donnée de l'arborescence"""
        x = self.my_tree.selection()[0]  # assignation d'une variable de la ligne sélectionnée
        self.my_tree.delete(x)  # suppression des données de la liste

    def remove_many(self):
        """Suppression de plusieurs données sélectionnées"""
        x = self.my_tree.selection()  # assignation d'une variable de la ligne sélectionnée
        for self.record in x:
            """Recours à une boucle pour supprimer un par un les données sélectionnées"""
            self.my_tree.delete(self.record)  # suppression des données de la liste

    def select_record(self):
        """Ajout dans les champs de saisies des données sélectionnées"""

        """Initialisation des champs de saisies"""
        self.name_box.delete(0, 'end')
        self.id_box.delete(0, 'end')
        self.topping_box.delete(0, 'end')

        """Assignation du n° d'indice de la ligne de saisie sélectionnée"""
        selected = self.my_tree.focus()

        """Assignation de la valeur de la ligne de saisie sélectionnée"""
        values = self.my_tree.item(selected, 'values')
        self.name_box.insert(0, values[0])
        self.id_box.insert(0, values[1])
        self.topping_box.insert(0, values[2])

    def update_record(self):
        """Mise à jour des données"""

        """Assignation du n° d'indice de la ligne de saisie sélectionnée (comme pour la fonction ci-avant)"""
        selected = self.my_tree.focus()

        """Mise à jour des données saisies"""
        self.my_tree.item(selected, text='', values=(self.name_box.get(), self.id_box.get(), self.topping_box.get()))

        """Initialisation des champs de saisies"""
        self.name_box.delete(0, 'end')
        self.id_box.delete(0, 'end')
        self.topping_box.delete(0, 'end')

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()    












