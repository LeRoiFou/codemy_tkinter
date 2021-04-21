"""
Tkinter - Codemy.com #18 : Dropdown menus
Lien : https://www.youtube.com/watch?v=3E_fK5hCUnI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=18

Dans ce programme on apprend à afficher un menu déroulant avec des titres (bof...)

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title('Apprendre à coder avec Codemy.com')
		self.root.geometry('400x400')
		self.widgets()

	def widgets(self):
		
		options = ['Lundi',
           'Mardi',
           'Mercredi',
           'Jeudi',
           'Vendredi',
           'Samedi',
           'Dimanche'
           ]

		self.clicked = tkinter.StringVar()
		self.clicked.set(options[2])  # affichage par défaut : Mercredi

		# argument options précédé de l'*' pour un affichage vertical des données
		drop = tkinter.OptionMenu(root, self.clicked, *options)  
		drop.pack()

		myButton = tkinter.Button(root, text='Montrer la sélection', command=self.show)
		myButton.pack()

	def show(self):
	    
	    myLabel = tkinter.Label(root, text=self.clicked.get())
	    myLabel.pack()


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()