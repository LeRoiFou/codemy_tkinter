"""
Tkinter - Codemy.com #105 : Build A Text Editor Part 2 - Open and Save As Files
Lien : https://www.youtube.com/watch?v=w5Nd4O76tDw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=105

Dans ce programme, on créé :
-> une fonction new_file() pour ouvrir un nouveau fichier
-> une fonction open_file() pour charger un fichier existant
-> une fonction save_as_file() pour enregistrer un fichier

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

import tkinter
from tkinter import filedialog
from tkinter import font

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('1200x660')
        self.widgets()
        
    def widgets(self):
        
        """Création d'un cadre pour le textbox 
        et pour la barre de défilement"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=5)

        """Création d'une barre de défilement pour le textbox"""
        text_scroll = tkinter.Scrollbar(my_frame)
        text_scroll.pack(side='right', fill='y')

        """Création d'un textbox"""
        self.my_text = tkinter.Text(
            my_frame,
            width=97,
            height=25,
            font='helevetica 16',
            selectbackground='green',
            selectforeground='black',
            undo=True,
            yscrollcommand=text_scroll.set)
        self.my_text.pack()

        """Configuration de la barre de défilement"""
        text_scroll.config(command=self.my_text.yview())

        """Création d'un menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Ajout du menu Fichier"""
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=file_menu)
        file_menu.add_command(label='Nouveau', command=self.new_file)
        file_menu.add_command(label='Ouvrir', command=self.open_file)
        file_menu.add_command(label='Enregistrer')
        file_menu.add_command(
            label='Enregistrer sous', 
            command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label='Quitter', command=root.quit)

        """Ajout du menu Editer"""
        edit_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Éditer', menu=edit_menu)
        edit_menu.add_command(label='Couper')
        edit_menu.add_command(label='Copier')
        edit_menu.add_command(label='Coller')
        edit_menu.add_command(label='Annuler')
        edit_menu.add_command(label='Rétablir')

        """Création d'une barre d'état en bas de la fenêtre"""
        self.status_bar = tkinter.Label(
            root, text='Prêt        ',
            anchor='e')
        self.status_bar.pack(fill='x', side='bottom', ipady=5)
        
    def new_file(self):
        """Méthode qui permet d'ouvrir un nouveau fichier"""
        
        # suppression de l'ancien texte de textbox
        self.my_text.delete('1.0', 'end')  
        
        # mise à jour du titre de la fenêtre
        root.title('Nouveau fichier')  
        
        # mise à jour de la barre de statut
        self.status_bar.config(text='Nouveau fichier        ')  

    def open_file(self):
        """Méthode qui permet d'ouvrir un fichier existant"""
        
        # suppression de l'ancien texte de textbox
        self.my_text.delete('1.0', 'end')  
        
        my_path = 'C:/Users/LRCOM/PycharmProjects/tests/pieces'
        
        self.text_file = filedialog.askopenfilename(
            initialdir=my_path,
            title='Ouvrir un fichier',
            filetypes=(('Fichier texte', '*.txt'),
                        ('Fichier HTML', '*.html'),
                        ('Fichier Python', '*.py'),
                        ('Tous fichiers', '*.*')))
        
        # variable pour la barre de statut
        name = self.text_file  
        
        # mise à jour de la barre de statut
        self.status_bar.config(text=f"{name}        ")  
        
        # variable pour le titre de la fenêtre
        name = name.replace(my_path, '')  
        
        # mise à jour du titre de la fenêtre
        root.title(f'{name}')  

        """Ouverture du fichier existant"""
        
         # chargement du fichier
        self.text_file = open(self.text_file, 'r') 
        
        # ouverture du fichier
        stuff = self.text_file.read()  
        
        # ajout du fichier au textbox
        self.my_text.insert('end', stuff) 
        
         # fermeture du fichier ouvert
        self.text_file.close()  

    def save_as_file(self):
        """Méthode permettant d'enregistrer sous"""
        
        my_path = 'C:/Users/LRCOM/PycharmProjects/tests/pieces'
        
        self.text_file = filedialog.asksaveasfilename(
            defaultextension='*.*',
            initialdir=my_path,
            title='Fichier sauvegardé',
            filetypes=(('Fichier texte', '*.txt'),
                       ('Fichier HTML', '*.html'),
                       ('Fichier Python', '*.py'),
                       ('Tous fichiers', '*.*')))
        
        if self.text_file:  # si le fichier existe
            
            # variable pour la barre de statut
            name = self.text_file  
            
            # mise à jour de la barre de statut
            self.status_bar.config(
                text=f"Sauvegardé sous {name}        ")  
            
            # variable pour le titre de la fenêtre
            name = name.replace(my_path, '')  
            
             # mise à jour du titre de la fenêtre
            root.title(f'{name}') 
            
            # écriture du fichier
            self.text_file = open(self.text_file, 'w')  
            
            # sauvegarde du fichier
            self.text_file.write(self.my_text.get(1.0, 'end')) 
            
            # fermeture du fichier
            self.text_file.close()  


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
