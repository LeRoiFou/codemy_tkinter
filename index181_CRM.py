"""
Tkinter - Codemy.com #181 : Add A Color Chooser To Treeview 
- Python Tkinter GUI Tutorial 181
Lien : https://www.youtube.com/watch?v=4j__fwak70g

Dans ce programme on apprend autre chose qu'à convertir 
une devise en une autre devise, 
pour cela on a recours à une API 
(interface de programmation applicative)...

On apprend à créer un CRM 
(Customer Relationship Management = Gestion de la relation client) 
avec le widget treeview (arborescence) et le recours 
à une base de données

Dans ce cours on apprend à changer les couleurs 
par défaut du widget treeview.
Pour cela, on importe l'objet colorchooser de tkinter et 
on rajoute un menu à la fenêtre principale avec 
ajout des méthodes suivantes :
-> primary_color()
-> secondary_color()
-> highlight_color()

À chaque fois qu'on intervient dans le SGBD, 
on a recours au langage SQL avec l'instruction c.execute()

Éditeur : Laurent REYNAUD
Date : 17-06-2021
"""

import tkinter
# Pour le widget treeview
from tkinter import ttk
# Message d'information/alerte...
from tkinter import messagebox 
# Couleurs pour les widgets
from tkinter import colorchooser 
import sqlite3

