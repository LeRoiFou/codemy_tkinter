"""
Tkinter - Codemy.com #147 : 
How To Use Images as Backgrounds - Python Tkinter GUI Tutorial #147
Lien : https://www.youtube.com/watch?v=WurCpmHtQc4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=147

Dans ce programme on apprend à mettre une image en fond de fenêtre

2ème méthode : situation où on a un fond de couleurs dégradées de l'image...
Dans ce cas là on a recours au widget Canvas par contre on a plus recours 
à l'instruction fg pour la couleur d'écriture et le placement des widgets
ne requiert plus d'utiliser les instructions pack, grid ou place...
Cette méthode est plus complexe notamment pour positionner les widgets 
au bon endroit, car l'instruction grid avec row et column facilite 
largement l'emplacement des widgets notamment lorsqu'on attribue 
un cadre spécifique à certains widgets

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter

root = tkinter.Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('800x500')

"""Chargement de l'image"""
bg = tkinter.PhotoImage(file='images/space.png')

"""Création d'un canvas"""
my_canvas = tkinter.Canvas(root, width=800, height=500)
my_canvas.pack(fill='both', expand=True)

"""Affichage de l'image dans le canvas"""
my_canvas.create_image(0, 0, image=bg, anchor='nw')
# l'instruction anchor permet d'afficher pleinement l'image  

"""Ajout du titre"""
my_canvas.create_text(
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
button1_window = my_canvas.create_window(10, 10, anchor='nw', window=button1)
button2_window = my_canvas.create_window(55, 10, anchor='nw', window=button2)
button3_window = my_canvas.create_window(137, 10, anchor='nw', window=button3)

# """Affichage de l'image dans la fenêtre"""
# my_label = Label(root, image=bg)
# my_label.place(x=0, y=0, relwidth=1, relheight=1) 
# # relwidth/relheight -> l'image accrochée au centre de la fenêtre
#
# """Ajout d'un titre en haut de l'image"""
# my_text = Label(
    # root, 
    # text='Bienvenue !', 
    # font='Helvetica 50', 
    # fg='white', 
    # ='#6b88fe')
# my_text.pack(pady=50)
#
# """Ajout d'un cadre"""
# my_frame = Frame(root, bg='#6b88fe')
# my_frame.pack(pady=20)
#
# """Ajout de boutons"""
# my_button1 = Button(my_frame, text='Sortie')
# my_button1.grid(row=0, column=0, padx=10)
# my_button2 = Button(my_frame, text='Commencer')
# my_button2.grid(row=0, column=1, padx=10)
# my_button3 = Button(my_frame, text='Effacer')
# my_button3.grid(row=0, column=2, padx=10)

root.mainloop()
