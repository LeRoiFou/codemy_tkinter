"""
Tkinter - Codemy.com #125 : 
Open Excel Spreadsheet In Treeview With Pandas and Numpy 
- Python Tkinter GUI Tutorial #125
Lien : https://www.youtube.com/watch?v=Bn1n1diGv_0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=125

Dans ce programme on apprend à importer les données Excel 
dans une arborescence.

On utilise pas cette fois-ci le module Excel openpyxl mais 
les modules qui ne sont pas installés automatiquement, et
qu'il faut donc installer les packages concernés 
(s'ils n'ont pas été installés auparavant) :
-> pandas
-> numpy pour les calculs dans les tableaux
-> xlrd pour lire les données d'Excel

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

import tkinter
from tkinter.constants import S
import pandas as pd
from tkinter import ttk, filedialog

class Gui:
    
    def __init__(self, root):
        "Constructeur de la clase"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Titre !')
        root.geometry('700x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Cadre"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=20)

        """Arborescence"""
        self.my_tree = ttk.Treeview(my_frame)
        
        """Barre de menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Menu fichier"""
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Feuilles de calcul', menu=file_menu)
        file_menu.add_command(label='Ouvrir', command=self.file_open)

        """Message d'erreur"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)
        
    def file_open(self):
        """Méthode permettant d'ouvrir un fichier Excel
        et d'alimenter les données dans l'arborescence"""

        """Boîte de dialogue"""
        filename = filedialog.askopenfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Ouvrir un fichier',
            filetypes=(('Fichier XLSX', '*.xlsx'),
                       ('Tous fichiers', '*.*')))

        """Ouverture d'un fichier Excel avec le module pandas"""
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
            except ValueError:
                self.my_label.config(
                    text="Le fichier n'a pas pu être ouvert...\
                        Essayez encore...")
            except FileNotFoundError:
                self.my_label.config(
                    text="Le fichier n'a pas pu être trouvé...\
                        Essayez encore...")

        """Appel de la fonction clear_tree() pour réinitialiser
        toutes les données déjà présentes dans l'arborescence"""
        self.clear_tree()

        """Alimentation des en-têtes des colonnes d'Excel 
        dans l'arborescence"""
        self.my_tree['column'] = list(df.columns)
        self.my_tree['show'] = 'headings'
        for column in self.my_tree['column']:
            self.my_tree.heading(column, text=column)

        """Alimentation des données d'Excel 
        dans l'arborescence"""
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.my_tree.insert('', 'end', values=row)

        """Affichage de l'arborescence"""
        self.my_tree.pack()

    def clear_tree(self):
        """Méthode permettant de réinitialiser 
        les données présentes dans l'arborescence"""
        
        self.my_tree.delete(*self.my_tree.get_children())


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
