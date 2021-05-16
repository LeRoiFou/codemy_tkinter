"""
Tkinter - Codemy.com #42 : overwrite grid labels
Lien : https://www.youtube.com/watch?v=Q-rRF6c8kJM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=42

Dans ce programme, on supprime le bouton effacer, il n'y a qu'un seul bouton qui permet d'afficher la saisie et pour
toute nouvelle saisie, le widget étiquette remplace la donnée affichée précedemment par la nouvelle donnée

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter

class GUI:

	def __init__(self, root):
		self.root = root
		root.geometry('400x400')
		root.title("Titre !")
		self.widgets()

	def widgets(self):

		self.myLabel = tkinter.Label(root)

		self.myEntry = tkinter.Entry(root, width=17, font='Helvetica 30', justify='center')
		self.myEntry.grid(row=0, column=0, padx=10, pady=10)

		self.myButton = tkinter.Button(root, text='Entrez votre nom', command=self.myClick)
		self.myButton.grid(row=1, column=0, pady=10)

		# deleteButton = tkinter.Button(root, text='Supprimer le texte', command=self.myDelete)
		# deleteButton.grid(row=2, column=0,pady=10)

	def myClick(self):
    	# Affichage des données saisies
	    
	    self.myLabel.destroy()  # cette instruction permet d'effacer intégralement les données précédemment affichées
	    hello = 'Bonjour ' + self.myEntry.get()
	    self.myLabel = tkinter.Label(root, text=hello)
	    self.myEntry.delete(0, 'end')  # lorsqu'on appuie sur le bouton 'Entrez votre nom' le champ de saisie est réinitialisé
	    self.myLabel.grid(row=3, column=0, pady=10)

	def myDelete():
	    """Suppression des données saisies"""

	    self.myLabel.grid_forget()
	    self.myButton['state'] = NORMAL

if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()