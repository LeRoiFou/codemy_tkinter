"""
Tkinter - Codemy.com #97 : Threading With Tkinter
Lien : https://www.youtube.com/watch?v=jnrCpA1xJPQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=97

Un thread permet de réaliser en même temps plus d'une fonction (voir partie modules : Threading)
Dans le programme ci-après, on dispose de deux boutons qui permettent d'effectuer deux instructions l'une par rapport à
l'autre :
-> Le 1er bouton permet d'afficher un message au bout de 5 secondes après avoir appuyé sur ce bouton ;
-> Le 2ème bouton permet d'afficher un chiffre au hasard après avoir appuyé sur ce bouton.
Mais sans recourir à un thread, on ne peut pas appuyer sur ce 2ème bouton, tant que les 5 secondes ne se sont pas
écoulées après avoir appuyé sur le 1er bouton...

Pour cela, l'instruction thread va être effectué sur la fonction 'bloquante' et qui est au cas particuler l'exécution du
bouton n° 1

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

import tkinter
import time  # module pour le bouton n° 1
from random import randint  # module pour le bouton n° 2
# module permettant d'exécuter les deux boutons définies ci-après, en même temps
import threading  

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x400')
        self.widgets()
        
    def widgets(self):
        
        """Titre de la fenêtre, qui change de message après avoir 
        appuyé sur le bouton n°1"""
        self.my_label = tkinter.Label(root, text='Salut !')
        self.my_label.pack(pady=20)

        """Bouton d'exécution pour afficher un message 5 secondes 
        après avoir appuyé sur le bouton : dans ce widget, on rajoute 
        l'instruction threand lors de l'appel de la fonction five_seconds() 
        dans la commande"""
        my_button1 = tkinter.Button(root, 
                                    text='5 secondes', 
                                    command=threading.Thread(target=self.five_seconds).start())
        my_button1.pack(pady=20)

        """Bouton d'exécution permettant d'afficher 
        un chiffre au hasard entre 1 et 100"""
        my_button2 = tkinter.Button(root, 
                                    text='Choisir un nombre au hasard', 
                                    command=self.rando)
        my_button2.pack(pady=20)

        """Affichage d'un chiffre au hasard après avoir appuyé sur le bouton n° 2"""
        self.random_label = tkinter.Label(root, text='')
        self.random_label.pack(pady=20)
        
    def five_seconds(self):
        """Méthode affichant le texte suivant au bout de 5 secondes 
        après avoir appuyé sur le bouton n° 1"""
        
        time.sleep(5)
        self.my_label.config(text='Les 5 secondes se sont écoulées !')

    def rando(self):
        """Méthode affichant un chiffre au hasard entre 1 et 100 
        après avoir appuyé sur le bouton n° 2"""
        
        self.random_label.config(text=f"Nombre au hasard : {randint(1, 100)}")

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
