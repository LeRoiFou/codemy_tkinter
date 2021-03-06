"""
Tkinter - Codemy.com #39 : modules random et tkinter
Lien : https://www.youtube.com/watch?v=f7HE2S4opdY&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=39

Affichage au hasard d'un nom figurant dans une liste

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter
from random import randint

class GUI:

	def __init__(self, root):
		self.root = root
		root.geometry('400x400')
		root.title("Titre !")
		self.widgets()

	def widgets(self):
		# méthode de configuration des widgets

		topLabel = tkinter.Label(root, text='Vainqueur', font='Helvetica 24')
		topLabel.pack(pady=20)

		winButton = tkinter.Button(root, text='Choisir le gagnant !', font='Helvetica 24', command=self.pick)
		winButton.pack(pady=20)

	def pick(self):
	    
	    # 16 entrées à l'origine mais avec des doublons...
	    entries = ['John', 'Albert', 'Machin', 'Dark Vador', 'Machin', 'Mozart', 'Einstein', 'Hulk', 'Shrek', 'Mozart',
	               'Einstein', 'Dame de pique', 'Machin', 'Albert', 'Einstein', 'Dame de pique']
	    entries_set = set(entries)  # conversion de la liste en un ensemble pour supprimer les doubles
	    unique_entries = list(entries_set)  # reconversion de l'ensemble en une liste
	    our_number = len(entries_set) - 1  # nombre de composants dans la liste - 1
	    rando = randint(0, our_number)  # nombre au hasard entre 0 et 8 (Composants de la liste allant de 0 à 8)
	    winnerLabel = tkinter.Label(root, text=unique_entries[rando], font='Helvetica 24')
	    winnerLabel.pack(pady=50)


if __name__ == '__main__':
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()