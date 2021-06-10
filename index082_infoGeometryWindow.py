"""
Tkinter - Codemy.com #82 : Get Height and Width Of Tkinter App
Lien : https://www.youtube.com/watch?v=_bZFyvMgS6M&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=82

Programme permettant d'afficher les dimensions de la fenêtre

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter

root = tkinter.Tk()
root.title('Mon titre !')
root.geometry('800x800')


def info():
    """Fonction permettant d'afficher les dimensions de la fenêtre"""
    dimension_label = tkinter.Label(root, text=root.winfo_geometry())
    dimension_label.pack(pady=20)
    height_label = tkinter.Label(root, text='Hauteur ' + str(root.winfo_height()))
    height_label.pack(pady=20)
    width_label = tkinter.Label(root, text='Largeur ' + str(root.winfo_width()))
    width_label.pack(pady=20)


"""Configuration du bouton d'exécution"""
my_button = tkinter.Button(root, text='Clique moi !', command=info)
my_button.pack(pady=20)

root.mainloop()
