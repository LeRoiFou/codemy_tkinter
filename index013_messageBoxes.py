"""
Tkinter - Codemy.com #13 : boîte à message (message boxes)
Lien : https://www.youtube.com/watch?v=S3AaSwpb5GE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=13

Ce programme permet d'afficher un message à titre informatif...
On peut également afficher un message d'alerte, d'interdiction, d'interrogation...

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

import tkinter
from tkinter import messagebox

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title('Apprendre à coder avec Codemy.com')
		Button = tkinter.Button(root, text='Information', command=self.popup).pack()

	def popup(self):
	    response = messagebox.askquestion("C'est mon info ;)", 'Bonjour !')
	    tkinter.Label(root, text=response).pack()
	    if response == 'yes':
	        tkinter.Label(root, text='Tu as cliqué oui !!!').pack()
	    else:
	        tkinter.Label(root, text='Tu as cliqué non !!!').pack()


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()