"""
Tkinter - Codemy.com #162 : Basic Search and Autofill - Python Tkinter GUI Tutorial #162
Lien : https://www.youtube.com/watch?v=0CXQ3bbBLVk

Dans ce programme lorsqu'on saisit dans le champ Entry, dans la zone de liste s'affiche les mots avec les premiers
caractères saisis

Éditeur : Laurent REYNAUD
Date : 14-01-21
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x300')


def update(data):
    """Fonction permettant d'ajouter la liste des pizzas dans la zone de liste"""

    """Réinitialisation de la zone de liste"""
    my_list.delete(0, END)

    """Ajout des données de la liste"""
    for item in data:
        my_list.insert(END, item)


def fillout(e):
    """Cette fonction a pour but d'afficher dans la zone de saisie, la pizza sélectionnée dans la zone de liste"""

    """Réinitialisation du champ de saisie"""
    my_entry.delete(0, END)

    """Insertion dans le champ de saisi, la pizza sélectionnée dans la zone de liste"""
    my_entry.insert(0, my_list.get(ACTIVE))


def check(e):
    """Cette fonction permet d'afficher dans la zone de liste, les pizzas à partir des premiers caractères saisis"""

    """Assignation du texte saisi dans le champ entry"""
    typed = my_entry.get()

    if typed == '':  # si rien n'est saisi
        """Les données de la zone de liste sont inchangées"""
        data = toppings

    else:  # sinon...
        """Initialisation d'une liste vide"""
        data = []
        """Pour chaque caractère de la liste de pizza"""
        for item in toppings:
            """Si le caractère saisi est un caractère de la liste de pizza"""
            if typed.lower() in item.lower():
                """Ajout du caractère dans la liste 'data'"""
                data.append(item)

    """Appel de la fonction update()"""
    update(data)


"""Configuration du titre"""
my_label = Label(root, text='Commencer à écrire', font='Helvetica 14', fg='grey')
my_label.pack(pady=20)

"""Configuration du champ de saisie"""
my_entry = Entry(root, font='Helvetica 20', justify='center')
my_entry.pack()

"""Configuration de la zone de liste"""
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

"""Assignation d'une liste de pizzas"""
toppings = ['Pepperoni', 'Poivrons', 'Champignons', 'Fromage', 'Oignons', 'Jambon', 'Oeuf']

"""Appel de la fonction update() déterminée ci-dessus"""
update(toppings)

"""Lien entre la zone de liste et le champ de saisi"""
my_list.bind('<<ListboxSelect>>', fillout)

"""Lien entre le champ de saisi et la zone de liste"""
my_entry.bind('<KeyRelease>', check)

root.mainloop()
