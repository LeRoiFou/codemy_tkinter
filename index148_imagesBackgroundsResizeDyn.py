"""
Tkinter - Codemy.com #148 : 
Dynamically Resize Background Images - Python Tkinter GUI Tutorial #148
Lien : https://www.youtube.com/watch?v=xiGQD2J47nA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=148

Dans ce programme on continue à mettre une image au fond de la fenêtre, 
mais cette fois-ci on redimensionne dynamiquement l'image par rapport 
aux dimensions de la fenêtre

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
        root.geometry('800x500')
        root.bind('<Configure>', self.resizer)
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Chargement de l'image"""
        bg = ImageTk.PhotoImage(file='images/mario.png')

        """Création d'un canvas"""
        self.my_canvas = tkinter.Canvas(root, width=800, height=500)
        self.my_canvas.pack(fill='both', expand=True)

        """Affichage de l'image dans le canvas"""
        # l'instruction anchor permet d'afficher pleinement l'image
        self.my_canvas.create_image(0, 0, image=bg, anchor='nw')  

        """Ajout du titre"""
        self.my_canvas.create_text(
            400, 
            250, 
            text='Bienvenue !', 
            font='Helvetica 50', 
            fill='white')  # fill : couleur d'écriture

        """Ajout de boutons"""
        button1 = tkinter.Button(root, text='Sortie')
        button2 = tkinter.Button(root, text='Commencer')
        button3 = tkinter.Button(root, text='Effacer')

        """Ajout des boutons au canvas"""
        button1_window = self.my_canvas.create_window(
            10, 
            10, 
            anchor='nw', 
            window=button1)
        button2_window = self.my_canvas.create_window(
            55, 
            10, 
            anchor='nw', 
            window=button2)
        button3_window = self.my_canvas.create_window(
            137, 
            10, 
            anchor='nw', 
            window=button3)
        
    def resizer(self, e):
        """Méthode permettant de redynamiser 
        la taille de l'image avec la fenêtre"""

        """Chargement de l'image"""
        self.bg1 = Image.open('images/mario.png')

        """Redimensionner l'image"""
        self.resized_bg = self.bg1.resize(
            (e.width, e.height), 
            Image.ANTIALIAS)

        """Redéfinir à nouveau l'image"""
        self.new_bg = ImageTk.PhotoImage(self.resized_bg)

        """Ajout au canvas"""
        self.my_canvas.create_image(0, 0, image=self.new_bg, anchor='nw')

        """Ajout du titre"""
        self.my_canvas.create_text(
            400, 
            250, 
            text='Bienvenue !', 
            font='Helvetica 50', 
            fill='white')  # fill : couleur d'écriture

        
if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