class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title('CRM')
        self.root.geometry('1000x500')
        self.database()
        self.menu()
        self.widgets_treeview()
        self.widgets_data()
        self.widgets_buttons()
        self.query_database()

    def menu(self):
       "Menu pour configurer les couleurs du widget treeview"
       
       # Ajout du menu
       my_menu = tkinter.Menu(root)
       root.config(menu=my_menu)
       
       # Menu 'Options'
       option_menu = tkinter.Menu(my_menu, tearoff=0)
       my_menu.add_cascade(label="Options", menu=option_menu)
       
       # Menu déroulant de 'Options'
       option_menu.add_command(
           label="Changer les couleurs primaires", 
           command=self.primary_color)
       option_menu.add_command(
           label="Changer les couleurs secondaires", 
           command=self.secondary_color)
       option_menu.add_command(
           label="Couleur de la ligne sélectionnée", 
           command=self.highlight_color)
       option_menu.add_separator()
       option_menu.add_command(label="Quitter", command=root.quit)
       
    def database(self):

        """
        # Liste de données clients
        self.data = [
        	["John", "Elder", 1, "123 Elder St.", 
         "Las Vegas", "NV", "89137"],
        	["Mary", "Smith", 2, "435 West Lookout", 
         "Chicago", "IL", "60610"],
        	["Tim", "Tanaka", 3, "246 Main St.", 
         "New York", "NY", "12345"],
        	["Erin", "Erinton", 4, "333 Top Way.", 
         "Los Angeles", "CA", "90210"],
        	["Bob", "Bobberly", 5, "876 Left St.", 
         "Memphis", "TN", "34321"],
        	["Steve", "Smith", 6, "1234 Main St.", 
         "Miami", "FL", "12321"],
        	["Tina", "Browne", 7, "654 Street Ave.", 
         "Chicago", "IL", "60611"],
        	["Mark", "Lane", 8, "12 East St.", 
         "Nashville", "TN", "54345"],
        	["John", "Smith", 9, "678 North Ave.", 
         "St. Louis", "MO", "67821"],
        	["Mary", "Todd", 10, "9 Elder Way.", 
         "Dallas", "TX", "88948"],
        	["John", "Lincoln", 11, "123 Elder St.", 
         "Las Vegas", "NV", "89137"],
        	["Mary", "Bush", 12, "435 West Lookout", 
         "Chicago", "IL", "60610"],
        	["Tim", "Reagan", 13, "246 Main St.", 
         "New York", "NY", "12345"],
        	["Erin", "Smith", 14, "333 Top Way.", 
         "Los Angeles", "CA", "90210"],
        	["Bob", "Field", 15, "876 Left St.", 
         "Memphis", "TN", "34321"],
        	["Steve", "Target", 16, "1234 Main St.", 
         "Miami", "FL", "12321"],
        	["Tina", "Walton", 17, "654 Street Ave.", 
         "Chicago", "IL", "60611"],
        	["Mark", "Erendale", 18, "12 East St.", 
         "Nashville", "TN", "54345"],
        	["John", "Nowerton", 19, "678 North Ave.", 
         "St. Louis", "MO", "67821"],
        	["Mary", "Hornblower", 20, "9 Elder Way.", 
         "Dallas", "TX", "88948"]	
        ]
        """

        """Création d'une base de donnée ou 
        connection à cette base de donnée"""
        self.conn = sqlite3.connect('database/tree_crm.db')

        # Création d'une instance de curseur
        c = self.conn.cursor()

        # Création d'une table si cette table n'existe pas
        c.execute("""CREATE TABLE if not exists customers (
        	Prenom text,
        	Nom text,
        	ID integer,
        	Adresse text,
        	Ville text,
        	Departement text,
        	CP text)
        	""")
        """
        # Ajout des éléments à la base de données
        for record in self.data:
        	c.execute("INSERT INTO customers VALUES 
         (:Prenom, :Nom, :ID, :Adresse, 
         :Ville, :Departement, :CP)", 
        {
        'Prenom': record[0],
        'Nom': record[1],
        'ID': record[2],
        'Adresse': record[3],
        'Ville': record[4],
        'Departement': record[5],
        'CP': record[6]
        }
        )
        """

        # Commit
        self.conn.commit()

        # Arrêt de la connection
        self.conn.close()

    def widgets_treeview(self):
        "Configuration du widget treeview"

        # Ajout de style
        self.style = ttk.Style()

        # Choix d'un thème
        self.style.theme_use('default')

        # Configuration des couleurs du treeview
        self.style.configure("Treeview", 
        	background="#D3D3D3",
        	foreground="black",
        	rowheight=25,
        	fieldbackground="#D3D3D3")

        # Changement de couleur à la sélection
        self.style.map('Treeview',
        	background=[('selected', '#347083')])

        """Créer un cadre pour le treeview 
        (pour la barre de défilement du treview)"""
        tree_frame = tkinter.Frame(root)
        tree_frame.pack(pady=10)

        # Créer une barre de défilement pour le treeview
        tree_scroll = tkinter.Scrollbar(tree_frame)
        tree_scroll.pack(side='right', fill='y')

        # Création du treeview
        self.my_tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set, 
            selectmode="extended")
        self.my_tree.pack()

        # Configuration de la barre de défilement
        tree_scroll.config(command=self.my_tree.yview)

        # Configuration des en-têtes
        self.my_tree['columns'] = (
            "Prénom", 
            "Nom", 
            "ID", 
            "Adresse",
            "Ville", 
            "Etat", 
            "Code postal")

        # Format des en-têtes
        self.my_tree.column("#0",
                            width=0, 
                            stretch='no')
        self.my_tree.column("Prénom", 
                            anchor='w', 
                            width=140)
        self.my_tree.column("Nom", 
                            anchor='w',
                            width=140)
        self.my_tree.column("ID", 
                            anchor='center',
                            width=100)
        self.my_tree.column("Adresse", 
                            anchor='center',
                            width=140)
        self.my_tree.column("Ville", 
                            anchor='center', 
                            width=140)
        self.my_tree.column("Etat", 
                            anchor='center', 
                            width=140)
        self.my_tree.column("Code postal", 
                            anchor='center', 
                            width=140)

        # Configuration des entêtes lors du passage avec la souris
        self.my_tree.heading("#0", 
                             text="", 
                             anchor='w')
        self.my_tree.heading("Prénom", 
                             text="Prénom", 
                             anchor='w')
        self.my_tree.heading("Nom", 
                             text="Nom", 
                             anchor='w')
        self.my_tree.heading("ID", 
                             text="ID", 
                             anchor='center')
        self.my_tree.heading("Adresse", 
                             text="Adresse", 
                             anchor='center')
        self.my_tree.heading("Ville", 
                             text="Ville", 
                             anchor='center')
        self.my_tree.heading("Etat",
                             text="Département", 
                             anchor='center')
        self.my_tree.heading("Code postal",
                             text="Code postal",
                             anchor='center')

        "Configuration des lignes du treeview"
        
        # Lignes impaires
        self.my_tree.tag_configure(
            "oddrow", 
            background="white") 
        
        # Lignes paires
        self.my_tree.tag_configure(
            "evenrow",
            background="lightblue") 

    def widgets_data(self):
        """Configuration des widgets pour 
        l'enregistrement des données"""

        # Ajout des champs de saisies pour les enregistrements
        data_frame = tkinter.LabelFrame(
            root, 
            text='Enregistrements')
        data_frame.pack(fill='x', expand='yes', padx=20)

        fn_label = tkinter.Label(data_frame, text='Prénom')
        fn_label.grid(row=0, column=0, padx=10, pady=10)
        self.fn_entry = tkinter.Entry(data_frame)
        self.fn_entry.grid(row=0, column=1, padx=10, pady=10)

        ln_label = tkinter.Label(data_frame, text='Nom')
        ln_label.grid(row=0, column=2, padx=10, pady=10)
        self.ln_entry = tkinter.Entry(data_frame)
        self.ln_entry.grid(row=0, column=3, padx=10, pady=10)

        id_label = tkinter.Label(data_frame, text='ID')
        id_label.grid(row=0, column=4, padx=10, pady=10)
        self.id_entry = tkinter.Entry(data_frame)
        self.id_entry.grid(row=0, column=5, padx=10, pady=10)

        address_label = tkinter.Label(data_frame, text='Adresse')
        address_label.grid(row=1, column=0, padx=10, pady=10)
        self.address_entry = tkinter.Entry(data_frame)
        self.address_entry.grid(row=1, column=1, padx=10, pady=10)

        city_label = tkinter.Label(data_frame, text='Ville')
        city_label.grid(row=1, column=2, padx=10, pady=10)
        self.city_entry = tkinter.Entry(data_frame)
        self.city_entry.grid(row=1, column=3, padx=10, pady=10)

        state_label = tkinter.Label(data_frame, text='Etat')
        state_label.grid(row=1, column=4, padx=10, pady=10)
        self.state_entry = tkinter.Entry(data_frame)
        self.state_entry.grid(row=1, column=5, padx=10, pady=10)

        zipcode_label = tkinter.Label(data_frame, text='Code postal')
        zipcode_label.grid(row=1, column=6, padx=10, pady=10)
        self.zipcode_entry = tkinter.Entry(data_frame)
        self.zipcode_entry.grid(row=1, column=7, padx=10, pady=10)

    def widgets_buttons(self):
        "Configuration des widgets des boutons"

        # Ajout de boutons
        button_frame = tkinter.LabelFrame(root, text='Commandes')
        button_frame.pack(fill='x', expand='yes', padx=20)

        update_button = tkinter.Button(
            button_frame, 
            text='Modifier', 
            command=self.update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = tkinter.Button(
            button_frame, 
            text='Ajouter', 
            command=self.add_record)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_all_button = tkinter.Button(
            button_frame, 
            text='Tout supprimer', 
            command=self.remove_all)
        remove_all_button.grid(row=0, column=2, padx=10, pady=10)

        remove_one_button = tkinter.Button(
            button_frame, 
            text='Supprimer une donnée', 
            command=self.remove_one)
        remove_one_button.grid(row=0, column=3, padx=10, pady=10)

        remove_many_button = tkinter.Button(
            button_frame, 
            text='Supprimer plusieurs données', 
            command=self.remove_many)
        remove_many_button.grid(row=0, column=4, padx=10, pady=10)

        move_up_button = tkinter.Button(
            button_frame, 
            text='Monter', 
            command=self.up)
        move_up_button.grid(row=0, column=5, padx=10, pady=10)

        move_down_button = tkinter.Button(
            button_frame, 
            text='Descendre', 
            command=self.down)
        move_down_button.grid(row=0, column=6, padx=10, pady=10)

        select_record_button = tkinter.Button(
            button_frame, 
            text="Effacer les données affichées", 
            command=self.clear_entries)
        select_record_button.grid(row=0, column=7, padx=10, pady=10)

        # À chaque fois qu'on sélectionne un enregistrement 
        # celui-ci s'affiche
        self.my_tree.bind("<ButtonRelease-1>", self.select_record)

    def primary_color(self):
        "Méthode changeant les couleurs primaires du widget Treeview"
        
        # Ouverture de la fenêture du choix des couleurs
        primary_color = colorchooser.askcolor()[1]
        
        if primary_color:
            
            # Lignes paires
            self.my_tree.tag_configure(
                "evenrow",
                background=primary_color) 
    
    def secondary_color(self):
        "Méthode changeant les couleurs secondaires du widget Treeview"
        
        # Ouverture de la fenêture du choix des couleurs
        secondary_color = colorchooser.askcolor()[1]
        
        if secondary_color:
            
            # Lignes impaires
            self.my_tree.tag_configure(
                "oddrow", 
                background=secondary_color) 
    
    def highlight_color(self):
        "Méthode changeant la ligne sélectionnée du widget Treeview"
        
        # Ouverture de la fenêture du choix des couleurs
        highlight_color = colorchooser.askcolor()[1]
        
        if highlight_color:
        
            # Changement de couleur à la sélection
            self.style.map('Treeview',
                background=[('selected', highlight_color)])

    def update_record(self):
        " Méthode permettant de modifier la donnée enregistrée"

        # Récupération de la donnée enregistrée
        selected = self.my_tree.focus()
        self.my_tree.item(
            selected, 
            text="", 
            values=(
                self.fn_entry.get(), 
                self.ln_entry.get(), 
                self.id_entry.get(),
                self.address_entry.get(), 
                self.city_entry.get(), 
                self.state_entry.get(), 
                self.zipcode_entry.get()))

        # Accès à la base de données
        self.conn = sqlite3.connect('database/tree_crm.db')
        c = self.conn.cursor()

        # Mise à jour de la base de données (langage SQL)
        c.execute("""UPDATE customers SET 
        	Prenom = :prenom, 
        	Nom = :nom, 
        	Adresse = :adresse, 
        	Ville = :ville, 
        	Departement = :departement, 
        	CP = :cp 
        	WHERE oid = :oid""",
        	{
        	'prenom': self.fn_entry.get(),
        	'nom': self.ln_entry.get(),
        	'adresse': self.address_entry.get(),
        	'ville': self.city_entry.get(),
        	'departement': self.state_entry.get(),
        	'cp': self.zipcode_entry.get(),
        	'oid': self.id_entry.get(),
        	})

        # Commit & arrêt de la connection
        self.conn.commit()
        self.conn.close()

        # Effacement des données
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        self.state_entry.delete(0, 'end')
        self.zipcode_entry.delete(0, 'end')

    def add_record(self):
        " Méthode permettant d'ajouter les données dans le SGBD"

        # Création d'une base de donnée ou connection 
        # à cette base de donnée
        self.conn = sqlite3.connect('database/tree_crm.db')

        # Création d'une instance de curseur
        c = self.conn.cursor()

        # Ajouter une nouvelle donnée (langage SQL)
        c.execute(
            "INSERT INTO customers VALUES (:prenom, :nom, :id, :adresse, :ville, :departement, :cp)",
        	{
        	'prenom': self.fn_entry.get(),
        	'nom': self.ln_entry.get(),
        	'id': self.id_entry.get(),
        	'adresse': self.address_entry.get(),
        	'ville': self.city_entry.get(),
        	'departement': self.state_entry.get(),
        	'cp': self.zipcode_entry.get(),
        	})

        # Commit
        self.conn.commit()

        # Arrêt de la connection
        self.conn.close()

        # Effacement des données
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        self.state_entry.delete(0, 'end')
        self.zipcode_entry.delete(0, 'end')

        # Effacement de la table d'arborescence
        self.my_tree.delete(*self.my_tree.get_children())
        # Équivaut aux instructions dans la méthode remove_all()

        # Récupération des données dans le SGBD
        self.query_database()

    def remove_all(self):
        "Méthode permettant d'effacer toutes les données enregistrées"

        # Message d'information
        response = messagebox.askyesno("Attention !!!",
        "Tout va être supprimé dans la base de données !\nEtes-vous suicidaire ?")
        
        # Si suite au message d'information ci-dessus 
        # on clique sur "OUI"
        if response == 1:

            # Effacement des données dans le widget treeview
            for record in self.my_tree.get_children():
        	    self.my_tree.delete(record)
 
            # Création d'une base de donnée ou connection 
            # à cette base de donnée
            self.conn = sqlite3.connect('database/tree_crm.db')

            # Création d'une instance de curseur
            c = self.conn.cursor()

            # Suppression de toutes les données 
            # dans le SGBD (langage SQL)
            c.execute("DROP TABLE customers")

            # Commit
            self.conn.commit()

            # Arrêt de la connection
            self.conn.close()

            # Effacement des données (voir méthode ci-après) 
            self.clear_entries()
        
            # Création d'une nouvelle table (voir méthode ci-avant)
            self.database()

    def remove_one(self):
        "Méthode permettant de supprimer une donnée enregistrée"

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)

        # Connection à cette base de donnée
        self.conn = sqlite3.connect('database/tree_crm.db')

        # Création d'une instance de curseur
        c = self.conn.cursor()

        # Suppression à partir de la base de données (langage SQL)
        c.execute("DELETE from customers WHERE oid=" + 
                  self.id_entry.get())

        # Commit
        self.conn.commit()

        # Arrêt de la connection
        self.conn.close()

        # Effacement de l'enregisrement affiché
        self.clear_entries()

        # Message d'information
        messagebox.showinfo("Delete!", "Cette donnée est supprimée !")

    def remove_many(self):
        "Méthode permettant d'effacer plusieurs données enregistrées"

        # Message d'information
        response = messagebox.askyesno("Attention !!!",
        "Les données sélectionnées vont être supprimées !\nEtes-vous sûr ?")
        
        # Si suite au message d'information ci-dessus 
        # on clique sur "OUI"
        if response == 1:
            
            # Sélection des données à supprimer
            x = self.my_tree.selection()
            
            # Assignation d'une liste pour le champ 'ID'
            ids_to_delete = []
            
            # Pour chaque donnée sélectionnée
            for record in x :
                # Affichage du champ 'ID' de la donnée sélectionnée
                # print(self.my_tree.item(record, 'values')[2])
                # Ajout de la donnée du champ 'ID' dans la liste
                ids_to_delete.append(
                    self.my_tree.item(record, 'values')[2])     
            
            # Suppression des données dans le widget treeview
            for record in x:
                self.my_tree.delete(record)
            
            # Connection à cette base de donnée
            self.conn = sqlite3.connect('database/tree_crm.db')

            # Création d'une instance de curseur
            c = self.conn.cursor()

            # Suppression à partir de la base de données 
            # (langage SQL)
            c.executemany("DELETE from customers WHERE id = ?",
                          [(a,) for a in ids_to_delete])
            """Pour l'instruction ci-dessus :
            [(a,) for a in ids_to_delete])
            voir le commentaire en début de ce script"""

            # Commit
            self.conn.commit()

            # Arrêt de la connection
            self.conn.close()

            # Effacement de l'enregisrement affiché
            # self.clear_entries()

    def up(self):
        """Méthode permettant de remonter l'enregistrement 
        parmis les données enregistrées"""

        rows = self.my_tree.selection()
        for row in rows:
        	self.my_tree.move(
             row, 
             self.my_tree.parent(row), 
             self.my_tree.index(row)-1)

    def down(self):
        """Mthode permettant de descendre l'enregistrement 
        parmis les données enregistrées"""

        rows = self.my_tree.selection()
        for row in reversed(rows):
        	self.my_tree.move(
             row, 
             self.my_tree.parent(row), 
             self.my_tree.index(row)+1)

    def clear_entries(self):
        """Méthode permettant d'effacer l'enregistrement affiché"""

        # Effacement des données
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        self.state_entry.delete(0, 'end')
        self.zipcode_entry.delete(0, 'end')

    def select_record(self, e):
        """Méthode permettant d'afficher l'enregistrement 
        sélectionné : lien avec la souris -> instruction bind utilisée"""

        # Effacement des données
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        self.state_entry.delete(0, 'end')
        self.zipcode_entry.delete(0, 'end')

        # Sélection des enregistrements
        selected = self.my_tree.focus()

        # Récupération de l'enregistrement sélectionnée
        values = self.my_tree.item(selected, 'values')

        # Affichage des données
        self.fn_entry.insert(0, values[0])
        self.ln_entry.insert(0, values[1])
        self.id_entry.insert(0, values[2])
        self.address_entry.insert(0, values[3])
        self.city_entry.insert(0, values[4])
        self.state_entry.insert(0, values[5])
        self.zipcode_entry.insert(0, values[6])

    def query_database(self):
        "Méthode permettant de lancer la base de données"

        # Création d'une base de donnée 
        # ou connection à cette base de donnée
        self.conn = sqlite3.connect('database/tree_crm.db')

        # création d'une instance de curseur
        c = self.conn.cursor()

        # Exécution de la base de données en recourant 
        # à la génération d'une clé primaire avec 'rowid'
        # (langage SQL)
        c.execute("SELECT rowid, * FROM customers")
        records = c.fetchall()

        # for record in records:
        # 	print(record)

        # Ajout des données à l'écran
        count = 0
        for record in records:
            if count % 2 == 0:
                # Rectification des colonnes 
                # à prendre en compte !!!
                self.my_tree.insert(
                    parent='', 
                    index='end', 
                    iid=count, 
                    text='', 
                	values=(
                     record[1], 
                     record[2], 
                     record[0], 
                     record[4],
                     record[5], 
                     record[6], 
                     record[7]),
                	tags=('evenrow',))
            else:
                self.my_tree.insert(
                    parent='', 
                    index='end',
                    iid=count, 
                    text='', 
                	values=(
                     record[1], 
                     record[2], 
                     record[0], 
                     record[4], 
                     record[5], 
                     record[6], 
                     record[7]),
                	tags=('oddrow',))
            count +=1

        # Commit
        self.conn.commit()

        # Arrêt de la connection
        self.conn.close()

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
