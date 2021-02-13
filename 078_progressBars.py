"""
Tkinter - Codemy.com #78 : Progress Bars With Tkinter
Lien : https://www.youtube.com/watch?v=Grbx15jRjQA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=78

Dans ce programme on apprend à créer une barre de progression dans laquelle se trouve une jauge de couleur verte.
Cette jauge verte va faire des allers-retours dans la barre de progression (un peu comme les yeux des robots), elle est
donc en mode 'indeterminate'

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Mon titre !')
root.geometry('600x400')


def step():
    """Avancée de la jauge verte dans la barre de progression"""
    # my_progress['value'] += 10  # incrémentation d'augmentation de la jauge par 10
    # my_progress.start(5)  # vitesse d'exécution de la jauge -> plus le chiffre est bas plus la jauge se déplace + vite
    for x in range(5):  # toutes les secondes, la jauge se déplace de 20 %
        my_label.config(text=my_progress['value'])  # affichage du % de progression de la jauge
        my_progress['value'] += 20  # incrémentation d'augmentation de la jauge par 20
        root.update_idletasks()  # mise à jour de la fenêtre
        time.sleep(1)  # temps = 1 seconde


def stop():
    """Arrêt du défilement de la jauge verte"""
    my_progress.stop()


"""Configuration de la barre de progression : le mode 'determinate' permet de cumuler la jauge verte qui va compléter la 
barre de progression du début à la fin alors que le mode 'indeterminate' permet de déplacer la jauge verte dans la barre  
de progression"""
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
my_progress.pack(pady=20)

"""Configuration du bouton d'exécution"""
my_button = Button(root, text='Démarrer', command=step)
my_button.pack(pady=20)

"""Configuration du bouton d'exécution"""
my_button2 = Button(root, text='Arrêter', command=stop)
my_button2.pack(pady=20)

"""Configuration d'une étiquette résultat"""
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
