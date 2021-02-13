"""
Tkinter - Codemy.com #123 : Custom Message Box Popups - Python Tkinter GUI Tutorial #123
Lien : https://www.youtube.com/watch?v=tpwu5Zb64lQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=123

Dans ce programme on customise le widget messagebox qui ne peut être modifié lorsqu'on a recours à cette instruction
(widget information, danger, alerte...), il faut donc crééer un faux widget messagebox

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('300x300')


def choice(option):
    """Lorsqu'on clique sur le bouton OUI / NON dans le faux widget messagebox, une message s'affiche dans la fenêtre
    principale"""
    pop.destroy()  # fermeture de la fenêtre du faux widget messagebox
    if option == 'OUI':
        my_label.config(text="Tu as cliqué sur 'OUI'")
    else:
        my_label.config(text="Tu as cliqué sur 'NON'")


def clicker():
    """Affichage d'un message box customisé"""

    """Configuration de la nouvelle fenêtre"""
    global pop
    pop = Toplevel(root)
    pop.title('Affichage')
    pop.geometry('250x200')
    pop.iconbitmap('images/Logo.ico')
    pop.config(bg='green')

    """Configuration de l'image à insérer"""
    global me  # si on n'assigne pas l'image en variable globale, elle ne s'affiche pas
    me = PhotoImage(file='images/LogoBis50x67.png')

    """Message 'titre'"""
    pop_label = Label(pop, text='Voulez-vous appuyer ?', bg='green', fg='white', font='Helvetica 12')
    pop_label.pack(pady=10)

    """Cadre"""
    my_frame = Frame(pop, bg='green')
    my_frame.pack(pady=50)

    """Affichage de l'image"""
    me_pic = Label(my_frame, image=me, borderwidth=0)
    me_pic.grid(row=0, column=0, padx=10)

    """Boutons"""
    yes = Button(my_frame, text='OUI', bg='orange', command=lambda: choice('OUI'))
    yes.grid(row=0, column=1, padx=10)
    no = Button(my_frame, text='NON', bg='yellow', command=lambda: choice('NON'))
    no.grid(row=0, column=2, padx=10)


"""Configuration du bouton d'exécution"""
my_button = Button(root, text='Clique !', command=clicker)
my_button.pack(pady=50)

"""Etiquette"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
