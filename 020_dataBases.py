"""
Tkinter - Codemy.com #20 : bases de données (databases)
Lien : https://www.youtube.com/watch?v=AK1J8xF4fuk&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=20

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

from tkinter import *
import sqlite3  # import de ce module pour les bases de données

root = Tk()
root.title('Apprendre à coder avec Codemy.com')
root.iconbitmap('images/homer.ico')
root.geometry('420x400')

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
f_name.grid(row=0, column=1, padx=20)
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

"""Création d'étiquettes de zone de textes"""
f_name_label = Label(root, text='Prénom')
f_name_label.grid(row=0, column=0)
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

"""Création d'un bouton 'soumettre'"""
submit_btn = Button(root, text="Ajouter à la BdB SQL", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


def query():
    """Fonction permettant d'afficher les données enregistrées dans la base de données SQL"""

    # Connection à la base de donnée
    conn = sqlite3.connect('address_book.db')

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
        print_records += str(record[0]) + ' ' + str(record[1]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)


"""Création d'un bouton pour afficher le contenu de la base de données"""
query_btn = Button(root, text='Afficher les données', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Sauvegarde des données
conn.commit()
# Fermeture de la connection
conn.close()

root.mainloop()
