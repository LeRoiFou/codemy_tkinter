"""
Tkinter - Codemy.com #128 : 
Dates and 2020 Countdown App - 
Python Tkinter GUI Tutorial #128
Lien : https://www.youtube.com/watch?v=TjRH1h0ClyI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=128

Dans ce programme on apprend à décompter le nombre de jours
restant d'ici la fin de l'année ... 2022

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

import tkinter
import time
import locale

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.title('Titre !')
        root.geometry('550x500')
        
        self.widgets()
        self.clock()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Compte à rebours"""
        
        # assignation du nombre de jours sur 2 ans
        days_in_2years = 365 * 2  
        
        # assignation du jour de l'année (001 à 366)
        todays_day_number = int(time.strftime('%j'))  
        
        # nombre de jours restant avant le 01-01-2023
        self.days_left = days_in_2years - todays_day_number  
        
        """Affichage message"""
        panic = tkinter.Label(
            root, 
            text='Ne pas paniquer !!!', 
            font='Helvetica 42', 
            bg='black', 
            fg='green')
        panic.pack(pady=20, ipadx=10, ipady=10)
        
        """Affichage de la date actuelle"""
        self.today_label = tkinter.Label(root, text='')
        self.today_label.pack(pady=20)

        """Affichage du compte à rebours"""
        countdown_label = tkinter.Label(
            root, 
            text=f"Il reste seulement {self.days_left} jours\
                \navant une année 2023 incroyable !!!",
            font='Helvetica 20')
        countdown_label.pack(pady=20)
        
    def clock(self):
        """Méthode permettant d'afficher la date actuelle"""
        
        # Conversion des données du module time en Français
        locale.setlocale(locale.LC_TIME, 'FR')
        
        # Configuration des fonctions predef de time
        day = time.strftime("%A")
        numb_day = time.strftime("%e")
        month = time.strftime("%B")
        year = time.strftime("%Y")
        self.today_label.config(
            text="Aujourd'hui nous sommes le "
            + day.capitalize() + ' ' 
            + numb_day + ' ' 
            + month.capitalize() + ' ' 
            + year)
        
        
if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
