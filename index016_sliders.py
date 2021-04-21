"""
Tkinter - Codemy.com #16 : sliders
Lien : https://www.youtube.com/watch?v=knUHd8ZGyiM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=16

Dans ce programme on apprend à afficher des barres des défilement chiffrés

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
		self.vertical = tkinter.Scale(root, from_=0, to_=400)
		self.vertical.pack()

		self.horizontal = tkinter.Scale(root, from_=0, to_=400, orient='horizontal')
		self.horizontal.pack()

		my_btn = tkinter.Button(root, text='Clique moi !', command=self.slide)
		my_btn.pack()

	def slide(self):
	    my_label = tkinter.Label(root, text=self.horizontal.get())
	    my_label.pack()
	    root.geometry(str(self.horizontal.get()) + 'x' + str(self.vertical.get()))


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()