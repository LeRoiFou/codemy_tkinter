"""
Tkinter - Codemy.com #86 : Sounds and Music in Tkinter
Lien : https://www.youtube.com/watch?v=djDcVWbEYoE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=86

Lecture et arrêt d'une musique avec le module pygame dont ce package doit être installé

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

from tkinter import *
import pygame

root = Tk()
root.title('Mon titre !')
root.geometry('500x400')

"""Initiatialisation de la classe mixer du module pygame pour la musique"""
pygame.mixer.init()


def play():
    """Fonction permettant de charger la musique"""
    pygame.mixer.music.load('audio/OdeToSleep.mp3')
    pygame.mixer.music.play(loops=0)  # loops = boucle


def stop():
    """Fonction permettant d'arrêter la musique"""
    pygame.mixer.music.stop()


"""Configuration du bouton d'exécution du lancement de la musique"""
my_button = Button(root, text='Lancement', font='Helvetica 32', command=play)
my_button.pack(pady=20)

"""Configuration du bouton d'exécution de l'arrêt de la musique"""
stop_button = Button(root, text='Arrêter', command=stop)
stop_button.pack(pady=20)

root.mainloop()
