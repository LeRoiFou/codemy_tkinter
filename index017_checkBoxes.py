"""
Tkinter - Codemy.com #17 : checkboxes 
Lien : https://www.youtube.com/watch?v=4IsLwwb_yDs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=17  

Dans ce programme on apprend à afficher une coche d'option 

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

		self.var = tkinter.StringVar()

		c = tkinter.Checkbutton(root, text='Cochez cette case, je vous défie', variable=self.var, onvalue='Pizza', 
			offvalue='Hamburger')
		c.deselect()  # Réponse 'off' ou 'on' dès la première ligne
		c.pack()

		my_btn = tkinter.Button(root, text='Montrer la sélection', command=self.show)
		my_btn.pack()


	def show(self):
	    my_label = tkinter.Label(root, text=self.var.get())
	    my_label.pack()


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()