"""
Tkinter - Codemy.com #173 : Add Functionality To Treeview CRM App - Python Tkinter GUI Tutorial #173
Lien : https://www.youtube.com/watch?v=I9gQurGuqSI

Dans ce programme on apprend autre chose qu'à convertir une devise en une autre devise, pour cela on a recours à une API
(interface de programmation applicative)...

On apprend à créer un CRM (Customer Relationship Management = Gestion de la relation client) avec le widget treeview
(arborescence) et le recours à une base de données

Dans le script ci-dessous on procède uniquement à une mise en forme

Éditeur : Laurent REYNAUD
Date : 21-04-21
"""

import tkinter
from tkinter import ttk # pour le widget treeview

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title('CRM')
		self.root.geometry('1000x500')
		self.widgets_treeview()
		self.widgets_data()
		self.widgets_buttons()

	def widgets_treeview(self):
		# configuration du widget treeview

		# ajout de style
		style = ttk.Style()

		# choix d'un thème
		style.theme_use('default')

		# configuration des couleurs du treeview
		style.configure("Treeview", 
			background="#D3D3D3",
			foreground="black",
			rowheight=25,
			fieldbackground="#D3D3D3")

		# changement de couleur à la sélection
		style.map('Treeview',
			background=[('selected', '#347083')])

		# créer un cadre pour le treeview (pour la barre de défilement du treview)
		tree_frame = tkinter.Frame(root)
		tree_frame.pack(pady=10)

		# créer une barre de défilement pour le treeview
		tree_scroll = tkinter.Scrollbar(tree_frame)
		tree_scroll.pack(side='right', fill='y')

		# création du treeview
		self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
		self.my_tree.pack()

		# configuration de la barre de défilement
		tree_scroll.config(command=self.my_tree.yview)

		# configuration des en-têtes
		self.my_tree['columns'] = ("Prénom", "Nom", "ID", "Adresse", "Ville", "Etat", "Code postal")

		# format des en-têtes
		self.my_tree.column("#0", width=0, stretch='no')
		self.my_tree.column("Prénom", anchor='w', width=140)
		self.my_tree.column("Nom", anchor='w', width=140)
		self.my_tree.column("ID", anchor='center', width=100)
		self.my_tree.column("Adresse", anchor='center', width=140)
		self.my_tree.column("Ville", anchor='center', width=140)
		self.my_tree.column("Etat", anchor='center', width=140)
		self.my_tree.column("Code postal", anchor='center', width=140)

		# configuration des entêtes lors du passage avec la souris
		self.my_tree.heading("#0", text="", anchor='w')
		self.my_tree.heading("Prénom", text="Prénom", anchor='w')
		self.my_tree.heading("Nom", text="Nom", anchor='w')
		self.my_tree.heading("ID", text="ID", anchor='center')
		self.my_tree.heading("Adresse", text="Adresse", anchor='center')
		self.my_tree.heading("Ville", text="Ville", anchor='center')
		self.my_tree.heading("Etat", text="Département", anchor='center')
		self.my_tree.heading("Code postal", text="Code postal", anchor='center')

		# ajout de fausses données
		data = [
			["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
			["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
			["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
			["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
			["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
			["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
			["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
			["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
			["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
			["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
			["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
			["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
			["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
			["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
			["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
			["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
			["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
			["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
			["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
			["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]	
		]

		# configuration des lignes du treeview
		self.my_tree.tag_configure("oddrow", background="white") # lignes impaires
		self.my_tree.tag_configure("evenrow", background="lightblue") # lignes paires

		# ajout des données à l'écran
		count = 0
		for record in data:
			if count % 2 == 0:
				self.my_tree.insert(parent='', index='end', iid=count, text='', 
					values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
					tags=('evenrow',))
			else:
				self.my_tree.insert(parent='', index='end', iid=count, text='', 
					values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
					tags=('oddrow',))
			count +=1

	def widgets_data(self):
		# configuration des widgets pour l'enregistrement des données

		# ajout des champs de saisies pour les enregistrements
		data_frame = tkinter.LabelFrame(root, text='Enregistrements')
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
		# configuration des widgets des boutons

		# ajout de boutons
		button_frame = tkinter.LabelFrame(root, text='Commandes')
		button_frame.pack(fill='x', expand='yes', padx=20)

		update_button = tkinter.Button(button_frame, text='Modifier', command=self.update_record)
		update_button.grid(row=0, column=0, padx=10, pady=10)

		add_button = tkinter.Button(button_frame, text='Ajouter')
		add_button.grid(row=0, column=1, padx=10, pady=10)

		remove_all_button = tkinter.Button(button_frame, text='Tout supprimer', command=self.remove_all)
		remove_all_button.grid(row=0, column=2, padx=10, pady=10)

		remove_one_button = tkinter.Button(button_frame, text='Supprimer une donnée', command=self.remove_one)
		remove_one_button.grid(row=0, column=3, padx=10, pady=10)

		remove_many_button = tkinter.Button(button_frame, text='Supprimer plusieurs données', command=self.remove_many)
		remove_many_button.grid(row=0, column=4, padx=10, pady=10)

		move_up_button = tkinter.Button(button_frame, text='Monter', command=self.up)
		move_up_button.grid(row=0, column=5, padx=10, pady=10)

		move_down_button = tkinter.Button(button_frame, text='Descendre', command=self.down)
		move_down_button.grid(row=0, column=6, padx=10, pady=10)

		select_record_button = tkinter.Button(button_frame, text="Effacer les données affichées", command=self.clear_entries)
		select_record_button.grid(row=0, column=7, padx=10, pady=10)

		# à chaque fois qu'on sélectionne un enregistrement celui-ci s'affiche
		self.my_tree.bind("<ButtonRelease-1>", self.select_record)

	def update_record(self):
		# méthode permettant de modifier la donnée enregistrée

		# récupération de la donnée enregistrée
		selected = self.my_tree.focus()
		self.my_tree.item(selected, text="", values=(self.fn_entry.get(), self.ln_entry.get(), self.id_entry.get(),
			self.address_entry.get(), self.city_entry.get(), self.state_entry.get(), self.zipcode_entry.get()))

		# effacement des données
		self.fn_entry.delete(0, 'end')
		self.ln_entry.delete(0, 'end')
		self.id_entry.delete(0, 'end')
		self.address_entry.delete(0, 'end')
		self.city_entry.delete(0, 'end')
		self.state_entry.delete(0, 'end')
		self.zipcode_entry.delete(0, 'end')

	def remove_all(self):
		# méthode permettant d'effacer toutes les données enregistrées

		for record in self.my_tree.get_children():
			self.my_tree.delete(record)

	def remove_one(self):
		# méthode permettant de supprimer une donnée enregistrée

		x = self.my_tree.selection()[0]
		self.my_tree.delete(x)

	def remove_many(self):
		# méthode permettant d'effacer plusieurs données enregistrées

		x = self.my_tree.selection()[0]
		for record in x:
			self.my_tree.delete(record)

	def up(self):
		# méthode permettant de remonter l'enregistrement parmis les données enregistrées

		rows = self.my_tree.selection()
		for row in rows:
			self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)-1)

	def down(self):
		# méthode permettant de descendre l'enregistrement parmis les données enregistrées

		rows = self.my_tree.selection()
		for row in reversed(rows):
			self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)+1)

	def clear_entries(self):
		# méthode permettant d'effacer l'enregistrement affiché

		# effacement des données
		self.fn_entry.delete(0, 'end')
		self.ln_entry.delete(0, 'end')
		self.id_entry.delete(0, 'end')
		self.address_entry.delete(0, 'end')
		self.city_entry.delete(0, 'end')
		self.state_entry.delete(0, 'end')
		self.zipcode_entry.delete(0, 'end')

	def select_record(self, e):
		# méthode permettant d'afficher l'enregistrement sélectionné : lien avec la souris -> instruction bind utilisée

		# effacement des données
		self.fn_entry.delete(0, 'end')
		self.ln_entry.delete(0, 'end')
		self.id_entry.delete(0, 'end')
		self.address_entry.delete(0, 'end')
		self.city_entry.delete(0, 'end')
		self.state_entry.delete(0, 'end')
		self.zipcode_entry.delete(0, 'end')

		# sélection des enregistrements
		selected = self.my_tree.focus()

		# récupération de l'enregistrement sélectionnée
		values = self.my_tree.item(selected, 'values')

		# affichage des données
		self.fn_entry.insert(0, values[0])
		self.ln_entry.insert(0, values[1])
		self.id_entry.insert(0, values[2])
		self.address_entry.insert(0, values[3])
		self.city_entry.insert(0, values[4])
		self.state_entry.insert(0, values[5])
		self.zipcode_entry.insert(0, values[6])


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()