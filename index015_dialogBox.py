"""
Tkinter - Codemy.com #15 : boîte de dialogue (dialog box)
Lien : https://www.youtube.com/watch?v=Aim_7fC-inw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=15

Dans ce programme, on apprend à ouvrir un fichier de type .png

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog

class GUI:

	def __init__(self, root):
		self.root = root
		self.root.title('Apprendre à coder avec Codemy.com')
		my_btn = tkinter.Button(root, text='Ouvrir le fichier', command=self.open).pack()

	def open(self):
	    # ouverture d'une boîte de dialogue pour charger un fichier sous format.jpg
	    root.filename = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/codemy_tkinter/images',
	                                               title='Sélectionner un fichier',
	                                               filetypes=(('Fichiers .png', '*.png'), ('Tous fichiers', '*.*')))
	    my_label = tkinter.Label(root, text=root.filename)
	    self.my_image = ImageTk.PhotoImage(Image.open(root.filename))  # Chargement de l'image
	    my_image_label = tkinter.Label(image=self.my_image).pack()  # Affichage de l'image sous la forme d'une étiquette


if __name__ == "__main__":
	root = tkinter.Tk()
	gui = GUI(root)
	root.mainloop()