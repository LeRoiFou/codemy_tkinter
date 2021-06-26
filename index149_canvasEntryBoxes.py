"""
Tkinter - Codemy.com #149 : 
Using Entry Boxes On Canvas - Python Tkinter GUI Tutorial #149
Lien : https://www.youtube.com/watch?v=32v2rdQnXvQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=149

Dans ce programme on insère un champ de saisi au canvas

L'instruction highlightthickness permet d'effacer la bordure 
qui contourne la fenêtre

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter
from PIL import ImageTk, Image

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('323x576')
        root.resizable(width=False, height=False)
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Définition de l'image de fond de fenêtre"""
        self.bg = ImageTk.PhotoImage(file='images/bg.png')

        """Définition du canvas"""
        self.my_canvas = tkinter.Canvas(
            root, 
            width=323, 
            height=576, 
            bd=0, 
            highlightthickness=0)
        self.my_canvas.pack(fill='both', expand=True)

        """Mettre l'image dans le canvas"""
        self.my_canvas.create_image(0, 0, image=self.bg, anchor='nw')

        """Définition des champs de saisies"""
        self.un_entry = tkinter.Entry(
            root, 
            font='Helvetica 24', 
            width=14, 
            fg='#336d92', 
            bd=0, 
            justify='center')
        self.pw_entry = tkinter.Entry(
            root, 
            font='Helvetica 24', 
            width=14, 
            fg='#336d92',
            bd=0, 
            justify='center')

        self.un_entry.insert(0, "Nom d'utilisateur")
        self.pw_entry.insert(0, "Mot de passe")

        """Ajout des champs de saisies au canvas"""
        un_window = self.my_canvas.create_window(
            34, 
            290, 
            anchor='nw', 
            window=self.un_entry)
        pw_window = self.my_canvas.create_window(
            34, 
            370, 
            anchor='nw',
            window=self.pw_entry)
        
        """Définition du bouton"""
        self.login_btn = tkinter.Button(
            root, 
            text='Identification', 
            font='Helvetica 20', 
            width=15, 
            fg='#336d92', 
            command=self.welcome)
        self.login_btn_window = self.my_canvas.create_window(
            36, 
            470,
            anchor='nw', 
            window=self.login_btn)
        
        """Liaison avec les champs de saisies"""
        self.un_entry.bind('<Button-1>', self.entry_clear)
        self.pw_entry.bind('<Button-1>', self.entry_clear)

    def welcome(self):
        """Méthode permettant d'afficher le mot 'bonjour' 
        après avoir appuyé sur le bouton d'exécution"""

        """Destruction des champs de saisies et du bouton"""
        self.un_entry.destroy()
        self.pw_entry.destroy()
        self.login_btn.destroy()

        """Ajout d'un message de bienvene"""
        self.my_canvas.create_text(
            160, 
            450, 
            text='Bienvenue !', 
            font='Helvetica 40', 
            fill='white')

    def entry_clear(self, e):
        """Méthode permettant de lier le champ de saisie 
        avec la souris : lorsqu'on clique sur le champs de saisie, 
        le texte affiché s'efface"""

        """Réinitialisation des champs de saisies"""
        if (self.un_entry.get() == 
            "Nom d'utilisateur" or 
            self.pw_entry.get() == "Mot de passe"):
            self.un_entry.delete(0, 'end')
            self.pw_entry.delete(0, 'end')

        """Lettres cachées par des étoiles"""
        self.pw_entry.config(show='*')
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
