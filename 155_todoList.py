"""
Tkinter - Codemy.com #155 : Cross and Uncross From ToDo List - Python Tkinter GUI Tutorial #155
Lien : https://www.youtube.com/watch?v=kI__2rHTdGo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=155

Dans ce programme on apprend à faire une liste des points à faire, tout en effaçant certains points de la liste, ou
tous les points de la liste, ou de désactiver les points effectués, ou à sauvegarder les points de la liste

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

from tkinter import *
from tkinter.font import Font

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Ma liste !')
root.geometry('600x500')

"""Configuration de la police d'écriture"""
my_font = Font(
    family='Brush Script MT',  # les exemples des différents types d'écritures se trouvent sur C:/Windows/Fonts
    size=30,
    weight='bold')

"""Cadre pour la zone de liste et la barre de défilement"""
my_frame = Frame(root)
my_frame.pack(pady=10)

"""Configuration et affichage d'une zone de liste"""
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg='SystemButtonFace',  # couleur par défaut de la fenêtre
                  bd=0,
                  fg='#464646',
                  highlightthickness=0,  # suppression de la bordure du cadre
                  selectbackground='#a6a6a6',  # couleur de fond de la donnée sélectionnée
                  activestyle='none',  # suppression du soulignement de la donnée sélectionnée
                  justify='center')
my_list.pack(side=LEFT, fill=BOTH)

"""Assignation d'une liste des choses à faire"""
stuff = ['Jeux', 'Cours', 'Documentation', 'Dossiers', 'Manger', 'Sport', 'Travaux divers', 'Administratif']

"""Ajout des données de la liste des choses à faire dans la zone de liste"""
for item in stuff:
    my_list.insert(END, item)

"""Configuration et affichage de la barre de défilement"""
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

"""Ajout de la barre de défilement à la zone de liste"""
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

"""Configuration et affichage d'un champ de saisie pour ajouter les données dans la zone de liste"""
my_entry = Entry(root, font='Helvetica 24', justify='center')
my_entry.pack(pady=20)

"""Cadre pour les boutons d'exécution"""
button_frame = Frame(root)
button_frame.pack(pady=20)


def delete_item():
    """Fonction permettant de supprimer un élément de la liste"""
    my_list.delete(ANCHOR)


def add_item():
    """Fonction permettant d'ajouter un élément de la liste"""
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_off_item():
    """Fonction permettant de désactiver un point de la liste : on ne peut pas rayer..."""

    """Changement de la couleur de la donnée sélectionnée"""
    my_list.itemconfig(
        my_list.curselection(),
        fg='#dedede')

    """Désactivation de la donnée sélectionnée"""
    my_list.selection_clear(0, END)


def uncross_item():
    """Fonction permettant de réactiver un point de la liste désactivée"""

    """Changement de la couleur de la donnée sélectionnée"""
    my_list.itemconfig(
        my_list.curselection(),
        fg='#464646')

    """Réactivation de la donnée sélectionnée"""
    my_list.selection_clear(0, END)


def delete_crossed_item():
    """Fonction permettant de supprimer tous les points désactivés"""

    """Assignation d'un compteur"""
    count = 0

    """Boucle while"""
    while count < my_list.size():
        """Tant que mon compteur est inférieur au nombre d'élements de ma liste"""
        if my_list.itemcget(count, 'fg') == '#dedede':
            """Si ma liste contient dans sa configuration une couleur de fond de code hexadécimal #dedede, la variable 
            'count' sera attribuée à cette donnée... 
            Suppression de toutes les données pour lesquelles un compteur a été attribué"""
            my_list.delete(my_list.index(count))
        count += 1  # parcours de toutes les données de la liste


"""Ajout des boutons"""
delete_button = Button(button_frame, text='Supprimer', command=delete_item)
add_button = Button(button_frame, text='Ajouter', command=add_item)
cross_off_button = Button(button_frame, text='Désactiver', command=cross_off_item)
uncross_button = Button(button_frame, text='Réactiver', command=uncross_item)
delete_crossed_button = Button(button_frame, text='Supp points désactivés', command=delete_crossed_item)

"""Affichage des boutons"""
delete_button.grid(row=0, column=0, padx=20)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2, padx=20)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4, padx=20)

root.mainloop()
