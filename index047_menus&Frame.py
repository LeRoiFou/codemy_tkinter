"""
Tkinter - Codemy.com #47 : Using Frames With Menus
Lien : https://www.youtube.com/watch?v=1cWWiXU02-g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=47

Combinaison des menus avec les frames

Éditeur : Laurent REYNAUD
Date : 29-11-2020
"""

import tkinter

class GUI:

    def __init__(self, root):
        self.root = root
        root.geometry('400x400')
        root.title("Titre !")
        self.menus()
        self.widgets()

    def menus(self):
        
        # Configuration de la barre de menus
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        # 1er titre de la barre de menus : 'Fichier'
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=file_menu)

        # Ajout des difféntes commandes du menu 'Fichier'
        file_menu.add_command(label='Nouveau...', command=self.file_new)
        file_menu.add_separator()
        file_menu.add_command(label='Sortie', command=root.quit)

        # 2ème titre de la barre de menus : 'Édition'
        edit_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Édition', menu=edit_menu)

        # Ajout des difféntes commandes du menu 'Édition'
        edit_menu.add_command(label='Couper', command=self.edit_cut)
        edit_menu.add_command(label='Coller', command=self.our_command)

        # 3ème titre de la barre de menus : 'Options'
        options_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Options', menu=options_menu)

        # Ajout des difféntes commandes du menu 'Options'
        options_menu.add_command(label='Rechercher', command=self.our_command)
        options_menu.add_command(label='Annuler', command=self.our_command)

    def widgets(self):
        
        # configuration de la fenêtre principale de chaque onglet
        self.file_new_frame = tkinter.Frame(root, width=400, height=400, bg='red')
        self.edit_cut_frame = tkinter.Frame(root, width=400, height=400, bg='blue')

    def our_command(self):
    
        myLabel = tkinter.Label(root, text='Vous avez cliqué sur un menu déroulant !').pack()

    def file_new(self):
        # Fonction pour la commande 'Nouveau' pour créer un cadre de couleur rouge
        
        # récursivité ;p
        self.hide_all_frames() 

        self.file_new_frame.pack(fill='both', expand=1)
        myLabel = tkinter.Label(self.file_new_frame, text='Vous avez cliqué sur le menu Fichier -> Nouveau !').pack()

    def edit_cut(self):
        # Fonction pour la commande 'Couper' pour créer un cadre de couleur bleue
        
        # récursivité ;p
        self.hide_all_frames()  
        
        self.edit_cut_frame.pack(fill='both', expand=1)
        myLabel = tkinter.Label(self.edit_cut_frame, text='Vous avez cliqué sur le menu Édition -> Couper !').pack()

    def hide_all_frames(self):
        # Cette fonction a pour but de 'cacher' le Frame appelé selon l'une des fonctions ci-avant
        
        self.file_new_frame.pack_forget()
        self.edit_cut_frame.pack_forget()

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()