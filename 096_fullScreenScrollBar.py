"""
Tkinter - Codemy.com #96 : Adding a Full Screen ScrollBar
Lien : https://www.youtube.com/watch?v=0WafQCaok6g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=96

Dans ce programme on ajoute une barre de défilement sur la fenêtre qui permet de se déplacer verticalement dans toute
la fenêtre
Le programme est assez important (+30 lignes pour une barre de défilement à la fenêtre...), il est donc préconisé
d'afficher tous les widgets sur la fenêtre sans recourir à une barre de défilement... voire recourir à notebook...

Éditeur : Laurent REYNAUD
Date : 16-12-20
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x400')

"""Création d'un cadre principal qui s'étend sur toute la fenêtre"""
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

"""Création d'un canvas situé à gauche du cadre principal"""
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

"""Ajouter une barre de défilement à droite du canvas sur toute sa largeur"""
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

"""Configuration du canvas"""
my_canvas.config(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion=my_canvas.bbox('all')))

"""Création d'un autre cadre à l'intérieur du canvas"""
second_frame = Frame(my_canvas)

"""Ajouter ce nouveau cadre à la fenêtre du canvas"""
my_canvas.create_window((0, 0), window=second_frame, anchor=NW)

for i in range(100):
    """Affichage de 100 boutons à la verticale à partir de 0 jusqu'à 99"""
    Button(second_frame, text=f"Button {i} Yo !").grid(row=i, column=0, pady=10)

root.mainloop()
