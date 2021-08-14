"""
Récapitulatif des fonctions natives dans tkinter

Touches raccourcies :
-> pour tout plier : CTRL + K + 1
-> pour tout déplier : CTRL + K + J

Éditeur : Laurent REYNAUD
Date : 16-05-2021
"""

import tkinter
from tkinter import ttk # widgets combobox...
from tkinter import font # police d'écriture
import time

class Add:
	"""La fonction add permet d'ajouter un widget sur un autre widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index048_panedWindows
	index064_noteBook
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		# Configuration du panneau de fenêtre qui s'étendra 
  		# sur toute la fenêtre
		panel_1 = tkinter.PanedWindow(bd=4, relief='raised', bg='red')
  
		# extension sur toute la longueur et la largeur de la fenêtre
		panel_1.pack(fill='both', expand=1)  

		# Configuration du panneau haut à l'intérieur du panneau ci-avant
		panel_2 = tkinter.PanedWindow(panel_1, orient='vertical', bd=4, relief='raised', bg='blue')
		panel_1.add(panel_2)

class After:
    """La fonction after permet de mettre à jour un widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index079_timeLocale
	index164_animateWidgets
	
	"""
    
    def __init__(self, root):
        self.root = root
        self.widgets()
        self.clock()
    
    def widgets(self):
        
        """Configuration étiquette résultat (temps actuel)"""
        self.my_label = tkinter.Label(root, text='', font='Helvetica 48', fg='green', bg='black')
        self.my_label.pack(pady=20)

        """Configuration d'une deuxième étiquette (date actuelle)"""
        self.my_label2 = tkinter.Label(root, text='', font='Helvetica 14')
        self.my_label2.pack(pady=10)
        
    def clock(self):
        """Affichage de l'heure : minute : seconde actuelles :
        -> On déclare les variables de temps avec l'instruction strftime()
        -> L'étiquette résultat affiche le temps actuelle grâce à l'instruction config()
        -> Mise à jour de l'étiquette avec l'instruction after() 
        avec pour arguments le temps en millisecondes et 
        une fonction récursive (fonction s'appelant elle-même)"""
        
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        day = time.strftime("%A")
        numb_day = time.strftime("%e")
        month = time.strftime("%B")
        year = time.strftime("%Y")
        # affichage du temps actuel
        self.my_label.config(text=hour + ':' + minute + ':' + second)
        # mise à jour du temps avec en arguments : temps en millisecondes, fonction  
        self.my_label.after(1000, self.clock)  
        # affichage de la date actuelle
        self.my_label2.config(text=day + ' ' + numb_day + ' ' + month + ' ' + year)   

