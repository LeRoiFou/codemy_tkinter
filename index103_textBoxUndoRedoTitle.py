"""
Tkinter - Codemy.com #103 : Undo and Redo Text Button
Lien : https://www.youtube.com/watch?v=yd2a_olJ4WM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=103

Dans ce programme on appr'end' à annuler et à rétablir une action.
Pour ces instructions, il n'y a pas lieu de crééer des fonctions, 
il suffit d'instruire l'instruction command dans le widget qui 
effectuera l'action, et mettre l'instruction 'undo=True' dans le widget textbox

En complément on apprend à changer le titre de la fenêtre 
par le nom du fichier dans la méthode open_text()

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
        root.geometry('500x700')
        self.widgets()
        
    def widgets(self):
        
        """Création d'un cadre pour le textbox et 
        la barre de défilement"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=10)

        """Création d'une barre de défilement pour le texbox"""
        text_scroll = tkinter.Scrollbar(my_frame)
        text_scroll.pack(side='right', fill='y')

        """Configuration de la boîte à texte"""
        self.my_text = tkinter.Text(
            my_frame, 
            width=40, 
            height=10, 
            font='helvetica 16',
            selectbackground='red',
            selectforeground='black',
            yscrollcommand=text_scroll.set,
            undo=True # annuler une action = Vrai
                    )
        self.my_text.pack(pady=20)

        """Configuration de la barre de défilement"""
        text_scroll.config(command=self.my_text.yview)

        """Configuration du bouton d'exécution 
        permettant d'ouvrir un fichier texte"""
        open_button = tkinter.Button(
            root, 
            text='Ouvrir un fichier texte', 
            command=self.open_text)
        open_button.pack(pady=20)

        """Configuration du bouton de sauvegarde 
        des données saisies dans le widget text box"""
        save_button = tkinter.Button(
            root, 
            text='Sauvegarder', 
            command=self.save_txt)
        save_button.pack(pady=20)

        """Configuration du bouton d'exécution 
        pour insérer une image dans le text box"""
        image_button = tkinter.Button(
            root, 
            text='Ajouter une image', 
            command=self.add_image)
        image_button.pack(pady=5)

        """Configuration du bouton d'exécution 
        pour afficher le texte sélectionné"""
        select_button = tkinter.Button(
            root, 
            text='Sélectionner le texte', 
            command=self.select)
        select_button.pack(pady=5)

        """Affichage du texte surligné dont la configuration 
        de l'étiquette se trouve dans la fonction select()"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack()

        """Configuration du bouton d'exécution 
        pour mettre en gras le texte sélectionné"""
        bold_button = tkinter.Button(
            root, 
            text='Gras', 
            command=self.bold)
        bold_button.pack(pady=5)

        """Configuration du bouton d'exécution 
        pour mettre en italique le texte sélectionné"""
        italics_button = tkinter.Button(
            root, 
            text='Italique', 
            command=self.italics_it)
        italics_button.pack(pady=5)

        """Configuration du bouton d'exécution 
        pour annuler une action"""
        undo_button = tkinter.Button(
            root, 
            text='Annuler', 
            command=self.my_text.edit_undo)
        undo_button.pack(pady=5)

        """Configuration du bouton d'exécution 
        pour rétablir une action"""
        redo_button = tkinter.Button(
            root, 
            text='Rétablir', 
            command=self.my_text.edit_redo)
        redo_button.pack(pady=5)
        
    def open_text(self):
        """Méthode permettant de récupérer 
        un fichier texte et de l'afficher 
        dans le widget textbox"""
        
        my_path = 'C:/Users/LRCOM/PycharmProjects/tests/pieces'
        
        text_file = filedialog.askopenfilename(
            initialdir=my_path,
            title='Ouvrir un fichier texte',
            filetypes=(('Fichiers .txt', '*.txt'), 
                       ('Tous fichiers', '*.*')))
        
        """Changement du titre de la fenêtre 
        par le nom du fichier ouvert"""
        name = text_file
        name = name.replace(
            'C:/Users/LRCOM/PycharmProjects/tests/pieces/',
            '')
        name = name.replace('.txt', '')

        text_file = open(text_file, 'r') 
        stuff = text_file.read()
        self.my_text.insert('end', stuff)
        text_file.close()

        """Configuration du titre de la fenêtre"""
        root.title(f"{name} - Fichier texte")

    def save_txt(self):
        """Méthode permettant de sauvegarder les modifications 
        faites dans le widget textbox dans le fichier ouvert"""
        
        my_path = 'C:/Users/LRCOM/PycharmProjects/tests/pieces'
        
        text_file = filedialog.askopenfilename(
            initialdir=my_path,
            title='Enregistrer sous',
            filetypes=(('Fichiers .txt', '*.txt'),))
        text_file = open(text_file, 'w')
        text_file.write(self.my_text.get(1.0, 'end'))

    def add_image(self):
        """Ajout d'une image dans le text box"""
        
        self.my_image = tkinter.PhotoImage(
            file='images/shrek.png')
        position = self.my_text.index('insert')
        self.my_text.image_create(
            position, 
            image=self.my_image)

    def select(self):
        """Affichage du texte surligné"""
        
        selected = self.my_text.selection_get()
        self.my_label.config(text=selected)

    def bold(self):
        """Mise en gras du texte sélectionné"""
        
        bold_font = font.Font(
            self.my_text, 
            self.my_text.cget('font'))
        
        bold_font.config(weight='bold')
        
        self.my_text.tag_config('bold', font=bold_font)
        
        current_tags = self.my_text.tag_names('sel.first')
        
        if 'bold' in current_tags:
            """Si le texte est déjà en gras... 
            supprimer cette mise en forme"""
            self.my_text.tag_remove(
                'bold', 
                'sel.first', 
                'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            self.my_text.tag_add(
                'bold', 
                'sel.first', 
                'sel.last')

    def italics_it(self):
        """Mise en italique du texte sélectionné"""
        
        italics_font = font.Font(
            self.my_text, 
            self.my_text.cget('font'))
        
        italics_font.config(slant='italic')
        
        self.my_text.tag_config(
            'italic', 
            font=italics_font)
        
        current_tags = self.my_text.tag_names('sel.first')
        
        if 'italic' in current_tags:
            """Si le texte est déjà en italique... 
            supprimer cette mise en forme"""
            self.my_text.tag_remove(
                'italic', 
                'sel.first', 
                'sel.last')
        else:
            """sinon ajouter cette mise en forme"""
            self.my_text.tag_add(
                'italic', 
                'sel.first', 
                'sel.last')


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
