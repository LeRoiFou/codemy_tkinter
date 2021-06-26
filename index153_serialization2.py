"""
Tkinter - Codemy.com #153 : 
Save To Dat File Instead of Databases - Python Tkinter GUI Tutorial #153
Lien : https://www.youtube.com/watch?v=l2Qs0GvI6Ho&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=153

Dans ce programme on apprend la sérialisation 
et la désérialisation avec le module pickle

Dans cet exemple on sérialise des données issues d'une zone de liste

Différence entre la sérialisation et une base de données :
On sérialise les données si elles sont peu importantes. 
À l'inverse, on a recours aux bases de données.
D'autre part, les données étant sérialisées (sauvegardées) et 
donc non modifiées, elles sont donc conservées dans un tuple, 
ce qui peut poser problème pour d'éventuelles modifications 
à effectuer sur les données sauvegardées...

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

import tkinter
import pickle

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x400')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Assignation d'une liste de tailles"""
        sizes = ['Petit', 'Moyen', 'Grand']

        # """Configuration d'une zone de texte"""
        # my_text = Text(root, width=40, height=10)
        # my_text.pack(pady=20)

        """Configuration d'une zone de liste"""
        self.my_list = tkinter.Listbox(root)
        self.my_list.pack(pady=20)

        """Ajout des données de la liste de tailles dans la zone de liste"""
        for item in sizes:
            self.my_list.insert('end', item)

        """Configuration et affichage des boutons"""
        my_button1 = tkinter.Button(
            root, 
            text='Sauvegarder', 
            command=self.save_file)
        my_button1.pack(pady=20)
        my_button2 = tkinter.Button(
            root, 
            text='Ouvrir', 
            command=self.open_file)
        my_button2.pack(pady=20)
        my_button3 = tkinter.Button(
            root, 
            text='Effacer les données', 
            command=self.delete_items)
        my_button3.pack(pady=20)
        
    def save_file(self):
        """Méthode permettant de sauvegarder les données"""

        """Assignation de l'obtention des données 
        saisies dans la zone de liste"""
        stuff = self.my_list.get(0, 'end')

        """Assignation d'un nom de fichier"""
        file_name = 'data/dat_stuff'

        """Assignation de l'ouverture du fichier en mode écriture"""
        output_file = open(file_name, 'wb')

        """Ajout des données de la zone de texte (variable stuff) 
        dans le fichier en mode écriture (variable output_file)"""
        pickle.dump(stuff, output_file)

    def open_file(self):
        """Méthode permettant d'ouvrir le fichier"""

        """Assignation d'un nom de fichier"""
        file_name = 'data/dat_stuff'

        """Assignation de l'ouverture du fichier en mode lecture"""
        input_file = open(file_name, 'rb')

        """Assignation de la récupération des données sauvegardées"""
        stuff = pickle.load(input_file)

        """Insertion des données récupérées dans la zone de liste"""
        for item in stuff:
            self.my_list.insert('end', item)

        print(stuff)

    def delete_items(self):
        """Méthode permettant d'effacer les données présentes 
        dans la zone de liste"""
        
        self.my_list.delete(0, 'end')


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
