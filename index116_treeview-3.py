"""
Tkinter - Codemy.com #116 : Treeview
Lien : https://www.youtube.com/watch?v=YTqDYmfccQU&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=116

Dans ce programme on apprend à crééer une arborescence

Ajout des données à partir d'une liste

Éditeur : Laurent REYNAUD
Date : 21-12-20
"""

import tkinter
from tkinter import ttk

class GUI:

	def __init__(self, root):
		self.root =root
		self.root.iconbitmap('images/Logo.ico')
		self.root.title('Titre !')
		self.root.geometry('500x500')
		self.widget()

	def widget(self):

		# Configuration de l'arborescence"""
		my_tree = ttk.Treeview(root)

		# Configuration des colonnes"""
		my_tree['columns'] = ('Name', 'ID', 'Favorite pizza')

		# Formatage des colonnes"""
		my_tree.column('#0', width=0, stretch='no')  # colonne fantôme : strectch='no' masque la colonne
		my_tree.column('Name', anchor='w', width=120)
		my_tree.column('ID', anchor='center', width=80)
		my_tree.column('Favorite pizza', anchor='w', width=120)

		# Configuration des en-têtes"""
		my_tree.heading('#0', text='', anchor='w')
		my_tree.heading('Name', text='Nom', anchor='w')
		my_tree.heading('ID', text='ID', anchor='center')
		my_tree.heading('Favorite pizza', text='Pizza préférée', anchor='w')

		# Ajout des données à partir d'une liste"""
		data = [['John', 1, 'Calzone'],
		        ['Albert', 2, 'Fromages'],
		        ['Marius', 3, 'Champignons'],
		        ['Bob', 4, 'Anchois'],
		        ['Clint', 5, 'Fruits de mer'],
		        ['Erin', 6, 'Ananas']]

		count = 0
		for record in data:
		    """Recours à une boucle for pour alimenter les données de la liste ci-dessus dans l'arborescence"""
		    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
		    count += 1

		# Affichage des données"""
		my_tree.pack(pady=20)


if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()