"""
Tkinter - Codemy.com #62 : Add Scrollbars to List Boxes  - 08 minutes 20 secondes
Lien : https://www.youtube.com/watch?v=8ijKnxkaoHE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=62

Création d'une barre de défilement à la verticale située à droite de la zone de liste

Éditeur : Laurent REYNAUD
Date : 03-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('400x500')

"""Création d'un cadre"""
my_frame = Frame(root)

"""Création de la barre de défilement"""
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

"""Configuration de la zone de liste : avec l'instruction selectmode on peut : 
-> sélectionner plusieurs données avec MULTIPLE 
-> étendre la sélection avec EXTENDED 
"""
my_listbox = Listbox(my_frame, width=50, yscrollcommand=my_scrollbar.set,
                     selectmode=MULTIPLE)  # connection zone de liste & barre de défil.

"""Configuration de la barre de défilement"""
my_scrollbar.config(command=my_listbox.yview)  # défilement de haut en bas de la zone de liste
my_scrollbar.pack(side=RIGHT, fill=Y)  # barre de défilement à droite sur toute la largeur de la zone de liste
my_frame.pack()

"""Placement de la zone de liste qui s'effectue après le placement de la barre de défilement. À l'inverse la barre de  
défilement se trouve en-dessous de la zone de liste"""
my_listbox.pack(pady=15)

"""Insertion dans la zone de liste d'un message"""
my_listbox.insert(END, '1er message')
my_listbox.insert(END, '2nd message')

"""Liste de messages à insérer dans la zone de liste en première position"""
my_list = ['Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux',
           'Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois']
for item in my_list:
    my_listbox.insert(0, item)  # 1ère position de la liste mais affichage inversée des données de la liste

"""Nouvelle entrée positionnée en 3ème ligne"""
my_listbox.insert(2, 'Une nouvelle entrée')  # cette donnée va être placée en 3ème position


def delete():
    """Fonction permettant de supprimer une des données de la zone de liste"""
    my_listbox.delete(ANCHOR)  # ANCHOR permet de sélectionner le texte mis en surlignage


def select():
    """Fonction permettant d'afficher en étiquette la donnée sélectionnée dans la zone de liste"""
    my_label.config(text=my_listbox.get(ANCHOR))  # ANCHOR permet de sélectionner le texte mis en surlignage


def delete_all():
    """Fonction supprimant TOUTES les données de la zone de liste"""
    my_listbox.delete(0, END)  # 0, END supprime toutes les données à la différence de ANCHOR


def select_all():
    result = ''
    for item in my_listbox.curselection():  # pour chaque donnée de la liste sélectionnée...
        result = result + str(my_listbox.get(item)) + '\n'  # affichage de chaque donnée par ligne distincte
    my_label.config(text=result)


def delete_multiple():
    """la fonction reversed permet de prendre d'un seul coup toutes les données sélectionnées. À défaut de cette
    instruction, les données à supprimer seront effacées une par une à chaque fois qu'on appuye sur le bouton
    'suppression multiple'"""
    for item in reversed(my_listbox.curselection()):  # pour chaque donnée de la liste sélectionnée...
        my_listbox.delete(item)


my_button = Button(root, text='Supprimer', command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text='Sélectionner', command=select)
my_button2.pack(pady=10)

my_label = Label(root, text='')  # étiquette configurée dans la fonction select() et la fonction select_all()
my_label.pack(pady=5)

my_button3 = Button(root, text='Tout supprimer', command=delete_all)
my_button3.pack(pady=10)

my_button4 = Button(root, text='Tout sélectionner', command=select_all)
my_button4.pack(pady=10)

my_button5 = Button(root, text='Suppression multiple', command=delete_multiple)
my_button5.pack(pady=10)

root.mainloop()
