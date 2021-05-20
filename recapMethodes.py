"""
Récapitulatif des fonctions préétablies dans tkinter

Touches raccourcies :
-> pour tout plier : CTRL + K + 1
-> pour tout déplier : CTRL + K + J

Éditeur : Laurent REYNAUD
Date : 16-05-2021
"""

import tkinter
from tkinter import ttk # widget combobox

class Add:
	"""La fonction add permet d'ajouter un widget sur un autre widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index048_panedWindows
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		# Configuration du panneau de fenêtre qui s'étendra sur toute la fenêtre
		panel_1 = tkinter.PanedWindow(bd=4, relief='raised', bg='red')
		panel_1.pack(fill='both', expand=1)  # extension sur toute la longueur et la largeur de la fenêtre

		# Configuration du panneau haut à l'intérieur du panneau ci-avant
		panel_2 = tkinter.PanedWindow(panel_1, orient='vertical', bd=4, relief='raised', bg='blue')
		panel_1.add(panel_2)

class Bind:
	"""La fonction bind qui comprend deux arguments (<évènement>, action) permet d'intervenir sur un widget
	en recourant aux touches du clavier ou à la souris
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index044_bind
	index045_bindComboBox&OptionMenu
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		my_button = tkinter.Button(root, text='Appuye-moi !')
		 # sélection automatique du bouton
		my_button.focus()
		# lorsqu'on clique avec le bouton de droite la méthode clicker() s'active
		# my_button.bind('<Button-3>', self.clicker)
		# lorsque la souris va sur le bouton, la méthode clicker() s'active
		my_button.bind('<Enter>', self.clicker)
		# en appuyant sur Entrée la méthode clicker() s'active
		# my_button.bind('<Return>', self.clicker)
		# en appuyant sur n'importe quelle touche du clavier la méthode clicker() s'active
		# my_button.bind('<Key>', self.clicker)
		
		my_button.pack()

	def clicker(self, e):

		my_label = tkinter.Label(root, text='Affichage du texte')
		my_label.pack()

class Config:
	"""La fonction config() permet de modifier la saisie faite dans le widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index061_listBox
	index062_listBox&ScrollBars
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_entry = tkinter.Entry(root)
		self.my_entry.pack()

		my_button = tkinter.Button(root, text="Modifier", command=self.func_config)
		my_button.pack()

		self.my_label = tkinter.Label(root, text="")
		self.my_label.pack()

	def func_config(self):
		
		insert = self.my_entry.get()
		self.my_label.config(text=insert)

class Current:

	"""La fonction current() permet d'afficher par défaut une donnée
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index045_bindComboBox&OptionMenu
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		options = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

		self.myCombo = ttk.Combobox(root, value=options)
		self.myCombo.current(2)  # affichage par défaut : mercredi
		self.myCombo.pack()

class Curselection:

	"""la fonction reversed permet de prendre d'un seul coup toutes les données 
    électionnées. À défaut de cette instruction, les données à supprimer seront 
    effacées une par une à chaque fois qu'on appuye sur le bouton concerné
    Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index062_listBox&ScrollBars"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):

		self.my_listbox = tkinter.Listbox(root, justify='center', selectmode='multiple')
		self.my_listbox.pack()

		my_list = ['Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 
	        'Un', 'Deux', 'Trois', 'Un', 'Deux','Trois', 'Un', 'Deux', 'Trois', 'Un',
	        'Deux', 'Trois']

		for item in my_list:
	        # insertion des données de la liste ci-dessus dans la zone de liste
			self.my_listbox.insert('end', item)

		my_button = tkinter.Button(root, text="Supprimer tout", command=self.delete_multiple)
		my_button.pack()

	def delete_multiple(self):

		for item in reversed(self.my_listbox.curselection()):
			self.my_listbox.delete(0, 'end')

class Delete:
	"""La fonction delete(0, 'end') permet d'effacer les données affichées dans le widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index005_calculatrice
	index006_calculatrice
	index007_calculatrice
	index020_dataBases
	index021_dataBases
	index022_dataBases
	index023_dataBases
	index038_entry&Height
	index041_removeLabels
	index042_overwriteLabels
	index061_listBox
	index062_listBox&ScrollBars
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_entry = tkinter.Entry(root)
		self.my_entry.pack()

		my_buttonDelete = tkinter.Button(root, text="Effacer", command=lambda:self.func_delete())
		my_buttonDelete.pack()

	def func_delete(self):

		self.my_entry.delete(0, 'end')

