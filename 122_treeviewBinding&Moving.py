"""
Tkinter - Codemy.com #122 : Binding and Moving Rows In Treeview - Python Tkinter GUI Tutorial #122
Lien : https://www.youtube.com/watch?v=tvXFpMGlHPk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=122

Dans ce programme :
-> on a recours à l'instruction bind pour afficher dans les champs de saisies la ligne sélectionnée sans recourir au
bouton 'Sélectionner' mais par un clique/double clique de la souris
-> à monter une ligne sélectionnée au-dessus des autres lignes ou à descendre une ligne sélectionnée en-dessous des
autres lignes de saisies

Éditeur : Laurent REYNAUD
Date : 22-12-20
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x800')


def add_record():
    """Ajout des données dans l'arborescence"""

    """Configuration du coloriage des lignes saisies dans l'arborescence"""
    my_tree.tag_configure('oddrow', background='white')  # couleur de la rangée impaire
    my_tree.tag_configure('evenrow', background='lightblue')  # couleur de la même rangée

    global count
    if count % 2 == 0:
        """Si la rangée est paire, la couleur de la lineg est de couleur blanche"""
        my_tree.insert(parent='', index='end', iid=count, text='', values=(name_box.get(), id_box.get(),
                                                                           topping_box.get()), tags='evenrow')
    else:
        """Sinon la rangée est impaire et la couleur de la ligne est de couleur bleu claire"""
        my_tree.insert(parent='', index='end', iid=count, text='', values=(name_box.get(), id_box.get(),
                                                                           topping_box.get()), tags='oddrow')
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


def select_record():
    """Ajout dans les champs de saisies des données sélectionnées"""

    """Initialisation des champs de saisies"""
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    """Assignation du n° d'indice de la ligne de saisie sélectionnée"""
    selected = my_tree.focus()

    """Assignation de la valeur de la ligne de saisie sélectionnée"""
    values = my_tree.item(selected, 'values')
    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


def update_record():
    """Mise à jour des données"""

    """Assignation du n° d'indice de la ligne de saisie sélectionnée (comme pour la fonction ci-avant)"""
    selected = my_tree.focus()

    """Mise à jour des données saisies"""
    my_tree.item(selected, text='', values=(name_box.get(), id_box.get(), topping_box.get()))

    """Initialisation des champs de saisies"""
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


def clicker(e):
    """Données rentrées dans les champs de saisies en sélectionnant la ligne de saisie souhaitée et en cliquant ou en
    double cliquant dessus"""
    select_record()


def up():
    """Fonction permettant de monter la ligne de saisie sélectionnée"""
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


def down():
    """Fonction permettant de descendre la ligne de saisie sélectionnée"""
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


"""Configuration du style de l'arborescence"""
style = ttk.Style()

"""Style préconfiguré de l'arborescence"""
style.theme_use('clam')

"""Style personnalisé de l'arborescence"""
style.configure('Treeview',
                background='silver',  # fond de couleur des lignes saisies dans l'arborescence
                rowheight=25,  # 'épaisseur' des lignes saisies dans l'arborescence
                fieldbackground='silver',  # fond de couleur des lignes non saisies dans l'arborescence
                )
style.map('Treeview', background=[('selected', 'green')])  # Couleur des lignes sélectionnées

"""Cadre pour l'arborescence"""
tree_frame = Frame(root)
tree_frame.pack(pady=20)

"""Barre de défilement pour l'arborescence"""
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

"""Configuration de l'arborescence"""
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

"""Affichage des données"""
my_tree.pack()

"""Configuration de la barre de défilement"""
tree_scroll.config(command=my_tree.yview)

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
        ['Erin', 6, 'Ananas'],
        ['Link', 7, 'Poivrons'],
        ['Dean', 8, 'Oeuf'],
        ['Heisenberg', 9, 'Crème fraîche'],
        ['John', 1, 'Calzone'],
        ['Albert', 2, 'Fromages'],
        ['Marius', 3, 'Champignons'],
        ['Bob', 4, 'Anchois'],
        ['Clint', 5, 'Fruits de mer'],
        ['Erin', 6, 'Ananas'],
        ['Link', 7, 'Poivrons'],
        ['Dean', 8, 'Oeuf'],
        ['John', 1, 'Calzone'],
        ['Albert', 2, 'Fromages'],
        ['Marius', 3, 'Champignons'],
        ['Bob', 4, 'Anchois'],
        ['Clint', 5, 'Fruits de mer'],
        ['Erin', 6, 'Ananas'],
        ['Link', 7, 'Poivrons'],
        ['Dean', 8, 'Oeuf']]

"""Configuration du coloriage des lignes saisies dans l'arborescence"""
my_tree.tag_configure('oddrow', background='white')  # couleur de la rangée impaire
my_tree.tag_configure('evenrow', background='lightblue')  # couleur de la même rangée

"""Recours à une boucle for pour alimenter les données de la liste ci-dessus dans l'arborescence et en attribuant une  
couleur selon si la ligne de rangée est paire ou impaire"""
count = 0
for record in data:
    if count % 2 == 0:
        """Si la rangée est paire, la couleur de la lgine est de couleur blanche"""
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]),
                       tags='evenrow')
    else:
        """Sinon la rangée est impaire et la couleur de la ligne est de couleur bleu claire"""
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]),
                       tags='oddrow')
    count += 1

"""Cadre"""
add_frame = Frame(root)
add_frame.pack(pady=20)

"""Etiquettes"""
nl = Label(add_frame, text='Nom')
nl.grid(row=0, column=0)

il = Label(add_frame, text='ID')
il.grid(row=0, column=1)

tl = Label(add_frame, text='Pizza préférée')
tl.grid(row=0, column=2)

"""Champs de saisi"""
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame, justify='center')
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

"""Boutons"""
move_up = Button(root, text='Monter', command=up)
move_up.pack(pady=10)

move_down = Button(root, text='Descendre', command=down)
move_down.pack(pady=10)

select_button = Button(root, text='Sélectionner', command=select_record)
select_button.pack(pady=10)

update_button = Button(root, text='Mise à jour', command=update_record)
update_button.pack(pady=10)

add_record = Button(root, text='Ajouter une donnée', command=add_record)
add_record.pack(pady=10)

remove_all = Button(root, text='Effacer toute les données', command=remove_all)
remove_all.pack(pady=10)

remove_one = Button(root, text='Effacer la donnée sélectionnée', command=remove_one)
remove_one.pack(pady=10)

remove_many = Button(root, text='Effacer plusieurs données sélectionnées', command=remove_many)
remove_many.pack(pady=10)

"""Bindings"""
my_tree.bind('<Double-1>', clicker)  # sélection d'une ligne saisie par un double clic gauche de la souris
my_tree.bind('<ButtonRelease-1>', clicker)  # sélection d'une ligne saisie par un clic gauche de la souris

root.mainloop()
