"""
Tkinter - Codemy.com #76 : Text To Speech With Tkinter
Lien : https://www.youtube.com/watch?v=cP93Uw0wVyE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=76

Chargement du package pyttsx3 (PYthon Text To Speech x3)
Dans ce programme une voix de synthèse répète se que l'on écrit

La documentation se trouve dans le lien suivant : https://pyttsx3.readthedocs.io/en/latest/

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

from tkinter import *
import pyttsx3  # module synthèse vocale

root = Tk()
root.title('Mon titre !')
root.geometry('800x500')


def talk():
    """Configuration de la voix de synthèse qui va répéter ce que l'on écrit dans le champ de saisi"""
    engine = pyttsx3.init()
    # rate = engine.getProperty('rate')  # vitesse de la voix
    # engine.setProperty('rate', rate + 500)  # vitesse de la voix
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0, END)  # à chaque fois que la synthèse vocale a fini de parler, le champ de saisi est réinitialisé


"""Configuration du champ de saisi"""
my_entry = Entry(root, font='Helvetica 28', justify='center')
my_entry.pack(pady=20)

"""Configuration du bouton d'exécution"""
my_button = Button(root, text='Parle !', command=talk)
my_button.pack(pady=20)

root.mainloop()