class Bind:
	"""La fonction bind qui comprend deux arguments (<évènement>, action) permet d'intervenir sur un widget
	en recourant aux touches du clavier ou à la souris
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index044_bind
	index045_bindComboBox&OptionMenu
	index069_canvas&ArrowKeys
	index070_canvas&ArrowKeys&Images
	index071_canvas&Mouse&Images
	index075_mouse&Images
	index085_mouseColorButtonPopupMessage
	index096_fullScreenScrollBar
	index135_transparentWindow
	index137_menuPopupsBind
	index149_canvasEntryBoxes
	index162_search
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

class ClipBoard:
    """La fonction clipboard_xxx() a plusieurs fonctionnalités :
    -> clipboard_delete() : réinitialise les données dans le presse-papier
    -> clipboard_append() : ajout des données dans le presse-papier
    -> clipboard_get() : contenu des données dans le presse-papier
    Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index108_buildATextEditor et suivants
	"""
    
    def __init__(self, root):
        self.root = root
        self.widgets()
        
    def widgets(self):
        
        self.my_text = tkinter.Text(root, width=40, height=5,)
        self.my_text.pack()
        
        my_button_copy = tkinter.Button(
			root,
   			text='Copier',
			command=self.copy_it)
        my_button_copy.pack()
        
        # Bouton contenu dans le presse-papier
        my_button_content = tkinter.Button(
            root, 
            text="Contenu", 
            command=self.content_it)
        my_button_content.pack()
        
        self.my_label = tkinter.Label(root, text="")
        self.my_label.pack()
        
    def copy_it(self):
        """Méthode permettant de réinitialiser le contenu dans le 
        presse-papier et de copier les données sélectionnées"""
        
        # Texte sélectionné
        selected = self.my_text.selection_get()
        
        # Réinitialisation des données dans le presse-papier
        root.clipboard_clear()
        
        # Ajout des données séléectionnées dans le presse-papier
        root.clipboard_append(selected)
              
    def content_it(self):
        "Méthode permettant d'afficher le contenu du presse-papier"
        
        # contenu dans le presse-papier
        selected = root.clipboard_get()
        
        # affichage du contenu dans le presse-papier
        self.my_label.config(text=f"Contenu du presse-papier : {selected}")

class Config:
	"""La fonction config() permet de modifier la saisie faite dans le widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index061_listBox
	index062_listBox&ScrollBars
	index063_config&Update
	index065_multipleEntry
	index066_imageButton&Border
	index067_entryAsInteger
	index071_canvas&Mouse&Images
	index072_calendar
	index074_OS
	index075_mouse&Images
	index079_timeLocale
	index085_mouseColorButtonPopupMessage
	index097_threads
	index098_spinboxes
	index099_textBox
	index102_textBoxBoldItalics
	index103_textBoxUndoRedoTitle
	index105_buildATextEditor et suivants
	index113_ticTacToeGame
	index114_Excel
	index123_messageBoxCustom
	index124_ExcelListbox
	index127_menuDisableDelete
	index128_timeLocale
	index129_modules1
	index130_spinboxReset
	index135_transparentWindow
	index137_menuPopupsBind
 	index141_memoryGame
	index142_memoryGame
	index144_rockPaperScissorsGame
	et suivants...
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
	index152_dependentComboboxListbox
	index163_beaufifulSoupBitcoinPrice
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
    Sélectionnées. À défaut de cette instruction, les données à supprimer seront 
    effacées une par une à chaque fois qu'on appuye sur le bouton concerné
    Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index062_listBox&ScrollBars
	index155_todoList et suivants
 	"""

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
	"""La fonction delete(0, 'end') permet d'effacer les données 
 	affichées dans le widget
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
	index099_textBox
	index105_buildATextEditor et suivants
	index125_ExcelTreeview
	index127_menuDisableDelete
	index143_pdf
	index149_canvasEntryBoxes
	index152_dependentComboboxListbox
	index153_serialization2
	index154_todoList et suivants
	index157_colorChangingNumberGame
	index162_search
	index168_foreinLanguageFlashCard
	index169_wikipediaSearch
	index170_passwordGenerator
	index171_currencyConverter
	index182_CRM
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
	index123_messageBoxCustom
	index139_splashScreen
	index149_canvasEntryBoxes
	index182_CRM
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
	"""La fonction focus() permet d'insérer automatiquement le selecteur
 	de la souris dans le widget concerné
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index182_CRM
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
	index065_multipleEntry
	index067_entryAsInteger
 	index080_resizeWindow
	index098_spinboxes
	index099_textBox
	index124_ExcelListbox
	index129_modules1
	index135_transparentWindow
	index144_rockPaperScissorsGame
	index149_canvasEntryBoxes
	index152_dependentComboboxListbox
	index153_serialization1
	index153_serialization2
	index156_todoList
	index157_colorChangingNumberGame
	index158_resizeWindowControlPanel
	index162_search
	index168_foreinLanguageFlashCard
	index170_passwordGenerator
	index171_currencyConverter
	index182_CRM
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

class Hide:
	"""La fonction hide() permet de cacher un onglet
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index064_noteBook
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		# Configuration des onglets
		self.my_notebook = ttk.Notebook(root)
		self.my_notebook.pack()

        # Configuration des cadres"""
		my_frame1 = tkinter.Frame(self.my_notebook, width=500, height=500, bg='blue')
		my_frame1.pack(fill='both', expand=1)
		my_frame2 = tkinter.Frame(self.my_notebook, width=500, height=500, bg='red')        
		my_frame2.pack(fill='both', expand=1)

        # Ajout des onglets
		self.my_notebook.add(my_frame1, text='Onglet 1')
		self.my_notebook.add(my_frame2, text='Onglet 2')

        # bouton
		my_button = tkinter.Button(my_frame1, text="Effacer l'onglet n° 2", command=self.hide_it)
		my_button.pack()

	def hide_it(self):
		
		self.my_notebook.hide(1)

	"""La fonction index('insert') permet d'insérer une image là où se trouve
	le curseur de la souris
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index101_textBoxImagesScrollBar
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		self.my_text = tkinter.Text(root)
		self.my_text.pack()

		my_button = tkinter.Button(root, text="Insérer", command=self.func_index)
		my_button.pack()

	def func_index(self):
		
		# position = self.my_text.index('insert')
		self.my_text.insert('end', 'e')

class Insert:
	"""La fonction insert(0, argument) permet d'insérer des données 
 	dans le widget Entry / Text...
	Pour le widget Text la fonction est insert('end', argument)
	Mais pour le cours index143_pdf la fonction est insert(1.0, argument)...
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index005_calculatrice
	index006_calculatrice
	index007_calculatrice
	index022_dataBases
	index023_dataBases
	index061_listBox
	index062_listBox&ScrollBars
	index100_textBoxFiledialog
	index101_textBoxImagesScrollBar
	index102_textBoxBoldItalics
	index103_textBoxUndoRedoTitle
	index105_buildATextEditor et suivants
	index125_ExcelTreeview
	index143_pdf
	index152_dependentComboboxListbox
	index153_serialization1
	index153_serialization2
	index154_todoList et suivants
	index162_search
	index169_wikipediaSearch
	index170_passwordGenerator
	index171_currencyConverter
	index182_CRM
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

