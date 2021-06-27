"""
Tkinter - Codemy.com #157 : 
Color Changing Number Guessing Game - Python Tkinter GUI Tutorial #157
Lien : https://www.youtube.com/watch?v=6Bky5KsM2mg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=157

Dans ce programme on créé un jeu de devinette sur un nombre
à choisir entre 1 et 10 : plus on est proche du chiffre à
obtenir et plus la couleur de fenêtre passe 
du bleu (froid) au rouge (chaud)

Éditeur : Laurent REYNAUD
Date : 29-12-20
"""

import tkinter
from random import randint

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x500')
        
        # Générer un chiffre au hasard dès le lancement du jeu
        self.widgets()
        self.rando()
          
    def widgets(self):
        "Configuration des widgets"
    
        """Titre de la fenêtre"""
        self.num_label = tkinter.Label(
            root, 
            text='Choisis un chiffre\nentre 1 et 10', 
            font=('Brush Script MT', 32))
        self.num_label.pack(pady=20)
        
        """Champ de saisi"""
        self.guess_box = tkinter.Entry(
            root, 
            font='Helvetica 100', 
            justify='center', width=2)
        self.guess_box.pack(pady=20)

        """Bouton d'exécution pour recouper le chiffre 
        saisi et le chiffre attendu"""
        guess_button = tkinter.Button(
            root, 
            text='Soumettre', 
            command=self.guesser)
        guess_button.pack(pady=20)

        """Bouton d'exécution pour rejouer"""
        random_button = tkinter.Button(
            root, 
            text='Nouveau chiffre', 
            command=self.rando)
        random_button.pack(pady=20)
    
    def rando(self):
        """Méthode permettant de générer au hasard 
        un chiffre en entier entre 1 et 10"""

        """Assignation d'un chiffre au hasard entre 1 et 10"""
        self.num = randint(1, 10)

        """Réinitialisation de la couleur de fond de fenêtre"""
        root.config(bg='SystemButtonFace')

        """Réinitialisation du titre de la fenêtre 
        et de la couleur de fond"""
        self.num_label.config(
            text="Choisis un chiffre\nentre 1 et 10", 
            bg='SystemButtonFace')

        """Réinitialisation du champ de saisi"""
        self.guess_box.delete(0, 'end')      
    
    def guesser(self):
        """Méthode permettant de recouper entre le 
        chiffre saisi et le chiffre attendu"""

        if self.guess_box.get().isdigit():
            """Si le champ de saisi a un chiffre... 

            Message à afficher"""
            self.num_label.config(
                text="Choisis un chiffre\nentre 1 et 10")

            """Assignation de l'écart entre le chiffre saisi
            et le chiffre attendu en nombre absolu (pas de négatif)"""
            dif = abs(self.num - int(self.guess_box.get()))

            """Recoupement du chiffre saisi avec le chiffre attendu"""
            if int(self.guess_box.get()) == self.num:

                """Assignation de l'erreur affichée dès 
                que le chiffre saisi est égal au chiffre 
                attendu : mise en place de la couleur par défaut"""
                bc = 'SystemButtonFace'

                """Si le chiffre saisi est égal au chiffre attendu..."""
                self.num_label.config(text='Correct !')
            
            elif dif == 5:
                """Si l'écart entre le chiffre saisi et 
                le chiffre attendu est égal à 5 : 
                assignation d'une couleur blanche"""
                bc = 'white'
            
            elif dif < 5:
                """Si l'écart entre le chiffre saisi et 
                le chiffre attendu est inférieur à 5 : 
                assignation d'une couleur 
                rouge dégradée selon l'écart"""
                bc = f"#ff{dif}{dif}{dif}{dif}"
            
            else:
                """Sinon si l'écart entre le chiffre saisi 
                et le chiffre attendu est supérieur à 5 : 
                assignation d'une couleur bleue dégradée 
                selon l'écart"""
                bc = f"#{dif}{dif}{dif}{dif}ff"

            """Reconfiguration de la couleur de fond de la fenêtre"""
            root.config(bg=bc)

            """Reconfiguration de la couleur du titre de la fenêtre"""
            self.num_label.config(bg=bc)

        else:
            """Si le champ a autre qu'un chiffre (lettre...)... 

            Réinitialisation des données dans le champs de saisi"""
            self.guess_box.delete(0, 'end')

            """Information que le caractère saisi n'est pas un chiffre"""
            self.num_label.config(text="Hé ! Ce n'est pas un chiffre !")
            

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
