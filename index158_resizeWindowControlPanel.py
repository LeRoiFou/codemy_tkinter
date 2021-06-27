"""
Tkinter - Codemy.com #158 : 
Window Resizer Control Panel - Python Tkinter GUI Tutorial #158
Lien : https://www.youtube.com/watch?v=tRC5Yi50WM8&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=158

Dans ce programme on apprend à contrôler la taille d'une nouvelle fenêtre
avec des curseurs de la fenêtre principale

Éditeur : Laurent REYNAUD
Date : 01/01/21
"""

import tkinter
from tkinter import ttk

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('300x650')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Bouton d'exécution pour ouvrir une nouvelle fenêtre"""
        launch_button = tkinter.Button(
            root, 
            text='Ouvrir une fenêtre', 
            command=self.launch)
        launch_button.pack(pady=20)

        """Cadre pour la largeur de la nouvelle fenêtre"""
        width_frame = tkinter.LabelFrame(root, text='Largeur')
        width_frame.pack(pady=20)

        """Curseur pour la largeur"""
        self.width_slider = ttk.Scale(
            width_frame, 
            from_=100, 
            to=500, 
            orient='horizontal', 
            length=200, 
            command=self.width_slide, 
            value=100)
        self.width_slider.pack(pady=20, padx=20)

        """Cadre pour la hauteur de la nouvelle fenêtre"""
        height_frame = tkinter.LabelFrame(
            root, 
            text='Hauteur')
        height_frame.pack(pady=20)

        """Curseur pour la hauteur"""
        self.height_slider = ttk.Scale(
            height_frame, 
            from_=100, 
            to=500, 
            orient='vertical', 
            length=200, 
            command=self.height_slide, 
            value=100)
        self.height_slider.pack(pady=20, padx=20)

        """Cadre pour la largeur ET la hauteur de la nouvelle fenêtre"""
        both_frame = tkinter.LabelFrame(
            root, 
            text='Largeur et hauteur')
        both_frame.pack(pady=20)

        """Curseur pour la largeur ET la hauteur"""
        self.both_slider = ttk.Scale(
            both_frame, 
            from_=100, 
            to=500, 
            orient='horizontal', 
            length=200, 
            command=self.both_slide, 
            value=100)
        self.both_slider.pack(pady=20, padx=20)
        
    def launch(self):
        """Méthode permettant d'ouvrir une nouvelle fenêtre"""
        
        self.second = tkinter.Toplevel()
        self.second.geometry('200x200')

    def width_slide(self, *args):
        """Méthode permettant de redimensionner 
        la largeur de la nouvelle fenêtre"""
        
        self.second.geometry(
            f"{int(self.width_slider.get())}x{int(self.height_slider.get())}")

    def height_slide(self, *args):
        """Méthode permettant de redimensionner 
        la hauteur de la nouvelle fenêtre"""
        
        self.second.geometry(
            f"{int(self.width_slider.get())}x{int(self.height_slider.get())}")

    def both_slide(self, *args):
        """Méthode permettant de redimensionner 
        la largeur ET la hauteur de la nouvelle fenêtre"""
        self.second.geometry(
            f"{int(self.both_slider.get())}x{int(self.both_slider.get())}")


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
