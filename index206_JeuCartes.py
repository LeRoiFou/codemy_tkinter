"""
Tkinter - Codemy.com #206 : Create A Deck Of Cards And Deal Them Out
Lien : https://www.youtube.com/watch?v=xJZksz2UpqE

Dans ce programme on apprend à créer un jeu de cartes :p

Éditeur : Laurent REYNAUD
Date : 19-01-22
"""

import tkinter as tk
import random
from PIL import Image, ImageTk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Jeu de cartes !")
        root.geometry('900x500')
        root.configure(background='green')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_frame = tk.Frame(root, bg='green')
        my_frame.pack(pady=20)
        
        dealer_frame = tk.LabelFrame(my_frame, text='Distributeur', bd=0)
        dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)
        
        player_frame = tk.LabelFrame(my_frame, text='Joueur', bd=0)
        player_frame.grid(row=0, column=1, ipadx=20)
        
        self.dealer_label = tk.Label(dealer_frame, text='')
        self.dealer_label.pack(pady=20)
        
        self.player_label = tk.Label(player_frame, text='')
        self.player_label.pack(pady=20)
        
        shuffle_button = tk.Button(root, text="Mélanger le jeu", 
                                   font='helvetica 14', command=self.shuffle)
        shuffle_button.pack(pady=20)
        
        card_button = tk.Button(root, text="Récupérer les cartes", 
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
        "Méthode permettant de remélanger le jeu"
        
        # Définition des cartes
        suits = ['clubs', 'diamonds', 'hearts', 'spades'] # trèfle, carreau...
        values = range(2, 15) # carte '2' jusqu'à la carte 'As'
        
        # Assignation des cartes dans une liste
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")
                
        # print(len(self.deck)) # 52 cartes dans la liste
        
        # Assignation des joueurs dans des listes
        self.dealer = []
        self.player = []
        
        "Pour le distributeur"
        
        # Choix d'une carte au hasard
        card = random.choice(self.deck)
        
        # Réinitialisation
        # à chaque fois qu'on appuie sur le bouton
        self.deck.remove(card)
        
        # Ajout d'une carte au distributeur
        self.dealer.append(card)
        
        # Récupération de l'image affectée 
        # au composant de la liste self.deck
        self.dealer_image = self.resize_cards(f'pic/cards/{card}.png')
        
        # Affichage de la carte dans le GUI
        self.dealer_label.config(image=self.dealer_image)
        
        "Pour le joueur"
        
        # Choix d'une carte au hasard
        card = random.choice(self.deck)
        
        # Réinitialisation de la partie
        self.deck.remove(card)
        
        # Ajout d'une carte au Dealer
        self.player.append(card)
        
        # Récupération de l'image affectée 
        # au composant de la liste self.deck
        self.player_image = self.resize_cards(f'pic/cards/{card}.png')
        
        # Affichage de la carte dans le GUI
        self.player_label.config(image=self.player_image)
        
        "Mise à jour du titre de la fenêtre principale"
        root.title(f"{len(self.deck)} cartes")
        
    
    def deal_cards(self):
        "Méthode permettant de récupérer les cartes du jeu"
        
        try:
            
            "Pour le distributeur"
            
            # Choix d'une carte au hasard
            card = random.choice(self.deck)
            
            # Réinitialisation de la partie
            self.deck.remove(card)
            
            # Ajout d'une carte au Dealer
            self.dealer.append(card)
            
            # Récupération de l'image affectée 
            # au composant de la liste self.deck
            self.dealer_image = self.resize_cards(f'pic/cards/{card}.png')
            
            # Affichage de la carte dans le GUI
            self.dealer_label.config(image=self.dealer_image)
            
            "Pour le joueur"
            
            # Choix d'une carte au hasard
            card = random.choice(self.deck)
            
            # Réinitialisation
            self.deck.remove(card)
            
            # Ajout d'une carte au Dealer
            self.player.append(card)
            
            # Récupération de l'image affectée 
            # au composant de la liste self.deck
            self.player_image = self.resize_cards(f'pic/cards/{card}.png')
            
            # Affichage de la carte dans le GUI
            self.player_label.config(image=self.player_image)
            
            "Mise à jour du titre de la fenêtre principale"
            root.title(f'{len(self.deck)} cartes restantes')

        except:
            root.title("Plus de cartes en jeu")
        
        
if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
