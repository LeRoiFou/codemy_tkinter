"""
Tkinter - Codemy.com #72 : Create A Date Picker Calendar
Lien : https://www.youtube.com/watch?v=fqfy-3IoVvs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=72

Création d'un calendrier en recourant au package 'tkcalendar'

Éditeur : Laurent REYNAUD
Date : 10-12-20
"""

from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Mon titre !')
root.geometry('600x400')

"""Configuration du calendrier version française"""
cal = Calendar(root, selectmode='day', year=2020, month=12, day=10, locale='Fr_fr')
cal.pack(pady=20, fill='both', expand=1)


def grab_date():
    """Fonction permettant d'afficher la date sélectionnée à partir du bouton 'Obtenir une date'"""
    my_label.config(text=cal.get_date())


"""Configuration du bout 'Obtenir une date'"""
my_button = Button(root, text='Obtenir une date', command=grab_date)
my_button.pack(pady=20)

"""Configuration de l'étiquette 'résultat'"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
