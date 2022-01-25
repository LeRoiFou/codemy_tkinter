"""
Tkinter - Codemy.com #207 : Create War Card Game
Lien : https://www.youtube.com/watch?v=2BDx3poRPBY

Dans ce programme on apprend à créer un jeu de cartes :p
Cette fois-ci on créé un jeu de bataille navale

Éditeur : Laurent REYNAUD
Date : 25-01-22
"""

import tkinter as tk
import random
from PIL import Image, ImageTk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Jeu de cartes !")
        root.geometry('900x550')
        root.configure(background='green')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_frame = tk.Frame(root, bg='green')
        my_frame.pack(pady=20)
        
        # Cadre pour le distributeur
        dealer_frame = tk.LabelFrame(my_frame, text='Distributeur', bd=0)
        dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)
        
        # Label pour insérer une image
        self.dealer_label = tk.Label(dealer_frame, text='')
        self.dealer_label.pack(pady=20)
        
        # Cadre pour le joueur
        player_frame = tk.LabelFrame(my_frame, text='Joueur', bd=0)
        player_frame.grid(row=0, column=1, ipadx=20)
        
        # Label pour insérer une image
        self.player_label = tk.Label(player_frame, text='')
        self.player_label.pack(pady=20)
        
        # Affichage du score : qui a gagné ?
        self.score_label = tk.Label(
            root, text='', font='Helvetica 14', bg='green')
        self.score_label.pack(pady=20)
        
        # Bouton pour relancer le jeu
        shuffle_button = tk.Button(root, text="Relancer", 
                                   font='helvetica 14', command=self.shuffle)
        shuffle_button.pack(pady=20)
        
        # Bouton pour poser les cartes
        card_button = tk.Button(root, text="Poser", 
                                font='helvetica 14', command=self.deal_cards)
        card_button.pack(pady=20)
        
        # Affichage des cartes dès le lancement du jeu
        self.shuffle()
        
    def resize_cards(self, card):
        "Configuration des images des cartes"
        
        # Ouverture de l'image
        our_card_img = Image.open(card)
        
        # Reconfiguration de l'image
        our_card_resize_image = our_card_img.resize((150, 218))
        
        # Chargement de l'image
        self.our_card_image = ImageTk.PhotoImage(our_card_resize_image)
        
        return self.our_card_image
        
    def shuffle(self):
        "Méthode permettant de relancer le jeu"
        
        # Assignation d'une liste de valeur des cartes
        suits = ['clubs', 'diamonds', 'hearts', 'spades'] # trèfle, carreau...
        
        # Assignation d'une liste du nombre de cartes par valeur
        values = range(2, 15) # carte '2' jusqu'à la carte 'As'
        
        # Assignation des 52 cartes dans une liste
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")
        # print(len(self.deck)) # 52 cartes dans la liste
        
        # Assignation des joueurs dans des listes
        self.dealer = []
        self.player = []
        
        # Assignation d'une liste des scores distributeur / joueur
        self.dscore = []
        self.pscore = []
        
        "Pour le distributeur"
        
        # Choix d'une carte au hasard
        dealer_card = random.choice(self.deck)
        
        # Ajout d'une carte au distributeur
        self.dealer.append(dealer_card)
        
        # Récupération de l'image affectée 
        # au composant de la liste self.deck
        self.dealer_image = self.resize_cards(f'pic/cards/{dealer_card}.png')
        
        # Affichage de la carte dans le GUI
        self.dealer_label.config(image=self.dealer_image)
        
        "Pour le joueur"
        
        # Choix d'une carte au hasard
        player_card = random.choice(self.deck)
        
        # Ajout d'une carte au joueur
        self.player.append(player_card)
        
        # Récupération de l'image affectée 
        # au composant de la liste self.deck
        self.player_image = self.resize_cards(f'pic/cards/{player_card}.png')
        
        # Affichage de la carte dans le GUI
        self.player_label.config(image=self.player_image)
        
        "Mise à jour du titre de la fenêtre principale"
        root.title(f"{len(self.deck)} cartes")
        
        "Obtention du score"
        self.score(dealer_card, player_card)
    
    def deal_cards(self):
        "Méthode permettant de poser les cartes"
        
        try:
            
            "Pour le distributeur"
            
            # Choix d'une carte au hasard
            dealer_card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(dealer_card)
            
            # Ajout d'une carte au Dealer
            self.dealer.append(dealer_card)
            
            # Récupération de l'image affectée 
            # au composant de la liste self.deck
            self.dealer_image = self.resize_cards(
                f'pic/cards/{dealer_card}.png')
            
            # Affichage de la carte dans le GUI
            self.dealer_label.config(image=self.dealer_image)
            
            "Pour le joueur"
            
            # Choix d'une carte au hasard
            player_card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(player_card)
            
            # Ajout d'une carte au Dealer
            self.player.append(player_card)
            
            # Récupération de l'image affectée 
            # au composant de la liste self.deck
            self.player_image = self.resize_cards(
                f'pic/cards/{player_card}.png')
            
            # Affichage de la carte dans le GUI
            self.player_label.config(image=self.player_image)
            
            "Mise à jour du titre de la fenêtre principale"
            root.title(f'{len(self.deck)} cartes restantes')
            
            "Obtention du score"
            self.score(dealer_card, player_card)

        except:
            # Intervention sur le titre de la fenêtre principale du jeu
            if self.dscore.count('x') == self.pscore.count('x'):    
                root.title(f"Fin du jeu - Ex aequo ! {self.dscore.count('x')} à {self.pscore.count('x')}")
            elif self.dscore.count('x') > self.pscore.count('x'): 
                root.title(f"Fin du jeu - Le distributeur à gagné : {self.dscore.count('x')} à {self.pscore.count('x')}")
            else:
                root.title(f"Fin du jeu - Le joueur à gagné : {self.pscore.count('x')} à {self.dscore.count('x')}")
            
    def score(self, dealer_card, player_card):
        "Bataille navale ! Affichage du score"
        
        # Récupération du numéro à chaque nom du fichier de l'image
        dealer_card = int(dealer_card.split("_", 1)[0])
        player_card = int(player_card.split("_", 1)[0])
        
        # Comparaison du n° des cartes et affichage des résultats
        if dealer_card == player_card:
            self.score_label.config(text="Ex aequo !")
        elif dealer_card > player_card:
            self.score_label.config(text="Le distributeur a gagné !")
            # ajout d'un 'x' dans la liste 
            # à chaque fois que le distributeur a gagné
            self.dscore.append("x") 
        else:
            self.score_label.config(text="Le joueur a gagné !")
            # ajout d'un 'x' dans la liste 
            # à chaque fois que le joueur a gagné
            self.pscore.append("x")
            
        "Mise à jour du titre de la fenêtre principale"
        root.title(
            f"{len(self.deck)} cartes | Distributeur : {self.dscore.count('x')}     Joueur : {self.pscore.count('x')}")
        
        
if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
