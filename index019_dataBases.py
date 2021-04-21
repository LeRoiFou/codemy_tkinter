"""
Tkinter - Codemy.com #19 : bases de données (databases)
Lien : https://www.youtube.com/watch?v=YR3h2CY21-U&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=19

Dans ce programme on apprend à lier tkinter avec une base de données. Pour cela on a recours au module sqlite3

Éditeur : Laurent REYNAUD
Date : 05-11-2020
"""

import tkinter
import sqlite3  # import de ce module pour les bases de données

root = tkinter.Tk()
root.title('Apprendre à coder avec Codemy.com')
root.iconbitmap('images/homer.ico')
root.geometry('400x400')

# Création d'une base de données connectée
conn = sqlite3.connect('pieces/address_book.db')

# Création d'un curseur
c = conn.cursor()

# Création d'une table
c.execute("""CREATE TABLE adresses(   
        first_name text,   
        last_name text,   
        address text,   
        city text,   
        state text,   
        zipcode integer)""")

# Archivage des connections effectuées
conn.commit()

# Fermeture de la connection
conn.close()

root.mainloop()
