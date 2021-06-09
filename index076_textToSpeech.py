"""
Tkinter - Codemy.com #76 : Text To Speech With Tkinter
Lien : https://www.youtube.com/watch?v=cP93Uw0wVyE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=76

Chargement du package pyttsx3 (PYthon Text To Speech x3)
Dans ce programme une voix de synthèse répète se que l'on écrit

La documentation se trouve dans le lien suivant : https://pyttsx3.readthedocs.io/en/latest/

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter
import pyttsx3  # module synthèse vocale

class GUI:
    
    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('800x500')   
        self.widgets() 
        
    def widgets(self):
        
        """Configuration du champ de saisi"""
        self.my_entry = tkinter.Entry(root, font='Helvetica 28', justify='center')
        self.my_entry.pack(pady=20)

        """Configuration du bouton d'exécution"""
        my_button = tkinter.Button(root, text='Parle !', command=self.talk)
        my_button.pack(pady=20)
        
    def talk(self):
        """Configuration de la voix de synthèse qui va répéter ce que l'on écrit dans le champ de saisi"""
        engine = pyttsx3.init()
        # rate = engine.getProperty('rate')  # vitesse de la voix
        # engine.setProperty('rate', rate + 500)  # vitesse de la voix
        engine.say(self.my_entry.get())
        engine.runAndWait()
        self.my_entry.delete(0, 'end')  # à chaque fois que la synthèse vocale a fini de parler, le champ de saisi est réinitialisé

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
