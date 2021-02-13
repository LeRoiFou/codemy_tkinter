"""
Tkinter - Codemy.com #22 : bases de données (databases) -> affichage des données saisies
Lien : https://www.youtube.com/watch?v=EAs3gr9mC9g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=22

Éditeur : Laurent REYNAUD
Date : 06-11-2020
"""

from tkinter import *
import sqlite3  # import de ce module pour les bases de données

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.geometry('320x400')

# Connection à la base de donnée
conn = sqlite3.connect('pieces/address_book.db')
# Création d'un curseur
c = conn.cursor()


# """Création d'une table"""
# c.execute("""CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer)""")


def delete():
    """Fonction permettant de supprimer un enregistrement de la BdD SQL"""
    # Connection à la base de donnée
    conn = sqlite3.connect('pieces/address_book.db')
    # Création d'un curseur
    c = conn.cursor()
    # Supprimer un enregistrement
    c.execute('DELETE from addresses WHERE oid = ' + delete_box.get())  # suppression à partir du n° de clé sélectionné


def edit():
    """Fonction pour supprimer un enregistrement"""
    editor = Tk()
    editor.title('Modifier un enregistrement')
    editor.iconbitmap('Images&Icons/Homer.ico')
    editor.geometry('320x400')

    conn = sqlite3.connect('pieces/address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)  # sélectionner toutes les données de la BdD SQL
    records = c.fetchall()  # récupération de toutes les données

    """Création zone de textes"""
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    """Création d'étiquettes de zone de textes"""
    f_name_label_editor = Label(editor, text='Prénom')
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text='Nom')
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text='Adresse')
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text='Ville')
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text='Département')
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text='Code postal')
    zipcode_label_editor.grid(row=5, column=0)

    # Boucle à travers les résultats obtenus
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    """Création d'un bouton pour valider l'enregistrement modifié"""
    edit_btn_editor = Button(editor, text="Valider l'enregistrement", command=edit)
    edit_btn_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=79)

    # Sauvegarde des données
    conn.commit()

    # Fermeture de la connection
    conn.close()


def submit():
    """Fonction pour soumettre la création de base de données"""
    # Connection à la base de donnée
    conn = sqlite3.connect('pieces/address_book.db')
    # Création d'un curseur
    c = conn.cursor()
    # Insertion des données de la table
    c.execute('insert into addresses values (:f_name, :l_name, :address, :city, :state, :zipcode)',
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    # Sauvegarde des données
    conn.commit()
    # Fermeture de la connection
    conn.close()
    # Effacement des données de la table de saisie
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


"""Création zone de textes"""
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

"""Création d'étiquettes de zone de textes"""
f_name_label = Label(root, text='Prénom')
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text='Nom')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Adresse')
address_label.grid(row=2, column=0)
city_label = Label(root, text='Ville')
city_label.grid(row=3, column=0)
state_label = Label(root, text='Département')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Code postal')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text='N° de la clé')
delete_box_label.grid(row=9, column=0, pady=5)

"""Création d'un bouton 'soumettre'"""
submit_btn = Button(root, text="Ajouter à la BdB SQL", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=92)


def query():
    """Fonction permettant d'afficher les données enregistrées dans la base de données SQL"""

    # Connection à la base de donnée
    conn = sqlite3.connect('pieces/address_book.db')

    # Création d'un curseur
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")  # sélectionner toutes les données de la BdD SQL
    records = c.fetchall()  # récupération de toutes les données

    # Sauvegarde des données
    conn.commit()

    # Fermeture de la connection
    conn.close()

    # Boucle pour afficher les données de la BdD SQL à la verticale
    print_records = ''
    for record in records:  # pour chaque valeur des données de la BdD SQL
        print_records += str(record[0]) + ' ' + str(record[1]) + '\t' + 'clé n° : ' + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


"""Création d'un bouton pour afficher le contenu de la base de données"""
query_btn = Button(root, text='Afficher les données', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=92)

"""Création d'un bouton pour supprimer un enregistrement"""
delete_btn = Button(root, text="Supprimer un enregistrement", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=67)

"""Création d'un bouton pour modifier un enregistrement"""
edit_btn = Button(root, text="Éditer un enregistrement", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=79)

# Sauvegarde des données
conn.commit()
# Fermeture de la connection
conn.close()

root.mainloop()
