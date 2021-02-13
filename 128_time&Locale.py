"""
Tkinter - Codemy.com #128 : Dates and 2020 Countdown App - Python Tkinter GUI Tutorial #128
Lien : https://www.youtube.com/watch?v=TjRH1h0ClyI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=128

Dans ce programme on apprend à décompter le nombre de jours restant d'ici la fin de l'année ... 2021

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *
import time
import locale

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('550x500')

"""Conversion des données du module time en Français"""
locale.setlocale(locale.LC_TIME, 'FR')

"""Affichage message"""
panic = Label(root, text='Ne pas paniquer !!!', font='Helvetica 42', bg='black', fg='green')
panic.pack(pady=20, ipadx=10, ipady=10)


def clock():
    """Fonction permettant d'afficher la date actuelle"""
    day = time.strftime("%A")
    numb_day = time.strftime("%e")
    month = time.strftime("%B")
    year = time.strftime("%Y")
    today_label.config(text="Aujourd'hui nous sommes le "
                            + day.capitalize() + ' ' + numb_day + ' ' + month.capitalize() + ' ' + year)


"""Affichage de la date actuelle"""
today_label = Label(root, text='')
today_label.pack(pady=20)

"""Appel de la fonction"""
clock()

"""Compte à rebours"""
days_in_2years = 365 * 2  # assignation du nombre de jours sur 2 ans
todays_day_number = int(time.strftime('%j'))  # assignation du jour de l'année (001 à 366)
days_left = days_in_2years - todays_day_number  # nombre de jours restant avant le 01-01-2023

"""Affichage du compte à rebours"""
countdown_label = Label(root, text=f"Il reste seulement {days_left} jours\navant une année 2023 incroyable !!!",
                        font='Helvetica 20')
countdown_label.pack(pady=20)

root.mainloop()
