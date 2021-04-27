"""
Tkinter - Codemy.com #116 : Treeview
Lien : https://www.youtube.com/watch?v=YTqDYmfccQU&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=116

Dans ce programme on apprend à crééer une arborescence

Première présentation de l'arborescence avec la 1ère colonne 'Etiquette' qui s'affiche automatiquement dans ce widget

Éditeur : Laurent REYNAUD
Date : 21-12-20
"""

import tkinter
from tkinter import ttk  # pour le widget treeview

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.iconbitmap('images/Logo.ico')
		self.root.title('Titre !')
		self.root.geometry('500x500')
		self.widgets()

	def widgets(self):

		# Configuration de l'arborescence
		my_tree = ttk.Treeview(root)

		# Configuration des colonnes
		my_tree['columns'] = ('Name', 'ID', 'Favorite pizza')

		# Formatage des colonnes
		my_tree.column('#0', width=120, minwidth=25)  # colonne fantôme
		my_tree.column('Name', anchor='w', width=120)
		my_tree.column('ID', anchor='center', width=80)
		my_tree.column('Favorite pizza', anchor='w', width=120)

		# Configuration des en-têtes
		my_tree.heading('#0', text='Etiquette', anchor='w')
		my_tree.heading('Name', text='Nom', anchor='w')
		my_tree.heading('ID', text='ID', anchor='center')
		my_tree.heading('Favorite pizza', text='Pizza préférée', anchor='w')

		# Ajout des données dans les colonnes
		my_tree.insert(parent='', index='end', iid=0, text='Parent', values=('John', 1, 'Calzone'))
		my_tree.insert(parent='', index='end', iid=1, text='Parent', values=('Albert', 2, 'Fromages'))
		my_tree.insert(parent='', index='end', iid=2, text='Parent', values=('Marius', 3, 'Champignons'))
		my_tree.insert(parent='', index='end', iid=3, text='Parent', values=('Bob', 4, 'Anchois'))
		my_tree.insert(parent='', index='end', iid=4, text='Parent', values=('Clint', 5, 'Fruits de mer'))
		my_tree.insert(parent='', index='end', iid=5, text='Parent', values=('Erin', 6, 'Ananas'))

		# Ajout d'un enfant
		my_tree.insert(parent='', index='end', iid=6, text='Enfant', values=('Steve', '1.1', 'Poivrons'))
		my_tree.move('6', '0', '0')  # position idd initiale, position idd souhaitée, sous-position idd souhaitée

		# Affichage des données
		my_tree.pack(pady=20)


if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()