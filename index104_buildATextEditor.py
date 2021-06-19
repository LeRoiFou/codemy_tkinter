"""
Tkinter - Codemy.com #104 : Build A Text Editor
Lien : https://www.youtube.com/watch?v=UlQRXJWUNBA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=104

Mise en place des widgets :
-> Menu
-> Cadre
-> Textbox
-> Barre de défilement
-> Barre d'état en bas de la fenêtre

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

        """Création d'une barre de défilement 
        pour le textbox"""
        text_scroll = tkinter.Scrollbar(my_frame)
        text_scroll.pack(side='right', fill='y')

        """Création d'un textbox"""
        my_text = tkinter.Text(
            my_frame,
            width=97,
            height=25,
            font='helevetica 16',
            selectbackground='green',
            selectforeground='black',
            undo=True,
            yscrollcommand=text_scroll.set)
        my_text.pack()

        """Configuration de la barre de défilement"""
        text_scroll.config(command=my_text.yview())

        """Création d'un menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Ajout du menu Fichier"""
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=file_menu)
        file_menu.add_command(label='Nouveau')
        file_menu.add_command(label='Ouvrir')
        file_menu.add_command(label='Sauvegarder')
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
        status_bar = tkinter.Label(
            root, 
            text='Prêt        ', 
            anchor='e')
        status_bar.pack(fill='x', side='bottom', ipady=5)

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
