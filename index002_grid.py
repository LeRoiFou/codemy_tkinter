"""
Tkinter - Codemy.com #2 : positionnement des widgets avec l'instruction grid()
Lien : https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2

Dans ce programme on apprend à position les widgets avec l'instruction grid()

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		self.widgets()

	def widgets(self):
		# étiquette
		myLabel1 = tkinter.Label(root, text='Bonjour !')
		myLabel2 = tkinter.Label(root, text='Mon nom est John Gerald')

		# affichage
		myLabel1.grid(row=0, column=0)
		myLabel2.grid(row=1, column=5)  # équivaut à la colonne 2 car rien n'est saisi de la colonne 2 à 4


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()