"""
Tkinter - Codemy.com #107 : Build A Text Editor Part 4 - Cut Copy Paste
Lien : https://www.youtube.com/watch?v=rUgAC_Ssflw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=107

Dans ce programme on apprend :
-> À couper, copier et coller le texte sélectionné dans le textbox 
à partir du menu
-> À résoudre l'anomalie du programme lorsque par exemple on copie 
avec les touches CTRL + X et on colle avec le menu :
Édition -> coller, qui fait ressortir une erreur de programmation, 
en recourant à l'instruction bind
-> Coordonner les touches de raccourcis du clavier pour couper/copier/coller 
avec les Méthodes présentes dans le menu Editer

Éditeur : Laurent REYNAUD
Date : 18-12-20
"""

import tkinter
from tkinter import filedialog
from tkinter import font

class Gui:
    
    def __init__(self, root):
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('1200x660')
        
        # False = rien ne se passe lorsque le programme lit cette instruction
        self.open_status_name = False  
        
        # False = rien ne se passe lorsque le programme lit cette instruction
        self.selected = False  
        
        # Mise au format de la fenêtre principale
        self.widgets()
        
    def widgets(self):
        
        """Création d'un cadre pour le textbox et pour 
        la barre de défilement"""
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
        my_menu.add_cascade(
            label='Fichier', 
            menu=file_menu)
        file_menu.add_command(
            label='Nouveau', 
            command=self.new_file)
        file_menu.add_command(
            label='Ouvrir', 
            command=self.open_file)
        file_menu.add_command(
            label='Enregistrer', 
            command=self.save_file)
        file_menu.add_command(
            label='Enregistrer sous', 
            command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(
            label='Quitter', 
            command=root.quit)

        """Ajout du menu Editer"""
        edit_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Éditer', menu=edit_menu)
        edit_menu.add_command(
            label='Couper    (ctrl+x)', 
            command=lambda: self.cut_text(False))
        edit_menu.add_command(
            label='Copier     (ctrl+c)', 
            command=lambda: self.copy_text(False))
        edit_menu.add_command(
            label='Coller      (ctrl+v)', 
            command=lambda: self.paste_text(False))
        edit_menu.add_command(label='Annuler')
        edit_menu.add_command(label='Rétablir')

        """Création d'une barre d'état en bas de la fenêtre"""
        self.status_bar = tkinter.Label(root, text='Prêt        ', anchor='e')
        self.status_bar.pack(fill='x', side='bottom', ipady=5)

        """Instructions bind pour les anomalies 
        relevées dans le couper/copier/coller"""
        root.bind('<Control-Key-x>', self.cut_text)
        root.bind('<Control-Key-c>', self.copy_text)
        root.bind('<Control-Key-v>', self.paste_text)
        
    def new_file(self):
        """Méthode qui permet d'ouvrir un nouveau fichier"""
        
         # Suppression de l'ancien texte de textbox
        self.my_text.delete('1.0', 'end') 
        
        # Mise à jour du titre de la fenêtre
        root.title('Nouveau fichier') 
        
        # Mise à jour de la barre de statut
        self.status_bar.config(text='Nouveau fichier        ')  

        self.open_status_name = False

    def open_file(self):
        """Méthode qui permet d'ouvrir un fichier existant"""

        # Suppression de l'ancien texte de textbox
        self.my_text.delete('1.0', 'end')  
        
        # Ouverture du fichier
        text_file = filedialog.askopenfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Ouvrir un fichier',
            filetypes=(('Fichier texte', '*.txt'),
                       ('Fichier HTML', '*.html'),
                       ('Fichier Python', '*.py'),
                       ('Tous fichiers', '*.*')))  

        # Vérifie s'il existe un nom de fichier
        if text_file:  
            self.open_status_name 
            self.open_status_name = text_file

        # Assignation d'une variable pour la barre de statut
        name = text_file  
        
        # Mise à jour de la barre de statut
        self.status_bar.config(text=f"{name}        ")  
        
        # Assignation variable pour titre fenêtre
        name = name.replace(
            'C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  
        
        # Mise à jour du titre de la fenêtre
        root.title(f'{name}') 

        """Ouverture du fichier existant"""
        
        # chargement du fichier
        text_file = open(text_file, 'r')  
        
        # ouverture du fichier
        stuff = text_file.read()  
        
        # ajout du fichier au textbox
        self.my_text.insert('end', stuff)  
        
        # fermeture du fichier ouvert
        text_file.close()  

    def save_as_file(self):
        """Méthode permettant d'enregistrer sous"""

        # sauvegarde du fichier
        text_file = filedialog.asksaveasfilename(
            defaultextension='*.*',
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Fichier sauvegardé',
            filetypes=(('Fichier texte', '*.txt'),
                       ('Fichier HTML', '*.html'),
                       ('Fichier Python', '*.py'),
                       ('Tous fichiers', '*.*')))  

         # assignation d'une variable pour la barre de statut
        name = text_file 
        
        # mise à jour de la barre de statut
        self.status_bar.config(text=f"Sauvegardé sous {name}        ")  
        
        # assignation variable remplacement chemin
        name = name.replace(
            'C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  
        
        # mise à jour du titre de la fenêtre
        root.title(f'{name}')  
        
        # écriture du fichier
        text_file = open(text_file, 'w')  
        
        # sauvegarde du fichier
        text_file.write(self.my_text.get(1.0, 'end'))  
        
        # fermeture du fichier
        text_file.close()  

    def save_file(self):
        """Méthode permettant d'enregistrer un fichier"""

        # si la variable globale est True, à savoir que le fichier 
        # est déjà ouvert...
        if self.open_status_name:
            
            # écriture du fichier  
            text_file = open(self.open_status_name, 'w')  
            
            # sauvegarde du fichier
            text_file.write(self.my_text.get(1.0, 'end'))  
            
            # fermeture du fichier
            text_file.close()  
            
            # mise à jour de la barre de statut
            self.status_bar.config(
                text=f"Sauvegardé sous {self.open_status_name}        ")  
            
        # si le fichier n'existe pas...    
        else:  
            
            # appel de cette Méthode pour 'enregistrer sous'
            self.save_as_file()  

    def cut_text(self, e):
        """Méthode permettant de couper le texte sélectionné dans le textbox"""

        # Si le raccourci clavier CTRL + X a été utilisé...
        if e:
            
            # assignation d'une variable des données présentes 
            # dans le presse-papier
            selected = root.clipboard_get() 
        
        else:
            """Les instructions ci-après permette de couper le texte 
            sélectionné à partir du menu Fichier -> Couper"""
            
            # si le texte est sélectionné...
            if self.my_text.selection_get():  
                
                # assignation d'une variable global du texte sélectionné
                selected = self.my_text.selection_get()  
                
                # Suppression du texte sélectionné
                self.my_text.delete('sel.first', 'sel.last') 
                
                # réinitialis. de toutes les données éventuellement 
                # présentes dans le presse-papier
                root.clipboard_clear()  
                
                # puis ajout du texte sélectionné dans le presse-papier
                root.clipboard_append(selected)  

    def copy_text(self, e):
        """Méthode permettant de copier le texte sélectionné dans le textbox
        Vérifie si nous avons utilisé les touches de raccourcis du clavier 
        ainsi que les données présentes dans le presse-papier : à chaque fois
        que l'on fait un copier/couper/coller, les données passent 
        automatiquement dans le presse-papier de windows.  
        Si on ne réinitialise pas toutes les données présentes dans le 
        presse-papier, à un moment donné, on copiera quelque chose qui était
        conservée dans le presse-papier, ce qui arrive de temps en temps dans 
        LibreOffice..."""
    
        # Si le raccourci clavier CTRL + C a été utilisé...
        if e:
            
            # assignation d'une variable des données présentes 
            # dans le presse-papier
            selected = root.clipboard_get()  
       
        else:
            """Les instructions suivantes permettent de copier le texte 
            sélectionné à partir du menu Fichier -> Copier"""
           
            # si le texte est sélectionné...
            if self.my_text.selection_get():  
                
                # assignation d'une variable du texte sélectionné
                selected = self.my_text.selection_get()  
                
                # réinitialis. de toutes les données éventuellement 
                # présentes dans le presse-papier
                root.clipboard_clear()  
                
                # puis ajout du texte sélectionné dans le presse-papier
                root.clipboard_append(selected)  

    def paste_text(self, e):
        """Méthode permettant de coller le texte sélectionné 
        dans le textbox"""

        # Si le raccourci clavier CTRL + V a été utilisé...
        if e:
            
            # assignation d'une variable des données présentes 
            # dans le presse-papier
            self.selected = root.clipboard_get()  
        
        else:
            """Les instructions suivantes permettent de copier le texte 
            sélectionné à partir du menu Fichier -> Coller"""
            
             # si le texte a été selectionné...
            if self.selected: 
                
                # insertion à la position du curseur de la souris
                position = self.my_text.index('insert')  
                
                # insertion du texte sélectionné dans le textbox
                self.my_text.insert(position, self.selected)  


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
