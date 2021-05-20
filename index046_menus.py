"""
Tkinter - Codemy.com #46 : Menu Bars With tKinter
Lien : https://www.youtube.com/watch?v=ZS2_v_zsPTg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=46

Création d'une barre de menus

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		root.geometry('400x400')
		root.title("Titre !")
		self.widgets()

	def widgets(self):

		# Configuration de la barre de menus
		my_menu = tkinter.Menu(root)
		root.config(menu=my_menu)

		# 1er titre de la barre de menus : 'Fichier'
		file_menu = tkinter.Menu(my_menu, tearoff=0)
		my_menu.add_cascade(label='Fichier', menu=file_menu)

		# Ajout des difféntes commandes du menu 'Fichier'
		file_menu.add_command(label='Nouveau...', command=self.our_command)
		file_menu.add_separator()
		file_menu.add_command(label='Sortie', command=root.quit)

		# 2ème titre de la barre de menus : 'Édition'
		edit_menu = tkinter.Menu(my_menu, tearoff=0)
		my_menu.add_cascade(label='Édition', menu=edit_menu)

		# Ajout des difféntes commandes du menu 'Édition'
		edit_menu.add_command(label='Couper', command=self.our_command)
		edit_menu.add_command(label='Coller', command=self.our_command)

		# 3ème titre de la barre de menus : 'Options'
		options_menu = tkinter.Menu(my_menu, tearoff=0)
		my_menu.add_cascade(label='Options', menu=options_menu)

		# Ajout des difféntes commandes du menu 'Options'
		options_menu.add_command(label='Rechercher', command=self.our_command)
		options_menu.add_command(label='Annuler', command=self.our_command)

	def our_command(self):
		myLabel = tkinter.Label(root, text='Vous avez cliqué sur un menu déroulant !').pack()

if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()