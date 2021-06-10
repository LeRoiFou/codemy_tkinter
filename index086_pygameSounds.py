"""
Tkinter - Codemy.com #86 : Sounds and Music in Tkinter
Lien : https://www.youtube.com/watch?v=djDcVWbEYoE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=86

Lecture et arrêt d'une musique avec le module pygame dont ce package 
doit être installé

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter
import pygame

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('500x400')
        # Initiatialisation de la classe mixer du module pygame pour la musique
        pygame.mixer.init()
        self.widgets()
        
    def widgets(self):
        
        """Configuration du bouton d'exécution du lancement de la musique"""
        my_button = tkinter.Button(root, text='Lancement', font='Helvetica 32', command=self.play)
        my_button.pack(pady=20)

        """Configuration du bouton d'exécution de l'arrêt de la musique"""
        stop_button = tkinter.Button(root, text='Arrêter', command=self.stop)
        stop_button.pack(pady=20)
        
    def play(self):
        """Méthode permettant de charger la musique"""
        
        pygame.mixer.music.load('audio/OdeToSleep.mp3')
        pygame.mixer.music.play(loops=0)  # loops = boucle

    def stop(self):
        """Méthode permettant d'arrêter la musique"""
        
        pygame.mixer.music.stop()
        

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
