"""
Tkinter - Codemy.com #112 : Select All and Clear - 
Build A Text Editor Part 9
Lien : https://www.youtube.com/watch?v=lrRKbbF6YyQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=112

Dans ce programme on apprend :
-> À sélectionner tout le texte avec la méthode select_all(e) : 
fonction paramétrée car en liaison avec les touches de raccourcis 'ctrl+a'
-> À supprimer tout le texte avec la méthode clear_all()

Éditeur : Laurent REYNAUD
Date : 20-12-20
"""

import tkinter
# pour l'ouverture et l'enregistrement des fichiers
from tkinter import filedialog  
# pour la police d'écriture en gras et en italique
from tkinter import font  
# pour la couleur d'écriture
from tkinter import colorchooser  
# pour l'impression d'un texte
import win32api  

class Gui:
    
    def __init__(self, root):
        
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Éditeur de texte ;)')
        root.geometry('1200x700')
        self.widgets()
        
    def widgets(self):
        
        self.open_status_name = False
        self.selected = False
        
        """Création d'un cadre pour la barre d'outils"""
        toolbar_frame = tkinter.Frame(root)
        toolbar_frame.pack(fill='x')

        """Création d'un cadre pour le textbox et 
        pour la barre de défilement"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=5)

        """Création d'une barre de défilement verticale 
        pour le textbox"""
        text_scroll = tkinter.Scrollbar(my_frame)
        text_scroll.pack(side='right', fill='y')

        """Création d'une barre de défilement horizontale 
        pour le textbox"""
        hor_scroll = tkinter.Scrollbar(my_frame, orient='horizontal')
        hor_scroll.pack(side='bottom', fill='x')

        """Création d'un textbox"""
        self.my_text = tkinter.Text(
            my_frame, 
            width=97, 
            height=25, 
            font='helevetica 16', 
            selectbackground='green', 
            selectforeground='black',
            undo=True, 
            yscrollcommand=text_scroll.set, 
            wrap='none', 
            xscrollcommand=text_scroll.set)
        self.my_text.pack()

        """Configuration de la barre de défilement verticale"""
        text_scroll.config(command=self.my_text.yview)

        """Configuration de la barre de défilement horizontale"""
        text_scroll.config(command=self.my_text.xview)

        """Création d'un menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Ajout du menu Fichier"""
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=file_menu)
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
            label='Imprimer', 
            command=self.print_file)
        file_menu.add_separator()
        file_menu.add_command(
            label='Quitter', 
            command=root.quit)

        """Ajout du menu Editer"""
        edit_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Éditer', menu=edit_menu)
        edit_menu.add_command(
            label='Couper', 
            accelerator='(ctrl+x)', 
            command=lambda: self.cut_text(False))
        edit_menu.add_command(
            label='Copier', 
            accelerator='(ctrl+c)', 
            command=lambda: self.copy_text(False))
        edit_menu.add_command(
            label='Coller', 
            accelerator='(ctrl+v)', 
            command=lambda: self.paste_text(False))
        edit_menu.add_separator()
        edit_menu.add_command(
            label='Annuler', 
            accelerator='(ctrl+z)', 
            command=self.my_text.edit_undo)
        edit_menu.add_command(
            label='Rétablir', 
            accelerator='(ctrl+y)', 
            command=self.my_text.edit_undo)
        edit_menu.add_separator()
        edit_menu.add_command(
            label='Sélectionner tout', 
            accelerator='(ctrl+a)', 
            command=lambda: self.select_all(True))
        edit_menu.add_command(
            label='Effacer tout', 
            command=self.clear_all)

        """Ajout du menu Couleur"""
        color_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Couleur', menu=color_menu)
        color_menu.add_command(
            label='Sur le texte sélectionné', 
            command=self.text_color)
        color_menu.add_command(
            label='Sur tout le texte', 
            command=self.all_text_color)
        color_menu.add_command(
            label="Fond d'écran", 
            command=self.bg_color)

        """Création d'une barre d'état en bas de la fenêtre"""
        self.status_bar = tkinter.Label(root, text='Prêt        ', anchor='e')
        self.status_bar.pack(fill='x', side='bottom', ipady=15)

        """Instructions bind pour les anomalies relevées 
        dans le couper/copier/coller"""
        root.bind('<Control-Key-x>', self.cut_text)
        root.bind('<Control-Key-c>', self.copy_text)
        root.bind('<Control-Key-v>', self.paste_text)

        """Liaison entre les touches de raccourcis 'ctrl+a' 
        avec le menu Éditer -> Sélectionner tout"""
        root.bind('<Control-A>', self.select_all)
        root.bind('<Control-a>', self.select_all)

        """Création des boutons de la barre d'outils"""
        bold_button = tkinter.Button(
            toolbar_frame, 
            text='Gras', 
            command=self.bold_it)
        bold_button.grid(row=0, column=0, sticky='w', padx=5)
        italics_button = tkinter.Button(
            toolbar_frame, 
            text='Italique', 
            command=self.italics_it)
        italics_button.grid(row=0, column=1, padx=5)
        undo_button = tkinter.Button(
            toolbar_frame, 
            text='Annuler', 
            command=self.my_text.edit_undo)
        undo_button.grid(row=0, column=2, padx=5)
        redo_button = tkinter.Button(
            toolbar_frame, 
            text='Rétablir', 
            command=self.my_text.edit_redo)
        redo_button.grid(row=0, column=3, padx=5)
        color_text_button = tkinter.Button(
            toolbar_frame, 
            text='Couleur du texte', 
            command=self.text_color)
        color_text_button.grid(row=0, column=4, padx=5)
        
    def new_file(self):
        """Méthode qui permet d'ouvrir un nouveau fichier"""

        # suppression de l'ancien texte de textbox
        self.my_text.delete('1.0', 'end')  
        
        # mise à jour du titre de la fenêtre
        root.title('Nouveau fichier')  
        
        # mise à jour de la barre de statut
        self.status_bar.config(text='Nouveau fichier        ')  
        
        self.open_status_name = False

    def open_file(self):
        """Méthode qui permet d'ouvrir un fichier existant"""

        # suppression de l'ancien texte de textbox
        self.my_text.delete('1.0', 'end')  
        
        # ouverture du fichier
        text_file = filedialog.askopenfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Ouvrir un fichier',
            filetypes=(('Fichier texte', '*.txt'),
                       ('Fichier HTML', '*.html'),
                       ('Fichier Python', '*.py'),
                       ('Tous fichiers', '*.*')))  

        if text_file:  # vérifie s'il existe un nom de fichier
            self.open_status_name = text_file 

        # assignation d'une variable pour la barre de statut
        name = text_file  
        
        # mise à jour de la barre de statut
        self.status_bar.config(text=f"{name}        ")  
        
        # assignation variable pour titre fenêtre
        name = name.replace(
            'C:/Users/LRCOM/PycharmProjects/tests/pieces/', '')  
        
        # mise à jour du titre de la fenêtre
        root.title(f'{name}')  

        """Ouverture du fichier existant"""
        text_file = open(text_file, 'r')  # chargement du fichier
        stuff = text_file.read()  # ouverture du fichier
        self.my_text.insert('end', stuff)  # ajout du fichier au textbox
        text_file.close()  # fermeture du fichier ouvert

    def save_as_file(self):
        """Méthode permettant d'enregistrer sous"""

        text_file = filedialog.asksaveasfilename(
            defaultextension='*.*',
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Fichier sauvegardé',
             filetypes=(('Fichier texte', '*.txt'),
                        ('Fichier HTML', '*.html'),
                        ('Fichier Python', '*.py'),
                        ('Tous fichiers', '*.*')))  # sauvegarde du fichier
 
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

        # si le fichier est déjà ouvert...
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
        else:  # si le fichier n'existe pas...
            # appel de cette fonction pour 'enregistrer sous'
            self.save_as_file()  

    def cut_text(self, e):
        """Méthode permettant de couper le texte sélectionné 
        dans le textbox"""

        if e:
            """Si le raccourci clavier CTRL + X a été utilisé..."""
            # assignation d'une variable des données présentes 
            # dans le presse-papier
            self.selected = root.clipboard_get()  
        else:
            """Les instructions ci-après permette de couper le texte 
            sélectionné à partir du menu Fichier -> Couper"""
            # si le texte est sélectionné...
            if self.my_text.selection_get():  
                # assignation du texte sélectionné
                self.selected = self.my_text.selection_get()  
                # Suppression du texte sélectionné
                self.my_text.delete('sel.first', 'sel.last')
                # réinitialis. de toutes les données éventuellement 
                # présentes dans le presse-papier  
                root.clipboard_clear()  
                # puis ajout du texte sélectionné dans le presse-papier
                root.clipboard_append(self.selected)  

    def copy_text(self, e):
        """Méthode permettant de copier le texte sélectionné 
        dans le textbox
        Verifie si nous avons utilisé les touches de raccourcis 
        du clavier ainsi que les données présentes dans le 
        presse-papier : à chaque fois que l'on fait un copier/couper/coller, 
        les données passent automatiquement dans le presse-papier de windows.  
        Si on ne réinitialise pas toutes les données présentes dans le 
        presse-papier, à un moment donné, on copiera quelque chose qui était 
        conservée dans le presse-papier, ce qui arrive de temps en temps 
        dans LibreOffice..."""
        if e:
            """Si le raccourci clavier CTRL + C a été utilisé..."""
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

        if e:
            """Si le raccourci clavier CTRL + V a été utilisé..."""
            # assignation d'une variable des données présentes 
            # dans le presse-papier
            self.selected = root.clipboard_get()  
        else:
            """Les instructions suivantes permettent de copier 
            le texte sélectionné à partir du menu Fichier -> Coller"""
            # si le texte a été selectionné...
            if self.selected:  
                # insertion à la position du curseur de la souris
                position = self.my_text.index('insert')  
                # insertion du texte sélectionné dans le textbox
                self.my_text.insert(position, self.selected)  

    def bold_it(self):
        """Méthode permettant de mettre en gras l'écriture"""

        """Création de la police d'écriture"""
        bold_font = font.Font(self.my_text, self.my_text.cget('font'))
        bold_font.config(weight='bold')

        """Configuration du texte sélectionné"""
        self.my_text.tag_config('bold', font=bold_font)

        # assignation d'une variable du texte sélectionné
        current_tags = self.my_text.tag_names('sel.first')  
        if 'bold' in current_tags:
            """Si le texte est déjà en italique... 
            supprimer cette mise en forme"""
            self.my_text.tag_remove('bold', 'sel.first', 'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            self.my_text.tag_add('bold', 'sel.first', 'sel.last')

    def italics_it(self):
        """Méthode permettant de mettre en italique l'écriture"""

        """Création de la police d'écriture"""
        italics_font = font.Font(self.my_text, self.my_text.cget('font'))
        italics_font.config(slant='italic')

        """Configuration du texte sélectionné"""
        self.my_text.tag_config('italic', font=italics_font)

        # assignation d'une variable du texte sélectionné
        current_tags = self.my_text.tag_names('sel.first')  
        if 'italic' in current_tags:
            """Si le texte est déjà en italique... 
            supprimer cette mise en forme"""
            self.my_text.tag_remove('italic', 'sel.first', 'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            self.my_text.tag_add('italic', 'sel.first', 'sel.last')

    def text_color(self):
        """Change la couleur de l'écriture du texte sélectionné"""

        """Choisir une couleur"""
        my_color = colorchooser.askcolor()[1]  # code couleur hexadecimal

        if my_color:
            """La mise en place de cette condition permet d'éviter 
            annuler la couleur sélectionnée lorsqu'on appuie sur le bouton 
            'annuler' de la boîte de dialogue des couleurs présentées"""

            """Création de la couleur d'écriture"""
            color_font = font.Font(self.my_text, self.my_text.cget('font'))

            """Configuration du texte sélectionné"""
            self.my_text.tag_config(
                'colored', 
                font=color_font, 
                foreground=my_color)

            # assignation d'une variable du texte sélectionné
            current_tags = self.my_text.tag_names('sel.first')  
            if 'colored' in current_tags:
                """Si le texte est déjà colorié... 
                supprimer cette mise en forme"""
                self.my_text.tag_remove('colored', 'sel.first', 'sel.last')
            else:
                """sinon ajouter cette mise en forme"""
                self.my_text.tag_add('colored', 'sel.first', 'sel.last')

    def all_text_color(self):
        """Change la couleur de tout le texte"""

        """Choisir une couleur"""
        my_color = colorchooser.askcolor()[1]  # code couleur hexadecimal

        if my_color:
            self.my_text.config(fg=my_color)

    def bg_color(self):
        """Change la couleur du fond d'écran"""

        """Choisir une couleur"""
        my_color = colorchooser.askcolor()[1]  # code couleur hexadecimal

        if my_color:
            self.my_text.config(bg=my_color)

    def print_file(self):
        """Méthode permettant d'imprimer un fichier"""
        
        file_to_print = filedialog.askopenfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Ouvrir un fichier',
            filetypes=(('Fichier texte', '*.txt'),
                       ('Fichier HTML', '*.html'),
                       ('Fichier Python', '*.py'),
                       ('Tous fichiers', '*.*')))  # ouverture du fichier

        # fonctionnalité à connaître pour imprimer
        if file_to_print:
            win32api.ShellExecute(0, 'print', file_to_print, None, '.', 0)  

    def select_all(self, e):
        """Permet de sélectionner tout le texte"""

        """Ajouter une balise 'sel' pour tout sélectionner"""
        # sélection de la 1ère à la dernière ligne
        self.my_text.tag_add('sel', '1.0', 'end')  

    def clear_all(self):
        """Permet d'effacer tout le texte"""
       
        self.my_text.delete(1.0, 'end')


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
