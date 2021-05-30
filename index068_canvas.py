"""
Tkinter - Codemy.com #68 : How to Draw Lines and Shapes With Canvas
Lien : https://www.youtube.com/watch?v=HrK9Kmz3_9A&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=68

Programme qui effectue des dessins géométriques à partir de canvas

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		root.title('Mon titre !')
		root.geometry('500x500')
		self.widgets()

	def widgets(self):

		"""Configuration d'un canvas sous fond blanc qui permet d'effectuer des figures géométriques"""
		my_canvas = tkinter.Canvas(root, width=300, height=200, bg='white')
		my_canvas.pack(pady=20)

		"""Création d'un retangle(x1, y1, x2, y2, fill='color') 
		x1, y1 : point en haut à gauche 
		x2, y2 : point en bas à droite"""
		my_canvas.create_rectangle(50, 150, 250, 50, fill='pink')

		"""Création d'une ellipse : même configuration qu'un rectangle"""
		my_canvas.create_oval(50, 150, 250, 50, fill='cyan')

		"""Création de lignes(x1, y1, x2, y2, fill='color')"""
		my_canvas.create_line(0, 100, 300, 100, fill='red')  # ligne à l'horizontal
		my_canvas.create_line(150, 200, 150, 0, fill='red')  # ligne à la verticale


if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()