class Move:
	"""La fonction 'move' permet de déplacer un widget avec l'instruction bind
	et les touches du clavier
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index069_canvas&ArrowKeys
	index070_canvas&ArrowKeys&Images
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):

		# Tailles et coordonnées en variables
		w = 600
		h = 400
		x = w // 2
		y = h // 2

		# Configuration d'un canvas sous fond blanc
		self.my_canvas = tkinter.Canvas(root, width=w, height=h, bg='white')
		self.my_canvas.pack(pady=20)

		# Configuration d'un cercle"""
		self.my_circle = self.my_canvas.create_oval(x, y, x + 10, y + 10)

		# Configuration des touches 'qsdz' du clavier pour déplacer le cercle
		root.bind("<Key>", self.pressing)

		# Configuration des touches directionnelles du clavier pour déplacer le cercle
		root.bind('<Left>', self.left)
		root.bind('<Right>', self.right)
		root.bind('<Up>', self.up)
		root.bind('<Down>', self.down)

	def left(self, event):
   			
		# Déplacement de 10 pixels à la gauche
		x = -10
		y = 0
		self.my_canvas.move(self.my_circle, x, y)

	def right(self, event):
        
		# Déplacement de 10 pixels à la droite
		x = 10
		y = 0
		self.my_canvas.move(self.my_circle, x, y)

	def up(self, event):
	    
		# Déplacement de 10 pixels en haut
		x = 0
		y = -10
		self.my_canvas.move(self.my_circle, x, y)

	def down(self, event):
	    
		# Déplacement de 10 pixels en bas
		x = 0
		y = 10
		self.my_canvas.move(self.my_circle, x, y)

	def pressing(self, event):
	   
		# Déplacement avec les touches 'qsdz'
		x = 0
		y = 0
		if event.char == 'q': x = -10  # déplacement à gauche
		if event.char == 's': y = 10  # déplacement en bas
		if event.char == 'd': x = 10  # déplacement à droite
		if event.char == 'z': y = -10  # déplacement en haut
		self.my_canvas.move(self.my_circle, x, y)

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
	"""La fonction select() permet de sélectionner automatiquement la case / l'onglet
	du widget concerné et à l'inverse,	la fonction deselect() permet de décocher 
	automatiquement la case / l'onglet
	La Fonction selection() permet d'accéder au composant d'un widget
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index017_checkBoxes
	index064_noteBook
	index182_CRM (selection())
	"""

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		
		check = tkinter.Checkbutton(root, text="Case déjà cochée !")
		check.select()
		check.pack()

