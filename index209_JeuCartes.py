"""
Tkinter - Codemy.com #208 : Check For Blackjack When Game Starts
Lien : https://www.youtube.com/watch?v=_ECjcYJah60

Dans ce programme on apprend à créer un jeu de cartes :p
Cette fois-ci on créé le jeu du black jack

Éditeur : Laurent REYNAUD
Date : 09-02-22
"""

import tkinter as tk
import random
from tkinter import ACTIVE, DISABLED, messagebox
from PIL import Image, ImageTk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Black Jack !")
        root.geometry('1200x750')
        root.configure(background='green')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_frame = tk.Frame(root, bg='green')
        my_frame.pack(pady=20)
        
        # Cadre pour le dealer
        dealer_frame = tk.LabelFrame(my_frame, text='dealer', bd=0)
        dealer_frame.pack(padx=20, ipadx=20)
        
        # Cartes du dealer
        self.dealer_label_1 = tk.Label(dealer_frame, text='')
        self.dealer_label_1.grid(row=0, column=0, pady=20, padx=20)
        
        self.dealer_label_2 = tk.Label(dealer_frame, text='')
        self.dealer_label_2.grid(row=0, column=1, pady=20, padx=20)
        
        self.dealer_label_3 = tk.Label(dealer_frame, text='')
        self.dealer_label_3.grid(row=0, column=2, pady=20, padx=20)
        
        self.dealer_label_4 = tk.Label(dealer_frame, text='')
        self.dealer_label_4.grid(row=0, column=3, pady=20, padx=20)
        
        self.dealer_label_4 = tk.Label(dealer_frame, text='')
        self.dealer_label_4.grid(row=0, column=4, pady=20, padx=20)
        
        self.dealer_label_4 = tk.Label(dealer_frame, text='')
        self.dealer_label_4.grid(row=0, column=5, pady=20, padx=20)
        
        # Cadre du player
        player_frame = tk.LabelFrame(my_frame, text='player', bd=0)
        player_frame.pack(ipadx=20, pady=10)
        
        # Cartes du player
        self.player_label_1 = tk.Label(player_frame, text='')
        self.player_label_1.grid(row=1, column=0,pady=20, padx=20)
        
        self.player_label_2 = tk.Label(player_frame, text='')
        self.player_label_2.grid(row=1, column=1,pady=20, padx=20)
        
        self.player_label_3 = tk.Label(player_frame, text='')
        self.player_label_3.grid(row=1, column=2,pady=20, padx=20)
        
        self.player_label_4 = tk.Label(player_frame, text='')
        self.player_label_4.grid(row=1, column=3,pady=20, padx=20)
        
        self.player_label_5 = tk.Label(player_frame, text='')
        self.player_label_5.grid(row=1, column=4,pady=20, padx=20)
        
        # Cadre pour les boutons
        button_frame = tk.Frame(root, bg='green')
        button_frame.pack(pady=20)
        
        # Boutons d'exécution
        shuffle_button = tk.Button(button_frame, text="Shuffle Deck", 
                                   font='helvetica 14', command=self.shuffle)
        shuffle_button.grid(row=0, column=0)
        
        self.card_button = tk.Button(button_frame, text="Hit Me!", 
                                font='helvetica 14', command=self.player_hit)
        self.card_button.grid(row=0, column=1, padx=10)
        
        self.stand_button = tk.Button(button_frame, text='Stand!', font='Helvetica 14')
        self.stand_button.grid(row=0, column=2)
        
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
    
    def blackjack_shuffle(self, player):
        "Résultat du score obtenu au blackjack"
       
        if player == "dealer":
            # Si le nombre de cartes posé est au nombre de 2
            if len(self.dealer_score) == 2:
                # Si le score des 2 cartes est de 21 points
                if self.dealer_score[0] + self.dealer_score[1] == 21 :
                    # Message informant que le dealer a gagné
                    messagebox.showinfo("Dealer wins!", 
                                        "BlackJack! Dealer wins!")
                    # Désactivation des boutons
                    self.card_button.config(state=DISABLED)
                    self.stand_button.config(state=DISABLED)
        
        if player == "player":
            # Si le nombre de cartes posé est au nombre de 2
            if len(self.player_score) == 2:
                # Si le score des 2 cartes est de 21 points
                if self.player_score[0] + self.player_score[1] == 21 :
                    # Message informant que le player a gagné
                    messagebox.showinfo("Player wins!", 
                                        "BlackJack! Player wins!")
                    # Désactivation des boutons
                    self.card_button.config(state=DISABLED)
                    self.stand_button.config(state=DISABLED)
          
    def shuffle(self):
        "Méthode permettant de relancer le jeu"
        
        # Réactivation des boutons après qu'un joueur ait gagné
        self.card_button.config(state=ACTIVE)
        self.stand_button.config(state=ACTIVE)
        
        # Suppression de toutes les cartes du précédent jeu
        self.dealer_label_1.config(image='')
        self.dealer_label_1.config(image='')
        self.dealer_label_1.config(image='')
        self.dealer_label_1.config(image='')
        self.dealer_label_1.config(image='')
        self.player_label_1.config(image='')
        self.player_label_2.config(image='')
        self.player_label_3.config(image='')
        self.player_label_4.config(image='')
        self.player_label_5.config(image='')
        
        # Assignation d'une liste de valeur des cartes
        suits = ['clubs', 'diamonds', 'hearts', 'spades'] # trèfle, carreau...
        
        # Assignation d'une liste du nombre de cartes par valeur
        values = range(2, 15) # carte '2' jusqu'à la carte 'As'
        
        # Assignation des 52 cartes dans une liste
        self.deck = []
        # Pour chaque valeur
        for suit in suits:
            # Pour chaque nombre
            for value in values:
                # Ajout de la carte dans une liste
                self.deck.append(f"{value}_of_{suit}")
        
        # Assignation du dealer et du player dans des listes
        self.dealer = []
        self.player = []
        
        # Assignation des scores du dealer et du player dans des listes
        self.dealer_score = []
        self.player_score = []
        
        # Assignation du nombre de cartes posées au dealer et au player
        self.dealer_spot = 0
        self.player_spot = 0
        
        # Donner deux cartes pour le dealer
        self.dealer_hit()
        self.dealer_hit()
        
        # Donner deux cartes pour le player
        self.player_hit()
        self.player_hit()
        
        # Mise à jour du titre de la fenêtre principale
        root.title(f"Reste {len(self.deck)} cartes")
    
    def dealer_hit(self):
        "Pose des cartes pour le dealer (max 5 cartes)"
        
        if self.dealer_spot < 5:
            try:
                
                # Choix d'une carte au hasard
                self.dealer_card = random.choice(self.deck)
                
                # Suppression de la carte jouée dans la liste
                self.deck.remove(self.dealer_card)
                
                # Ajout d'une carte au dealer
                self.dealer.append(self.dealer_card)
                
                # Récupération du n° de la carte
                dcard = int(self.dealer_card.split('_', 1)[0])
                
                # Si la carte est l'As
                if dcard == 14:
                    # cela vaut 11 points
                    self.dealer_score.append(11)
                # Si la carte est le Valet, la Reine ou le Roi
                elif dcard == 11 or dcard == 12 or dcard == 13:
                    # cela vaut 10 points
                    self.dealer_score.append(10)
                else:
                    # Sinon la carte vaut le nombre de points de sa valeur
                    self.dealer_score.append(dcard)
                
                # Pour chaque carte posée au jeu...
                
                if self.dealer_spot == 0:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image1 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_1.config(image=self.dealer_image1)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                    
                elif self.dealer_spot == 1:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image2 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_2.config(image=self.dealer_image2)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                elif self.dealer_spot == 2:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image3 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_3.config(image=self.dealer_image3)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                    
                elif self.dealer_spot == 3:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image4 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_4.config(image=self.dealer_image4)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                    
                elif self.dealer_spot == 4:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image5 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_5.config(image=self.dealer_image5)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                "Mise à jour du titre de la fenêtre principale"
                root.title(f'{len(self.deck)} cartes restantes')
                
            except:
                root.title("Plus de cartes en jeu")
            
            # Score réalisé par le dealer    
            self.blackjack_shuffle("dealer")
    
    def player_hit(self):
        "Pose des cartes pour le player (max 5 cartes)"
        
        if self.player_spot < 5:
            try:
                
                # Choix d'une carte au hasard
                player_card = random.choice(self.deck)
                
                # Suppression de la carte jouée dans la liste
                self.deck.remove(player_card)
                
                # Ajout d'une carte au player
                self.player.append(player_card)
                
                # Récupération du n° de la carte
                pcard = int(self.dealer_card.split('_', 1)[0])
                
                # Si la carte est l'As
                if pcard == 14:
                    # cela vaut 11 points
                    self.player_score.append(11)
                # Si la carte est le Valet, la Reine ou le Roi
                elif pcard == 11 or pcard == 12 or pcard == 13:
                    # cela vaut 10 points
                    self.player_score.append(10)
                else:
                    # Sinon la carte vaut le nombre de points de sa valeur
                    self.player_score.append(pcard)
                
                # Pour chaque carte posée au jeu...
                
                if self.player_spot == 0:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image1 = self.resize_cards(
                        f'pic/cards/{player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_1.config(image=self.player_image1)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                    
                elif self.player_spot == 1:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image2 = self.resize_cards(
                        f'pic/cards/{player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_2.config(image=self.player_image2)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                elif self.player_spot == 2:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image3 = self.resize_cards(
                        f'pic/cards/{player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_3.config(image=self.player_image3)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                    
                elif self.player_spot == 3:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image4 = self.resize_cards(
                        f'pic/cards/{player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_4.config(image=self.player_image4)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                    
                elif self.player_spot == 4:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image5 = self.resize_cards(
                        f'pic/cards/{player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_5.config(image=self.player_image5)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                "Mise à jour du titre de la fenêtre principale"
                root.title(f'{len(self.deck)} cartes restantes')
                
            except:
                root.title("Plus de cartes en jeu")
            
            # Score réalisé par le player
            self.blackjack_shuffle("player")
    
    # def deal_cards(self):
    #     "Méthode permettant de poser les cartes"
        
    #     try:
            
    #         "Pour le dealer"
            
    #         # Choix d'une carte au hasard
    #         card = random.choice(self.deck)
            
    #         # Suppression de la carte jouée dans la liste
    #         self.deck.remove(card)
            
    #         # Ajout d'une carte au Dealer
    #         self.dealer.append(card)
            
    #         # Récupération de l'image affectée 
    #         # au composant de la liste self.deck
    #         self.dealer_image = self.resize_cards(f'pic/cards/{card}.png')
            
    #         # Affichage de la carte dans le GUI
    #         self.dealer_label_1.config(image=self.dealer_image)
            
    #         "Pour le player"
            
    #         # Choix d'une carte au hasard
    #         card = random.choice(self.deck)
            
    #         # Suppression de la carte jouée dans la liste
    #         self.deck.remove(card)
            
    #         # Ajout d'une carte au Dealer
    #         self.player.append(card)
            
    #         # Récupération de l'image affectée 
    #         # au composant de la liste self.deck
    #         self.player_image = self.resize_cards(f'pic/cards/{card}.png')
            
    #         # Affichage de la carte dans le GUI
    #         self.player_label_1.config(image=self.player_image)
            
    #         "Mise à jour du titre de la fenêtre principale"
    #         root.title(f'{len(self.deck)} cartes restantes')

    #     except:
    #         root.title("Plus de cartes en jeu")
            

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
