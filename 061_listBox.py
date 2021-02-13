"""
Tkinter - Codemy.com #61 : List Boxes  
Lien : https://www.youtube.com/watch?v=wEv3BworNK8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=61  

Widget listbox (zone de liste) 
Avec l'instruction insert() on met en premier argument la position du message dans la liste, et en deuxième argument  
le message à insérer dans la liste  
Avec l'instruction delete() on supprime une des données sélectionnée dans la zone de liste  

Éditeur : Laurent REYNAUD  
Date : 03-12-20  
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('400x400')

"""Configuration de la zone de liste"""
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

"""Insertion dans la zone de liste d'un message"""
my_listbox.insert(END, '1er message')
my_listbox.insert(END, '2nd message')

"""Liste de messages à insérer dans la zone de liste en première position"""
my_list = ['Un', 'Deux', 'Trois']
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


my_button = Button(root, text='Supprimer', command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text='Sélectionner', command=select)
my_button2.pack(pady=10)

my_label = Label(root, text='')  # étiquette configurée dans la fonction select()
my_label.pack(pady=5)

root.mainloop()
