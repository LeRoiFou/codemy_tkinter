"""
Tkinter - Codemy.com #6 : construire une calculatrice (suite)!
Lien : https://www.youtube.com/watch?v=XhCfsuMyhXo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=6

-> padx : le widget fait la largeur de la fenêtre
-> pady : le widget fait la hauteur de la fenêtre
-> borderwidth : profondeur du widget
-> columnspan : largeur du widget sur un certain nombre de colonnes

Remarque : avec l'expression lambda on ne peut pas recourir à la POO, la seule solution dans ce cas c'est d'effectuer
des variables de contrôles pour chaque bouton de la calculatrice en lien avec le champ de saisie Entry...

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

from tkinter import *

root = Tk()
root.title('Ma petite calculatrice')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_clear():
    e.delete(0, 'end')


def button_add():
    """Recours à l'instruction 'global' : cette variable globale f_num équivaut à une variable de classe en POO car elle
     va être utilisée dans une autre fonction"""
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, 'end')


def button_equal():
    second_number = e.get()
    e.delete(0, 'end')
    e.insert(0, f_num + int(second_number))


# Définition des boutons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_click = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=button_clear)

# Affichage des boutons à l'écran
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_click.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)


# e.insert(0, '')


def button_click(number):
    current = e.get()
    e.delete(0, 'end')
    e.insert(0, str(current) + str(number))


root.mainloop()
