"""
Tkinter - Codemy.com #79 : Timers and Clocks with TKinter
Lien : https://www.youtube.com/watch?v=ruohUTTo8Kw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=79

Dans ce programme on affiche le temps et la date actuel
Concernant l'instruction strftime du module time, voir le lien : https://www.tutorialspoint.com/python/time_strftime.htm

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter
import time
import locale

locale.setlocale(locale.LC_TIME, 'FR')  # conversion des données du module time en Français

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.geometry('600x400')
        root.title('Mon titre !')
        self.widgets()
        self.clock()
    
    def widgets(self):
        
        """Configuration étiquette résultat (temps actuel)"""
        self.my_label = tkinter.Label(root, text='', font='Helvetica 48', fg='green', bg='black')
        self.my_label.pack(pady=20)

        """Configuration d'une deuxième étiquette (date actuelle)"""
        self.my_label2 = tkinter.Label(root, text='', font='Helvetica 14')
        self.my_label2.pack(pady=10)
        
    def clock(self):
        """Affichage de l'heure : minute : seconde actuelles :
        -> On déclare les variables de temps avec l'instruction strftime()
        -> L'étiquette résultat affiche le temps actuelle grâce à l'instruction config()
        -> Mise à jour de l'étiquette avec l'instruction after() 
        avec pour arguments le temps en millisecondes et 
        une fonction récursive (fonction s'appelant elle-même)"""
        
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        day = time.strftime("%A")
        numb_day = time.strftime("%e")
        month = time.strftime("%B")
        year = time.strftime("%Y")
        # affichage du temps actuel
        self.my_label.config(text=hour + ':' + minute + ':' + second)
        # mise à jour du temps avec en arguments : temps en millisecondes, fonction  
        self.my_label.after(1000, self.clock)  
        # affichage de la date actuelle
        self.my_label2.config(text=day + ' ' + numb_day + ' ' + month + ' ' + year)

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
