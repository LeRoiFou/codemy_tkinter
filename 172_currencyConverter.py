"""
Tkinter - Codemy.com #172 : Build a CRM Tool With Treeview And Database - Python Tkinter GUI Tutorial #172
Lien : https://www.youtube.com/watch?v=G9seoA3Mv4Y

Dans ce programme on apprend autre chose qu'à convertir une devise en une autre devise, pour cela on a recours à une API
(interface de programmation applicative)...

On apprend à créer un CRM (Customer Relationship Management = Gestion de la relation client) avec le widget treeview
(arborescence) et le recours à une base de données

Dans le script ci-dessous on procède uniquement à une mise en forme

Éditeur : Laurent REYNAUD
Date : 24-03-21
"""

import tkinter
from tkinter import ttk # pour le treeview

root = tkinter.Tk()
root.title('CRM')
root.geometry('1000x500')

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
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# configuration de la barre de défilement
tree_scroll.config(command=my_tree.yview)

# configuration des en-têtes
my_tree['columns'] = ("Prénom", "Nom", "ID", "Adresse", "Ville", "Etat", "Code postal")

# format des en-têtes
my_tree.column("#0", width=0, stretch='no')
my_tree.column("Prénom", anchor='w', width=140)
my_tree.column("Nom", anchor='w', width=140)
my_tree.column("ID", anchor='center', width=100)
my_tree.column("Adresse", anchor='center', width=140)
my_tree.column("Ville", anchor='center', width=140)
my_tree.column("Etat", anchor='center', width=140)
my_tree.column("Code postal", anchor='center', width=140)

# configuration des entêtes lors du passage avec la souris
my_tree.heading("#0", text="", anchor='w')
my_tree.heading("Prénom", text="Prénom", anchor='w')
my_tree.heading("Nom", text="Nom", anchor='w')
my_tree.heading("ID", text="ID", anchor='center')
my_tree.heading("Adresse", text="Adresse", anchor='center')
my_tree.heading("Ville", text="Ville", anchor='center')
my_tree.heading("Etat", text="Département", anchor='center')
my_tree.heading("Code postal", text="Code postal", anchor='center')

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
my_tree.tag_configure("oddrow", background="white") # lignes impaires
my_tree.tag_configure("evenrow", background="lightblue") # lignes paires

# ajout des données à l'écran
global count
count = 0

for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', 
			values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
			tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', 
			values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
			tags=('oddrow',))
	count +=1

# ajout des champs de saisies pour les enregistrements
data_frame = tkinter.LabelFrame(root, text='Enregistrements')
data_frame.pack(fill='x', expand='yes', padx=20)

fn_label = tkinter.Label(data_frame, text='Prénom')
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = tkinter.Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = tkinter.Label(data_frame, text='Nom')
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = tkinter.Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = tkinter.Label(data_frame, text='ID')
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = tkinter.Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = tkinter.Label(data_frame, text='Adresse')
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = tkinter.Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = tkinter.Label(data_frame, text='Ville')
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = tkinter.Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = tkinter.Label(data_frame, text='Etat')
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = tkinter.Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = tkinter.Label(data_frame, text='Code postal')
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = tkinter.Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)

# ajout de boutons
button_frame = tkinter.LabelFrame(root, text='Commandes')
button_frame.pack(fill='x', expand='yes', padx=20)

update_button = tkinter.Button(button_frame, text='Modifier')
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = tkinter.Button(button_frame, text='Ajouter')
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = tkinter.Button(button_frame, text='Tout effacer')
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = tkinter.Button(button_frame, text='Effacer une donnée')
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = tkinter.Button(button_frame, text='Effacer des données')
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = tkinter.Button(button_frame, text='Déplacer en haut')
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = tkinter.Button(button_frame, text='Déplacer en bas')
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = tkinter.Button(button_frame, text='Selection des enregistrements')
select_record_button.grid(row=0, column=7, padx=10, pady=10)

root.mainloop()
