"""
Tkinter - Codemy.com #118 : Color and Style Our Treeview - Python Tkinter GUI Tutorial #118
Lien : https://www.youtube.com/watch?v=ewxT3ZEGKAA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=118

Dans ce programme on apprend à configurer le style de l'arborescence

Pour les différents thèmes préconfigurés de l'arbosrescence, avec l'instruction style.theme_use(), aller dans la console
puis saisir les instructions suivantes :
from tkinter import ttk
s=ttk.Style()
s.theme_names()
Les thèmes actuels sont les suivants :
('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

L'instruction configure(fieldbackground='...') pour la couleur de fond des lignes non saisies de l'arborescence, ne
fonctionne que si un style préconfiguré a été instruit, mais, pour autant, ne fonctionne pas pour les thèmes suivants :
-> vista
-> xpnative

Préférence pour le style préconfiguré 'clam'...

Éditeur : Laurent REYNAUD
Date : 22-12-20
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x600')


def add_record():
    """Ajout des données dans l'arborescence"""
    global count
    my_tree.insert(parent='', index='end', iid=count, text='', values=(name_box.get(), id_box.get(), topping_box.get()))
    count += 1
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


def remove_all():
    """Suppression de toutes les données de l'arborescence"""
    for record in my_tree.get_children():
        my_tree.delete(record)


def remove_one():
    """Suppression d'une donnée de l'arborescence"""
    x = my_tree.selection()[0]  # assignation d'une variable de la ligne sélectionnée
    my_tree.delete(x)  # suppression des données de la liste


def remove_many():
    """Suppression de plusieurs données sélectionnées"""
    x = my_tree.selection()  # assignation d'une variable de la ligne sélectionnée
    for record in x:
        """Recours à une boucle pour supprimer un par un les données sélectionnées"""
        my_tree.delete(record)  # suppression des données de la liste


"""Configuration du style de l'arborescence"""
style = ttk.Style()

"""Style préconfiguré de l'arborescence"""
style.theme_use('clam')

"""Style personnalisé de l'arborescence"""
# style.configure('Treeview',
#                 background='silver',  # fond de couleur des lignes saisies dans l'arborescence
#                 rowheight=25,  # 'épaisseur' des lignes saisies dans l'arborescence
#                 fieldbackground='yellow',  # fond de couleur des lignes non saisies dans l'arborescence
#                 )
# style.map('Treeview', background=[('selected', 'green')])  # Couleur des lignes sélectionnées

"""Configuration de l'arborescence"""
my_tree = ttk.Treeview(root)

"""Configuration des colonnes"""
my_tree['columns'] = ('Name', 'ID', 'Favorite pizza')

"""Formatage des colonnes"""
my_tree.column('#0', width=0, stretch=NO)  # colonne fantôme
my_tree.column('Name', anchor=W, width=140)
my_tree.column('ID', anchor=CENTER, width=100)
my_tree.column('Favorite pizza', anchor=W, width=140)

"""Configuration des en-têtes"""
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Name', text='Nom', anchor=W)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('Favorite pizza', text='Pizza préférée', anchor=W)

"""Ajout des données à partir d'une liste"""
data = [['John', 1, 'Calzone'],
        ['Albert', 2, 'Fromages'],
        ['Marius', 3, 'Champignons'],
        ['Bob', 4, 'Anchois'],
        ['Clint', 5, 'Fruits de mer'],
        ['Erin', 6, 'Ananas']]

"""Recours à une boucle for pour alimenter les données de la liste ci-dessus dans l'arborescence"""
count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
    count += 1

"""Affichage des données"""
my_tree.pack(pady=20)

"""Cadre"""
add_frame = Frame(root)
add_frame.pack(pady=20)

"""Etiquettes"""
nl = Label(add_frame, text='Nom')
nl.grid(row=0, column=0)

il = Label(add_frame, text='ID')
il.grid(row=0, column=1)

tl = Label(add_frame, text='En-tête')
tl.grid(row=0, column=2)

"""Champs de saisi"""
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame, justify='center')
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

"""Boutons"""
add_record = Button(root, text='Ajouter une donnée', command=add_record)
add_record.pack(pady=10)

remove_all = Button(root, text='Effacer toute les données', command=remove_all)
remove_all.pack(pady=10)

remove_one = Button(root, text='Effacer la donnée sélectionnée', command=remove_one)
remove_one.pack(pady=10)

remove_many = Button(root, text='Effacer plusieurs données sélectionnées', command=remove_many)
remove_many.pack(pady=10)

root.mainloop()
