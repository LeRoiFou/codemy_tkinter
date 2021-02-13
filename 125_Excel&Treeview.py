"""
Tkinter - Codemy.com #125 : Open Excel Spreadsheet In Treeview With Pandas and Numpy - Python Tkinter GUI Tutorial #125
Lien : https://www.youtube.com/watch?v=Bn1n1diGv_0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=125

Dans ce programme on apprend à importer les données Excel dans une arborescence. Cependant, il n'était pas possible
d'ouvrir des fichiers .xlsx (pb conversion fichier calc en .xlsx ?), seuls les fichiers Excel sous format .xls ont pu
être ouverts.

On utilise pas cette fois-ci le module Excel openpyxl mais les modules qui ne sont pas installés automatiquement, et
qu'il faut donc installer les packages concernés (s'ils n'ont pas été installés auparavant) :
-> pandas
-> numpy pour les calculs dans les tableaux
-> xlrd pour lire les données d'Excel

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('700x500')

"""Cadre"""
my_frame = Frame(root)
my_frame.pack(pady=20)

"""Arborescence"""
my_tree = ttk.Treeview(my_frame)


def file_open():
    """Fonction permettant d'ouvrir un fichier Excel et d'alimenter les données dans l'arborescence"""

    """Boîte de dialogue"""
    filename = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                          title='Ouvrir un fichier',
                                          filetypes=(('Fichier XLS', '*.xls'),
                                                     ('Tous fichiers', '*.*')))

    """Ouverture d'un fichier Excel avec le module pandas"""
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="Le fichier n'a pas pu être ouvert... Essayez encore...")
        except FileNotFoundError:
            my_label.config(text="Le fichier n'a pas pu être trouvé... Essayez encore...")

    """Appel de la fonction clear_tree() pour réinitialiser toutes les données déjà présentes dans l'arborescence"""
    clear_tree()

    """Alimentation des en-têtes des colonnes d'Excel dans l'arborescence"""
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    for column in my_tree['column']:
        my_tree.heading(column, text=column)

    """Alimentation des données d'Excel dans l'arborescence"""
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert('', 'end', values=row)

    """Affichage de l'arborescence"""
    my_tree.pack()


def clear_tree():
    """Fonction permettant de réinitialiser les données présentes dans l'arborescence"""
    my_tree.delete(*my_tree.get_children())


"""Barre de menu"""
my_menu = Menu(root)
root.config(menu=my_menu)

"""Menu fichier"""
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Feuilles de calcul', menu=file_menu)
file_menu.add_command(label='Ouvrir', command=file_open)

"""Message d'erreur"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
