"""
Tkinter - Codemy.com #149 : Using Entry Boxes On Canvas - Python Tkinter GUI Tutorial #149
Lien : https://www.youtube.com/watch?v=32v2rdQnXvQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=149

Dans ce programme on insère un champ de saisi au canvas

L'instruction highlightthickness permet d'effacer la bordure qui contourne la fenêtre

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('323x576')
root.resizable(width=False, height=False)

"""Définition de l'image de fond de fenêtre"""
bg = ImageTk.PhotoImage(file='images/bg.png')

"""Définition du canvas"""
my_canvas = Canvas(root, width=323, height=576, bd=0, highlightthickness=0)
my_canvas.pack(fill='both', expand=True)

"""Mettre l'image dans le canvas"""
my_canvas.create_image(0, 0, image=bg, anchor='nw')

"""Définition des champs de saisies"""
un_entry = Entry(root, font='Helvetica 24', width=14, fg='#336d92', bd=0, justify='center')
pw_entry = Entry(root, font='Helvetica 24', width=14, fg='#336d92', bd=0, justify='center')

un_entry.insert(0, "Nom d'utilisateur")
pw_entry.insert(0, "Mot de passe")

"""Ajout des champs de saisies au canvas"""
un_window = my_canvas.create_window(34, 290, anchor='nw', window=un_entry)
pw_window = my_canvas.create_window(34, 370, anchor='nw', window=pw_entry)


def welcome():
    """Fonction permettant d'afficher le mot 'bonjour' après avoir appuyé sur le bouton d'exécution"""

    """Destruction des champs de saisies et du bouton"""
    un_entry.destroy()
    pw_entry.destroy()
    login_btn.destroy()

    """Ajout d'un message de bienvene"""
    my_canvas.create_text(160, 450, text='Bienvenue !', font='Helvetica 40', fill='white')


"""Définition du bouton"""
login_btn = Button(root, text='Identification', font='Helvetica 20', width=15, fg='#336d92', command=welcome)
login_btn_window = my_canvas.create_window(36, 470, anchor='nw', window=login_btn)


def entry_clear(e):
    """Fonction permettant de lier le champ de saisie avec la souris : lorsqu'on clique sur le champs de saisie, le
    texte affiché s'efface"""

    """Réinitialisation des champs de saisies"""
    if un_entry.get() == "Nom d'utilisateur" or pw_entry.get() == "Mot de passe":
        un_entry.delete(0, END)
        pw_entry.delete(0, END)

    """Lettres cachées par des étoiles"""
    pw_entry.config(show='*')


"""Liaison avec les champs de saisies"""
un_entry.bind('<Button-1>', entry_clear)
pw_entry.bind('<Button-1>', entry_clear)

root.mainloop()
