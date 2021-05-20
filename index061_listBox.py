"""
Tkinter - Codemy.com #61 : List Boxes  
Lien : https://www.youtube.com/watch?v=wEv3BworNK8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=61  

Widget listbox (zone de liste) 
Avec l'instruction insert() on met en premier argument la position du message dans la liste, et en deuxième argument  
le message à insérer dans la liste  
Avec l'instruction delete() on supprime une des données sélectionnée dans la zone de liste  

Éditeur : Laurent REYNAUD  
Date : 03-12-20  
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		root.title('Mon titre !')
		root.geometry('400x400')
		self.widgets()

	def widgets(self):

		"""Configuration de la zone de liste"""
		self.my_listbox = tkinter.Listbox(root)
		self.my_listbox.pack(pady=15)

		"""Insertion dans la zone de liste d'un message"""
		self.my_listbox.insert('end', '1er message')
		self.my_listbox.insert('end', '2nd message')

		"""Liste de messages à insérer dans la zone de liste en première position"""
		my_list = ['Un', 'Deux', 'Trois']
		for item in my_list:
		    self.my_listbox.insert(0, item)  # 1ère position de la liste mais affichage inversée des données de la liste

		"""Nouvelle entrée positionnée en 3ème ligne"""
		self.my_listbox.insert(2, 'Une nouvelle entrée')  # cette donnée va être placée en 3ème position

		my_button = tkinter.Button(root, text='Supprimer', command=self.delete)
		my_button.pack(pady=10)

		my_button2 = tkinter.Button(root, text='Sélectionner', command=self.select)
		my_button2.pack(pady=10)

		self.my_label = tkinter.Label(root, text='')  # étiquette configurée dans la fonction select()
		self.my_label.pack(pady=5)

	def delete(self):
		"""Méthode permettant de supprimer une des données de la zone de liste"""
	
		self.my_listbox.delete('anchor')  # 'anchor' permet de sélectionner le texte mis en surlignage


	def select(self):
		"""Méthode permettant d'afficher en étiquette la donnée sélectionnée dans la zone de liste"""

		# 'anchor' permet de sélectionner le texte mis en surlignage
		self.my_label.config(text=self.my_listbox.get('anchor'))  

if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()