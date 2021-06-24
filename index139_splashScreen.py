"""
Tkinter - Codemy.com #139 : 
How To Create A Splash Screen - Python Tkinter GUI Tutorial #139
Lien : https://www.youtube.com/watch?v=LTVvHObxc4E&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=139

Dans ce programme on apprend à afficher un écran de démarrage 
avant de lancer le programme.
Dans cet exemple une fenêtre présentant le logo apparaît avant 
une nouvelle fenêtre pour exécuter le programme souhaité

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

import tkinter
from PIL import ImageTk, Image

class Gui:
    
    def __init__(self, splash_root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre de démarrage
        self.splash_root = splash_root
        splash_root.geometry('300x200')
        # cette instruction permet de masquer la barre d'outils :
        splash_root.overrideredirect(True)  
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Logo"""
        self.splash_image = ImageTk.PhotoImage(
            Image.open('images/Logo.ico'))
        splash_label = tkinter.Label(image=self.splash_image)
        splash_label.pack(pady=20)
        
        """Temps d'affichage en millisecondes de la deuxième fenêtre"""
        # arguments : temps en millisecondes, appel fonction main_window()
        splash_root.after(2_000, self.main_window)  
        
    def main_window(self):
        """Fonction permettant d'effacer la fenêtre de démarrage 
        et d'afficher une deuxième fenêtre"""

        """Suppression de la fenêtre de démarrage"""
        splash_root.destroy()

        """Configuration de la 2ème fenêtre"""
        root = tkinter.Tk()
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x550')

        """Message"""
        main_label = tkinter.Label(
            root, 
            text='Deuxième fenêtre', 
            font='Helvetica 18')
        main_label.pack(pady=20)


if __name__ == '__main__':
    splash_root = tkinter.Tk()
    gui = Gui(splash_root)   
    # cette instruction ne fait pas appel cette fois-ci à une variable :
    tkinter.mainloop()  
