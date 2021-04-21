"""
Tkinter - Codemy.com #22 : bases de données (databases) -> affichage des données saisies
Lien : https://www.youtube.com/watch?v=EAs3gr9mC9g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=22

Éditeur : Laurent REYNAUD
Date : 06-11-2020
"""

import tkinter
import sqlite3  # import de ce module pour les bases de données

class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title('Apprendre à coder avec Codemy.com')
        self.root.geometry('320x400')
        self.my_sql()
        self.widgets()

    def my_sql(self):

        # Connection à la base de donnée
        self.conn = sqlite3.connect('pieces/address_book.db')
        # Création d'un curseur
        c = self.conn.cursor()

        # """Création d'une table"""
        # c.execute("""CREATE TABLE adresses(
        #         first_name text,
        #         last_name text,
        #         address text,
        #         city text,
        #         state text,
        #         zipcode integer)""")

        # Sauvegarde des données
        self.conn.commit()

        # Fermeture de la connection
        self.conn.close()

    def widgets(self):

        # Création zone de textes
        self.f_name = tkinter.Entry(root, width=30)
        self.f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.l_name = tkinter.Entry(root, width=30)
        self.l_name.grid(row=1, column=1, padx=20)
        self.address = tkinter.Entry(root, width=30)
        self.address.grid(row=2, column=1, padx=20)
        self.city = tkinter.Entry(root, width=30)
        self.city.grid(row=3, column=1, padx=20)
        self.state = tkinter.Entry(root, width=30)
        self.state.grid(row=4, column=1, padx=20)
        self.zipcode = tkinter.Entry(root, width=30)
        self.zipcode.grid(row=5, column=1, padx=20)
        self.delete_box = tkinter.Entry(root, width=30)
        self.delete_box.grid(row=9, column=1, pady=5)

        # Création d'étiquettes de zone de textes
        f_name_label = tkinter.Label(root, text='Prénom')
        f_name_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = tkinter.Label(root, text='Nom')
        l_name_label.grid(row=1, column=0)
        address_label = tkinter.Label(root, text='Adresse')
        address_label.grid(row=2, column=0)
        city_label = tkinter.Label(root, text='Ville')
        city_label.grid(row=3, column=0)
        state_label = tkinter.Label(root, text='Département')
        state_label.grid(row=4, column=0)
        zipcode_label = tkinter.Label(root, text='Code postal')
        zipcode_label.grid(row=5, column=0)
        delete_box_label = tkinter.Label(root, text='N° de la clé')
        delete_box_label.grid(row=9, column=0, pady=5)

        # Création d'un bouton 'soumettre'
        submit_btn = tkinter.Button(root, text="Ajouter à la BdB SQL", command=self.submit)
        submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=92)

        # Création d'un bouton pour afficher le contenu de la base de données
        query_btn = tkinter.Button(root, text='Afficher les données', command=self.query)
        query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=92)

        # Création d'un bouton pour supprimer un enregistrement
        delete_btn = tkinter.Button(root, text="Supprimer un enregistrement", command=self.delete)
        delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=67)

        # Création d'un bouton pour modifier un enregistrement
        edit_btn = tkinter.Button(root, text="Éditer un enregistrement", command=self.edit)
        edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=79)

    def delete(self):
        # Fonction permettant de supprimer un enregistrement de la BdD SQL

        # Connection à la base de donnée
        self.conn = sqlite3.connect('pieces/address_book.db')
        # Création d'un curseur
        c = self.conn.cursor()
        # Supprimer un enregistrement
        c.execute('DELETE from adresses WHERE oid = ' + self.delete_box.get())  # suppression à partir du n° de clé sélectionné

    def edit(self):
        # Fonction pour supprimer un enregistrement

        editor = tkinter.Tk()
        editor.title('Modifier un enregistrement')
        # editor.iconbitmap('Images&Icons/Homer.ico')
        editor.geometry('320x400')

        self.conn = sqlite3.connect('pieces/address_book.db')
        c = self.conn.cursor()
        record_id = self.delete_box.get()
        c.execute("SELECT * FROM adresses WHERE oid = " + record_id)  # sélectionner toutes les données de la BdD SQL
        records = c.fetchall()  # récupération de toutes les données

        # Création zone de textes
        f_name_editor = tkinter.Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor = tkinter.Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1, padx=20)
        address_editor = tkinter.Entry(editor, width=30)
        address_editor.grid(row=2, column=1, padx=20)
        city_editor = tkinter.Entry(editor, width=30)
        city_editor.grid(row=3, column=1, padx=20)
        state_editor = tkinter.Entry(editor, width=30)
        state_editor.grid(row=4, column=1, padx=20)
        zipcode_editor = tkinter.Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1, padx=20)

        # Création d'étiquettes de zone de textes
        f_name_label_editor = tkinter.Label(editor, text='Prénom')
        f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
        l_name_label_editor = tkinter.Label(editor, text='Nom')
        l_name_label_editor.grid(row=1, column=0)
        address_label_editor = tkinter.Label(editor, text='Adresse')
        address_label_editor.grid(row=2, column=0)
        city_label_editor = tkinter.Label(editor, text='Ville')
        city_label_editor.grid(row=3, column=0)
        state_label_editor = tkinter.Label(editor, text='Département')
        state_label_editor.grid(row=4, column=0)
        zipcode_label_editor = tkinter.Label(editor, text='Code postal')
        zipcode_label_editor.grid(row=5, column=0)

        # Boucle à travers les résultats obtenus
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        # Création d'un bouton pour valider l'enregistrement modifié
        edit_btn_editor = tkinter.Button(editor, text="Valider l'enregistrement", command=self.edit)
        edit_btn_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=79)

        # Sauvegarde des données
        self.conn.commit()

        # Fermeture de la connection
        self.conn.close()

    def submit(self):
        # Fonction pour soumettre la création de base de données

        # Connection à la base de donnée
        self.conn = sqlite3.connect('pieces/address_book.db')
        # Création d'un curseur
        c = self.conn.cursor()
        # Insertion des données de la table
        c.execute('insert into adresses values (:f_name, :l_name, :address, :city, :state, :zipcode)',
                  {
                      'f_name': self.f_name.get(),
                      'l_name': self.l_name.get(),
                      'address': self.address.get(),
                      'city': self.city.get(),
                      'state': self.state.get(),
                      'zipcode': self.zipcode.get()
                  })
        # Sauvegarde des données
        self.conn.commit()
        # Fermeture de la connection
        self.conn.close()
        # Effacement des données de la table de saisie
        self.f_name.delete(0, 'end')
        self.l_name.delete(0, 'end')
        self.address.delete(0, 'end')
        self.city.delete(0, 'end')
        self.state.delete(0, 'end')
        self.zipcode.delete(0, 'end')

    def query(self):
        # Fonction permettant d'afficher les données enregistrées dans la base de données SQL

        # Connection à la base de donnée
        self.conn = sqlite3.connect('pieces/address_book.db')

        # Création d'un curseur
        c = self.conn.cursor()
        c.execute("SELECT *, oid FROM adresses")  # sélectionner toutes les données de la BdD SQL
        records = c.fetchall()  # récupération de toutes les données

        # Sauvegarde des données
        self.conn.commit()

        # Fermeture de la connection
        self.conn.close()

        # Boucle pour afficher les données de la BdD SQL à la verticale
        print_records = ''
        for record in records:  # pour chaque valeur des données de la BdD SQL
            print_records += str(record[0]) + ' ' + str(record[1]) + '\t' + 'clé n° : ' + str(record[6]) + '\n'

        query_label = tkinter.Label(root, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()