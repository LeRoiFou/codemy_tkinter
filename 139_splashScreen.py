"""
Tkinter - Codemy.com #139 : How To Create A Splash Screen - Python Tkinter GUI Tutorial #139
Lien : https://www.youtube.com/watch?v=LTVvHObxc4E&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=139

Dans ce programme on apprend à afficher un écran de démarrage avant de lancer le programme.
Dans cet exemple une fenêtre présentant le logo apparaît avant une nouvelle fenêtre pour exécuter le programme souhaité

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

from tkinter import *
from PIL import ImageTk, Image

"""Fenêtre de démarrage"""
splash_root = Tk()
splash_root.geometry('300x200')
splash_root.overrideredirect(True)  # cette instruction permet de masquer la barre d'outils de Pycharm

"""Logo"""
splash_image = ImageTk.PhotoImage(Image.open('images/Logo.ico'))
splash_label = Label(image=splash_image)
splash_label.pack(pady=20)


def main_window():
    """Fonction permettant d'effacer la fenêtre de démarrage et d'afficher une deuxième fenêtre"""

    """Suppression de la fenêtre de démarrage"""
    splash_root.destroy()

    """Configuration de la 2ème fenêtre"""
    root = Tk()
    root.iconbitmap('images/Logo.ico')
    root.title('Titre !')
    root.geometry('500x550')

    """Message"""
    main_label = Label(root, text='Deuxième fenêtre', font='Helvetica 18')
    main_label.pack(pady=20)


"""Temps d'affichage en millisecondes de la deuxième fenêtre"""
splash_root.after(3_000, main_window)  # arguments : temps en millisecondes, appel fonction main_window()

mainloop()  # cette instruction ne fait pas appel cette fois-ci à une variable
