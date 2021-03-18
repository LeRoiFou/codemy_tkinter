"""
Tkinter - Codemy.com #171 : Build A Currency Converter App - Python Tkinter GUI Tutorial #171
Lien : https://www.youtube.com/watch?v=1VVlRgDZ0bg

Dans ce programme on apprend à convertir une devise en une autre devise, pour cela on a recours à une API
(interface de programmation applicative)

https://youtu.be/1VVlRgDZ0bg?t=973

Éditeur : Laurent REYNAUD
Date : 18-03-21
"""

import tkinter
from tkinter import ttk
from tkinter import messagebox
import locale

root = tkinter.Tk()
root.title('Devises')
root.geometry('500x520')

# onglets
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# cadre pour chaque onglet
currency_frame = tkinter.Frame(my_notebook, width=480, height=480)
currency_frame.pack(fill='both', expand=1)
conversion_frame = tkinter.Frame(my_notebook, width=480, height=480)
conversion_frame.pack(fill='both', expand=1)

# ajout des onglets
my_notebook.add(currency_frame, text='Devises')
my_notebook.add(conversion_frame, text='Conversion')

# désactivation du 2ème onglet
my_notebook.tab(1, state='disabled')

#################################################
# ONGLET SUR LES DEVISES
#################################################

def lock():
	# si un des champs du 1er onglet n'est pas rempli...
	if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
		messagebox.showwarning('Attention !', "Tu n'as pas rempli tous les champs !")
	else:
		# désactivation du champ du cours
		home_entry.config(state='disabled')
		# désactivation des champ du cours à convertir et taux du cours
		conversion_entry.config(state='disabled')
		rate_entry.config(state='disabled')
		# activation du 2ème onglet
		my_notebook.tab(1, state='normal')
		# changement des titres des cadres du 2ème onglet
		amount_label.config(text=f"Cours en {home_entry.get()} à convertir en {conversion_entry.get()}")
		converted_label.config(text=f"Équivaut en {conversion_entry.get()}")
		# changement du texte du bouton permettant de convertir le montant saisi
		convert_button.config(text=f"Conversion de la devise {home_entry.get()}")

def unlock():
	# activation des champs du cours, du cours à convertir et du taux du cours
	home_entry.config(state='normal')
	conversion_entry.config(state='normal')
	rate_entry.config(state='normal')
	#  désactivation du 2ème onglet
	my_notebook.tab(1, state='disabled')

# cadre pour saisir la devise à convertir
home = tkinter.LabelFrame(currency_frame, text='Votre devise')
home.pack(pady=20)

# champ de saisi du cours
home_entry = tkinter.Entry(home, font='Helvetica 24', justify='center')
home_entry.pack(pady=10, padx=10)

# cadre pour la conversion de la devise
conversion = tkinter.LabelFrame(currency_frame, text='Conversion de la devise')
conversion.pack(pady=20)

# titre pour la conversion
conversion_label = tkinter.Label(conversion, text='Devise à convertir en...')
conversion_label.pack(pady=10)

# champ de saisi du cours à convertir
conversion_entry = tkinter.Entry(conversion, font='Helvetica 24', justify='center')
conversion_entry.pack(pady=10, padx=10)

# titre pour le taux de conversion
rate_label = tkinter.Label(conversion, text='Taux de conversion')
rate_label.pack(pady=10)

# champ de saisi pour le taux
rate_entry = tkinter.Entry(conversion, font='Helvetica 24', justify='center')
rate_entry.pack(pady=10, padx=10)

# cadre pour le bouton
button_frame = tkinter.Frame(currency_frame)
button_frame.pack(pady=20)

# boutons
lock_button = tkinter.Button(button_frame, text='Bloquer', command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = tkinter.Button(button_frame, text='Débloquer', command=unlock)
unlock_button.grid(row=0, column=1, padx=10)


#################################################
# ONGLET POUR LA CONVERSION
#################################################

def convert():
	# réinitialisation du champ de saisie du montant coverti
	converted_entry.delete(0, 'end')
	# assignation de la conversion du montant du cours actuel x taux de la devise
	conversion = float(rate_entry.get()) * float(amount_entry.get())
	# conversion en deux décimales
	conversion = round(conversion, 2)
	# format numérique avec séparateur de milliers
	locale.setlocale(locale.LC_ALL, 'fr_FR')
	conversion = locale.currency(conversion, False, True, False)
	# mise à jour du montant converti
	converted_entry.insert(0, conversion)

def clear():
	# réinitiation des champs de saisies
	amount_entry.delete(0, 'end')
	converted_entry.delete(0, 'end')


# cadre pour le montant à saisir
amount_label = tkinter.LabelFrame(conversion_frame, text='Montant à convertir')
amount_label.pack(pady=20)

# champ de saisi pour le montant
amount_entry = tkinter.Entry(amount_label, font='Helvetica 24', justify='center')
amount_entry.pack(pady=10, padx=10)

# bouton pour convertir
convert_button = tkinter.Button(amount_label, text='Convertir', command=convert)
convert_button.pack(pady=20)

# Cadre du montant converti
converted_label = tkinter.LabelFrame(conversion_frame, text='Montant converti')
converted_label.pack(pady=20)

# champ de saisi du montant converti
converted_entry = tkinter.Entry(converted_label, font='Helvetica 24', justify='center', bd=0, bg='systembuttonface')
converted_entry.pack(pady=10, padx=10)

# bouton pour effacer
clear_button = tkinter.Button(conversion_frame, text='Effacer', command=clear)
clear_button.pack(pady=20)

# fausse étiquette pour l'espacement
spacer = tkinter.Label(conversion_frame, text='', width=68)
spacer.pack()

root.mainloop()
