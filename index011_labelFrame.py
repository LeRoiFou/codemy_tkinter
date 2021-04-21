"""
Tkinter - Codemy.com #11 : les cadres (frame)
Lien : https://www.youtube.com/watch?v=_auZ8TTkojQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11

Dans ce programme on apprend à insérer des widgets dans un cadre

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title('Apprendre à coder avec Codemy.com')
		# self.root.iconbitmap('images/homer.ico')
		self.widgets()

	def widgets(self):

		frame = tkinter.LabelFrame(root, text="C'est mon cadre...", padx=50, pady=50)
		frame.pack(padx=10, pady=10)
		b = tkinter.Button(frame, text='Ne pas cliquer !')
		b2 = tkinter.Button(frame, text='... ni sur ce bouton !')
		b.grid(row=0, column=0)
		b2.grid(row=1, column=1)


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()




