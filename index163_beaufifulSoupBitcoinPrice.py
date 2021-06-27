"""
Tkinter - Codemy.com #163 : 
Bitcoin Price Web Scraper With BeautifulSoup 
- Python Tkinter GUI Tutorial #163
Lien : https://www.youtube.com/watch?v=LQsZyGNM9ag

Dans ce programme on apprend à connaître la valeur du Bitcoin 
toutes les 30 secondes à partir d'un site internet.
À la différence du module API, ici les données sont prises directement 
sur un site internet, comme par exemple connaître
le cours du fioul au jour le jour...

Le code source de la page web concernée a été copiée avec un clique droit
de la souris sur la page web concernée ->
"Afficher le code source de la page" puis CTRL+A puis CTRL+C et CTRL+V 
dans un nouveau fichier .html afin de trouver le nom de la classe 
où se trouve la ligne où est affichée la valeur du bitcoin

Package à télécharger : beautifulsoup4

Dans ce programme on affiche également le temps et la date actuel 
(voir tuto tkinter 79_Time&Locale)
Concernant l'instruction strftime du module time, voir le lien : 
https://www.tutorialspoint.com/python/time_strftime.htm

Éditeur : Laurent REYNAUD
Date : 19-01-21
"""

import tkinter
# permet d'obtenir la mise à jour des données
from bs4 import BeautifulSoup  
# récupération des données d'une URL
import urllib  
from urllib import request
# mise à jour des données à un temps T
from datetime import datetime  
# conversion du module time en français
import locale  

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('550x210')
        root.config(bg='black')
        
        # Configuration du temps
        self.my_time()
        # Configuration des widgets
        self.widgets()
        # Lancement du programme mise à jour toutes les 30 secondes
        self.update()
        
    def my_time(self):
        "Configuration du temps"
        
        """Conversion des données du module time en français"""
        locale.setlocale(locale.LC_TIME, 'FR')

        """Temps actuel"""
        now = datetime.now()
        self.current_time = now.strftime('%H:%M:%S')

        """Assignation d'une variable booléenne"""
        self.previous = False
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration d'une fenêtre"""
        my_frame = tkinter.Frame(root, bg='black')
        my_frame.pack(pady=20)

        """Chargement d'une image"""
        self.logo = tkinter.PhotoImage(file='images/bitcoin.png')
        logo_label = tkinter.Label(my_frame, image=self.logo, bd=0)
        logo_label.grid(row=0, column=0, rowspan=2)

        """Ajout du label 'bitcoin'"""
        self.bit_label = tkinter.Label(
            my_frame,
            text='TEST', 
            font='Helvetica 45', 
            bg='black', 
            fg='green', 
            bd=0)
        self.bit_label.grid(row=0, column=1, padx=20, sticky='s')

        """Dernière valeur du bitcoin"""
        self.latest_price = tkinter.Label(
            my_frame, 
            text='test de déplacement', 
            font='Helvetica 8', 
            bg='black', 
            fg='grey')
        self.latest_price.grid(row=1, column=1, sticky='n')
        
        """Création d'une barre de statuts"""
        self.status_bar = tkinter.Label(
            root, 
            text=f"Dernière mise à jour : {self.current_time}    ", 
            bd=0, 
            anchor='e', 
            bg='black', 
            fg='grey')
        self.status_bar.pack(fill='x', side='bottom', ipady=2)
        
    def update(self):
        """Mise à jour de la valeur du bitcoin toutes les 30 secondes"""

        """Récupération de la valeur du bitcoin"""
        
        # site internet de la valeur bitcoin
        my_path = 'https://www.coindesk.com/price/bitcoin'
        page = urllib.request.urlopen(my_path).read()  
        
        # récupération de la page source du site internet concerné
        html = BeautifulSoup(page, 'html.parser')  
        
        # récupération du nom de la classe où se trouve la ligne 
        # de la valeur du bitcoin
        price_large = html.find(class_='price-large')  
        
        # affichage de la ligne récupérée du fichier .html
        print(price_large)  
        
        # conversion de la chaîne de récupération du fichier html en str
        price_large1 = str(price_large)  
        
        # récupération de la valeur du bitcoin dans la str
        price_large2 = price_large1[54:63]  
        
        # mise à jour de l'étiquette
        self.bit_label.config(text=f"${price_large2}")  

        """Mise à jour de la fenêtre principale toutes les 30 secondes"""
        root.after(30_000, self.update)  # 30_000 ms = 30 secondes

        """Temps actuel"""
        now = datetime.now()
        self.current_time = now.strftime('%H:%M:%S')

        """Mise à jour de la barre de statuts"""
        self.status_bar.config(
            text=f"Dernière mise à jour : {self.current_time}    ")

        """Sélection du cours en cours"""
        current = price_large2

        """Suppression de la virgule affichée à la valeur du bitcoin
        pour les centimes"""
        current = current.replace(',', '')

        """Détermination du changement de valeur entre deux visus"""
        
        # si faux (la variable self.previous est toujours une booléenne)
        if self.previous:  
            
            # si la valeur actuelle a diminué 
            # (la variable self.previous devient un float)
            if float(self.previous) > float(current):  
                self.latest_price.config(
                    text=f"La valeur du Bitcoin a baissé de "
                    f"{round(float(self.previous) - float(current), 2)} $", 
                    fg='red')
                
            # si la valeur actuelle est inchangée    
            elif float(self.previous) == float(current):  
                self.latest_price.config(
                    text='Valeur du bitcoin inchangée', 
                    fg='grey')
                
            # si vrai :    
            else:  
                self.latest_price.config(
                    text=f"La valeur du Bitcoin a augmenté de "
                    f"{round(float(current) - float(self.previous), 2)} $", 
                    fg='green')
                
        # sinon si vrai (la variable self.previous est toujours une booléenne)
        else:  
            
            # la variable self.previous devient un float
            self.previous = current  
            self.latest_price.config(
                text='Valeur du bitcoin inchangée',
                fg='grey')


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
