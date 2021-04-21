"""
Tkinter - Codemy.com #12 : radio buttons
Lien : https://www.youtube.com/watch?v=uqJZWLlnSqs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=12

Ce programme permet d'afficher une liste d'option (ici le choix de pizzas)

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

import tkinter


class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title('Apprendre à coder avec Codemy.com')
		self.widgets()

	def widgets(self):

		# assignation d'une liste de tuples
		MODES = [
		    ('Pepperoni', 'Pepperoni'),
		    ('Fromage', 'Fromage'),
		    ('Champignon', 'Champignon'),
		    ('Oignon', 'Oignon'),
		]

		# variable de contrôles
		pizza = tkinter.StringVar()
		pizza.set('Pepporoni')  # cette instruction permet de décocher toutes les options affichées

		# affichage des options
		for text, mode in MODES:
		    tkinter.Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor='w')

		# bouton d'exécution permettant d'afficher l'option choisie"""
		myButton = tkinter.Button(root, text='Clique !', command=lambda: self.clicked(pizza.get()))
		myButton.pack()


	def clicked(self, value):
	# fonction permettant d'afficher l'option choisie
	    
	    myLabel = tkinter.Label(root, text=value)
	    myLabel.pack()


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()
