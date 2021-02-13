"""
Tkinter - Codemy.com #79 : Timers and Clocks with TKinter
Lien : https://www.youtube.com/watch?v=ruohUTTo8Kw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=79

Dans ce programme on affiche le temps et la date actuel
Concernant l'instruction strftime du module time, voir le lien : https://www.tutorialspoint.com/python/time_strftime.htm

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

from tkinter import *
import time
import locale

root = Tk()
root.title('Mon titre !')
root.geometry('600x400')

locale.setlocale(locale.LC_TIME, 'FR')  # conversion des données du module time en Français


def clock():
    """Affichage de l'heure : minute : seconde actuelles :
    -> On déclare les variables de temps avec l'instruction strftime()
    -> L'étiquette résultat affiche le temps actuelle grâce à l'instruction config()
    -> Mise à jour de l'étiquette avec l'instruction after() avec pour arguments le temps en millisecondes et une
    fonction récursive (fonction s'appelant elle-même)"""
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    numb_day = time.strftime("%e")
    month = time.strftime("%B")
    year = time.strftime("%Y")
    my_label.config(text=hour + ':' + minute + ':' + second)  # affichage du temps actuel
    my_label.after(1000, clock)  # mise à jour du temps avec en arguments : temps en millisecondes, fonction
    my_label2.config(text=day + ' ' + numb_day + ' ' + month + ' ' + year)  # affichage de la date actuelle


"""Configuration étiquette résultat (temps actuel)"""
my_label = Label(root, text='', font='Helvetica 48', fg='green', bg='black')
my_label.pack(pady=20)

"""Configuration d'une deuxième étiquette (date actuelle)"""
my_label2 = Label(root, text='', font='Helvetica 14')
my_label2.pack(pady=10)

"""Exécution de la fonction clock()"""
clock()

root.mainloop()