class Destroy:
	"""La fonction 'destroy' permet d'éviter de fermer automatiquement le widget à la différence de 'quit'
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index005_calculatrice
	index006_calculatrice
	index007_calculatrice
	index023_dataBases
	index042_overwriteLabels
	index050_deleteFrameChildrenWidgets
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):

		my_button1 = tkinter.Button(root, text="Clique pour une nouvelle fenêtre", command=self.open_window)
		my_button1.pack()

	def open_window(self):

		top = tkinter.Toplevel()

		my_label = tkinter.Label(top, text="Félicitations ! Tu as ouvert une nouvelle fenêtre")
		my_label.pack()

		my_button2 = tkinter.Button(top, text="Quitter cette fenêtre", command=top.destroy)
		my_button2.pack()

class Focus:
	"""La fonction focus() permet d'insérer automatiquement le selecteur de la souris dans le widget concerné
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_entry = tkinter.Entry(root, justify="center")
		self.my_entry.focus()
		self.my_entry.pack()

class Forget:
	"""La fonction forget() permet de faire disparaître un wiget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index041_removeLabels
	index042_overwriteLabels
	index047_menus&Frame
	index050_deleteFrameChildrenWidgets
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):

		self.my_label = tkinter.Label(root, text="Ce texte ne disparaîtra jamais !")
		self.my_label.pack()

		my_button = tkinter.Button(root, text="Faire disparaître ce texte", command=self.myDelete)
		my_button.pack()

	def myDelete(self):

		self.my_label.pack_forget()

class Get:
	"""La fonction get() permet de récupérer les données saisies dans un widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index006_calculatrice
	index007_calculatrice
	index018_optionMenu
	index020_dataBases
	index021_dataBases
	index022_dataBases
	index023_dataBases
	index038_entry&Height
	index042_overwriteLabels
	index045_bindComboBox&OptionMenu
	index061_listBox
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_entry = tkinter.Entry(root)
		self.my_entry.pack()

		my_button = tkinter.Button(root, text="Récupérer", command=self.func_get)
		my_button.pack()

		self.my_label = tkinter.Label(root, text="")
		self.my_label.pack()

	def func_get(self):
		
		insert = self.my_entry.get()
		self.my_label.config(text=insert)

class Insert:
	"""La fonction insert(0, argument) permet d'insérer des données dans le widget Entry
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index005_calculatrice
	index006_calculatrice
	index007_calculatrice
	index022_dataBases
	index023_dataBases
	index061_listBox
	index062_listBox&ScrollBars
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_entry = tkinter.Entry(root)
		self.my_entry.pack()

		my_button = tkinter.Button(root, text="Insérer", command=lambda:self.func_insert("Test ! "))
		my_button.pack()

	def func_insert(self, e):
		
		self.my_entry.insert(0, e)

class Quit:
	"""La fonction 'quit' permet de quitter l'application
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index008_icon&quit
	index047_menus&Frame
	index050_deleteFrameChildrenWidgets
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		my_button = tkinter.Button(root, text="Quitter l'application", command=root.quit)
		my_button.pack()

class Select:
	"""La fonction select() permet de cocher automatiquement la case dans le widget concerné et à l'inverse,
	la fonction deselect() permet de décocher automatiquement la case
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index017_checkBoxes
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		check = tkinter.Checkbutton(root, text="Case déjà cochée !")
		check.select()
		check.pack()

class Set:
	"""La fonction set() permet de modifier le texte affiché et il est utilisé surtout avec le widget Label
	en recourant aux variables de contrôles
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index012_radioButton
	index018_optionMenu
	index045_bindComboBox&OptionMenu
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_labelVar = tkinter.StringVar()  # variables de contrôles
		self.my_labelVar.set("Ce texte ne sera jamais modifié !")
		my_label = tkinter.Label(root, textvariable=self.my_labelVar)
		my_label.pack()

		my_button = tkinter.Button(root, text="Modifier ce maudit texte !", command=self.update)
		my_button.pack()

	def update(self):

		self.my_labelVar.set("Le texte a été modifié !!!")

if __name__ == '__main__':
	root = tkinter.Tk()
	# add = Add(root)
	# bind = Bind(root)
	# config = Config(root)
	# current = Current(root)
	curselection = Curselection(root)
	# delete = Delete(root)
	# destroy = Destroy(root)
	# focus = Focus(root)
	# forget = Forget(root)
	# get = Get(root)
	# insert = Insert(root)
	# quit = Quit(root)
	# select = Select(root)
	# set = Set(root)
	root.mainloop()