class SelectionGet:
    """La fonction selection_get() permet de sélectionner un texte ou une partie
    du texte dans le widget text et dans l'exemple ci-dessous, de l'afficher
	index102_textBoxBoldItalics
	index107_buildATextEditor et suivants
	"""
    
    def __init__(self, root):
        self.root = root
        self.widgets()
        
    def widgets(self):
        
        self.my_text = tkinter.Text(root, width=40, height=5,)
        self.my_text.pack()
        
        my_button = tkinter.Button(root, text="Sélectionner", command=self.select_it)
        my_button.pack()
        
        self.my_label = tkinter.Label(root, text="")
        self.my_label.pack()
        
    def select_it(self):
        "Méthode affichant le texte sélectionné dans le widget Text"
        
        my_select = self.my_text.selection_get()
        self.my_label.config(text=my_select)

class Set:
	"""La fonction set() permet de modifier le texte affiché en recourant aux variables de contrôles
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index012_radioButton
	index018_optionMenu
	index045_bindComboBox&OptionMenu
	index130_spinboxReset
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

class Tag:
    """La fonction tag() permet de modifier la mise en forme de la police 
    d'écriture dans le widget Text, mais également présent changer la
    configuration du widget treeview avec l'instruction tag_configure
	Fonction retrouvée dans les cours suivants dans codemy_tkinter :
	index102_textBoxBoldItalics
	index103_textBoxUndoRedoTitle
	index109_buildATextEditor et suivants
	index182_CRM (tag_configure)
	"""
    
    def __init__(self, root):
        self.root = root
        self.widgets()
        
    def widgets(self):
        
        self.my_text = tkinter.Text(root, width=40, 
                                    height=5, 
                                    font="Helvetica 20",
                                    selectbackground='blue')
        self.my_text.grid(row=0, column=0, columnspan=2)
        
        my_button_bold = tkinter.Button(root, text="Gras", command=self.bold_it)
        my_button_bold.grid(row=1, column=0)
        
        my_button_italic = tkinter.Button(root, text="Italique", command=self.italic_it)
        my_button_italic.grid(row=1, column=1)  
        
    def bold_it(self):
        "Police d'écriture en gras"
        
        # Récupération de la police d'écriture
        bold_font = font.Font(self.my_text, self.my_text.cget('font'))  
        
        # Configuration pour la mise en gras de l'écriture
        bold_font.config(weight='bold') 
        self.my_text.tag_config('bold', font=bold_font)
        
        # Caractères sélectionnés
        current_tags = self.my_text.tag_names('sel.first')
        if 'bold' in current_tags:
            """Si le texte est déjà en gras... 
            supprimer cette mise en forme"""
            self.my_text.tag_remove('bold', 'sel.first', 'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            self.my_text.tag_add('bold', 'sel.first', 'sel.last')   
    
    def italic_it(self):
        "Police d'écriture en italique"
        
        # Récupération de la police d'écriture
        italic_font = font.Font(self.my_text, self.my_text.cget('font'))  
        
        # Configuration pour la mise en gras de l'écriture
        italic_font.config(slant='italic') 
        self.my_text.tag_config('italic', font=italic_font)
        
        # Caractères sélectionnés
        current_tags = self.my_text.tag_names('sel.first')
        if 'italic' in current_tags:
            """Si le texte est déjà en italique... 
            supprimer cette mise en forme"""
            self.my_text.tag_remove('italic', 'sel.first', 'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            self.my_text.tag_add('italic', 'sel.first', 'sel.last') 

if __name__ == '__main__':
	root = tkinter.Tk()
	# add = Add(root)
	# after = After(root)
	# bind = Bind(root)
	# clipboard = ClipBoard(root)
	# config = Config(root)
	# current = Current(root)
	# curselection = Curselection(root)
	# delete = Delete(root)
	# destroy = Destroy(root)
	# focus = Focus(root)
	# forget = Forget(root)
	# get = Get(root)
	# hide = Hide(root)
	# insert = Insert(root)
	# move = Move(root)
	# quit = Quit(root)
	# select = Select(root)
	# selection_get = SelectionGet(root)
	# set = Set(root)
	# tag = Tag(root)
	root.mainloop()
