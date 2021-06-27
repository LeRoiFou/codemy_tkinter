"""
Tkinter - Codemy.com #156 : 
Save and Open ToDo Lists - Python Tkinter GUI Tutorial #156
Lien : https://www.youtube.com/watch?v=Vm0ivVxNaA8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=156

Dans ce programme on apprend à faire une liste des points à faire, 
tout en effaçant certains points de la liste, ou tous les points de la liste, 
ou de désactiver les points effectués, 
ou à sauvegarder les points de la liste

Éditeur : Laurent REYNAUD
Date : 27-12-20
"""

import tkinter
from tkinter.font import Font
from tkinter import filedialog
import pickle

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Ma liste !')
        root.geometry('600x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration de la police d'écriture"""
        my_font = Font(
            family='Brush Script MT',
            size=30,
            weight='bold')

        """Cadre pour la zone de liste et la barre de défilement"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=10)

        """Configuration et affichage d'une zone de liste"""
        self.my_list = tkinter.Listbox(my_frame,
                        font=my_font,
                        width=25,
                        height=5,
                        bg='SystemButtonFace',
                        bd=0,
                        fg='#464646',
                        highlightthickness=0,
                        selectbackground='#a6a6a6',
                        activestyle='none',
                        justify='center')
        self.my_list.pack(side='left', fill='both')

        """Configuration et affichage de la barre de défilement"""
        my_scrollbar = tkinter.Scrollbar(my_frame)
        my_scrollbar.pack(side='right', fill='both')

        """Ajout de la barre de défilement à la zone de liste"""
        self.my_list.config(yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=self.my_list.yview)

        """Configuration et affichage d'un champ de saisie pour ajouter
        les données dans la zone de liste"""
        self.my_entry = tkinter.Entry(
            root, 
            font='Helvetica 24', 
            justify='center', 
            width=30)
        self.my_entry.pack(pady=20)

        """Cadre pour les boutons d'exécution"""
        button_frame = tkinter.Frame(root)
        button_frame.pack(pady=20)
        
        """Barre de menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Menu Fichier"""
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=file_menu)
        file_menu.add_command(
            label='Sauvegarder', 
            command=self.save_list)
        file_menu.add_command(
            label='Ouvrir', 
            command=self.open_list)
        file_menu.add_separator()
        file_menu.add_command(
            label='Tout supprimer', 
            command=self.clear_list)

        """Ajout des boutons"""
        delete_button = tkinter.Button(
            button_frame, 
            text='Supprimer', 
            command=self.delete_item)
        add_button = tkinter.Button(
            button_frame, 
            text='Ajouter', 
            command=self.add_item)
        cross_off_button = tkinter.Button(
            button_frame, 
            text='Désactiver', 
            command=self.cross_off_item)
        uncross_button = tkinter.Button(
            button_frame, 
            text='Réactiver', 
            command=self.uncross_item)
        delete_crossed_button = tkinter.Button(
            button_frame, 
            text='Suppr points désactivés', 
            command=self.delete_crossed_item)

        """Affichage des boutons"""
        delete_button.grid(row=0, column=0, padx=20)
        add_button.grid(row=0, column=1, padx=20)
        cross_off_button.grid(row=0, column=2, padx=20)
        uncross_button.grid(row=0, column=3, padx=20)
        delete_crossed_button.grid(row=0, column=4, padx=20)
        
    def delete_item(self):
        """Méthode permettant de supprimer un élément de la liste"""
        
        self.my_list.delete('anchor')

    def add_item(self):
        """Méthode permettant d'ajouter un élément de la liste"""
        
        self.my_list.insert('end', self.my_entry.get())
        self.my_entry.delete(0, 'end')

    def cross_off_item(self):
        """Méthode permettant de désactiver un point de la liste : 
        on ne peut pas rayer..."""

        """Changement de la couleur de la donnée sélectionnée"""
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg='#dedede')

        """Désactivation de la donnée sélectionnée"""
        self.my_list.selection_clear(0, 'end')

    def uncross_item(self):
        """Méthode permettant de réactiver un point de la liste désactivée"""

        """Changement de la couleur de la donnée sélectionnée"""
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg='#464646')

        """Réactivation de la donnée sélectionnée"""
        self.my_list.selection_clear(0, 'end')

    def delete_crossed_item(self):
        """Méthode permettant de supprimer tous les points désactivés"""

        """Assignation d'un compteur"""
        count = 0

        """Boucle while"""
        while count < self.my_list.size():
            """Tant que mon compteur est inférieur 
            au nombre d'élements de ma liste"""
            
            if self.my_list.itemcget(count, 'fg') == '#dedede':
                """Si ma liste contient dans sa configuration une couleur 
                de fond de code hexadécimal #dedede, la variable 
                'count' sera attribuée à cette donnée... 
                Suppression de toutes les données pour lesquelles 
                un compteur a été attribué"""
                self.my_list.delete(self.my_list.index(count))
            else:
                count += 1  # parcours de toutes les données de la liste

    def save_list(self):
        """Méthode permettant de sauvegarder les données de la zone liste"""

        """Répertoire de sauvegarde"""
        file_name = filedialog.asksaveasfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/data',
            title='Enregistrer le fichier',
            filetypes=(('Fichiers .dat', '*.dat'), ('Tous fichiers', '*.*')))

        """Extension .dat du fichier"""
        if file_name:
            if file_name.endswith('.dat'):
                """Si le nom du fichier a pour fin de saisie '.dat': RAF"""
                pass
            else:
                """Sinon mettre l'extension '.dat' à la fin du nom 
                du fichier saisi"""
                file_name = f"{file_name}.dat"

        """Suppression des éléments désactivés (grisés) avant d'enregistrer"""
        count = 0  # assignation d'un compteur

        while count < self.my_list.size():
            """Tant que mon compteur est inférieur 
            au nombre d'élements de ma liste"""
            
            if self.my_list.itemcget(count, 'fg') == '#dedede':
                """Si ma liste contient dans sa configuration 
                une couleur de fond de code hexadécimal #dedede, la variable
                'count' sera attribuée à cette donnée... 
                Suppression de toutes les données pour lesquelles 
                un compteur a été attribué"""
                self.my_list.delete(self.my_list.index(count))
            else:
                count += 1  # parcours de toutes les données de la liste

        """Assignation de la récupération de tous les éléments 
        de la zone de liste"""
        stuff = self.my_list.get(0, 'end')

        """Assignation fichier de sauvegarde en écriture"""
        output_file = open(file_name, 'wb')

        """Ajout des éléments de la zone de liste au fichier 
        de sauvegarde en écriture (sérialisation)"""
        pickle.dump(stuff, output_file)

    def open_list(self):
        """Méthode permettant d'ouvrir le fichier de sauvegarde"""

        """Répertoire d'ouverture du fichier"""
        file_name = filedialog.askopenfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/data',
            title='Ouvrir le fichier',
            filetypes=(('Fichiers .dat', '*.dat'), ('Tous fichiers', '*.*')))

        """Réinitialisation de toutes les données présentes 
        dans la zone de liste"""
        if file_name:
            self.my_list.delete(0, 'end')

        """Assignation de l'ouverture du fichier en lecture"""
        input_file = open(file_name, 'rb')

        """Assignation du chargement des données du fichier ouvert"""
        stuff = pickle.load(input_file)

        """Alimentation des données du fichier ouvert dans la zone de liste"""
        for item in stuff:
            self.my_list.insert('end', item)

    def clear_list(self):
        """Méthode permettant de tout supprimer de la zone de liste"""
        self.my_list.delete(0, 'end')

        
if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
