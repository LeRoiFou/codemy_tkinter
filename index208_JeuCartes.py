"""
Tkinter - Codemy.com #208 : Build A Blackjack Card Game
Lien : https://www.youtube.com/watch?v=gBS2pYAGUgA

Dans ce programme on apprend à créer un jeu de cartes :p
Cette fois-ci on créé le jeu du black jack

Éditeur : Laurent REYNAUD
Date : 01-02-22
"""

import tkinter as tk
import random
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
        
        # Cadre pour le distributeur
        dealer_frame = tk.LabelFrame(my_frame, text='Distributeur', bd=0)
        dealer_frame.pack(padx=20, ipadx=20)
        
        # Cartes du distributeur
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
        
        # Cadre du joueur
        player_frame = tk.LabelFrame(my_frame, text='Joueur', bd=0)
        player_frame.pack(ipadx=20, pady=10)
        
        # Cartes du joueur
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
        shuffle_button = tk.Button(button_frame, text="Relancer", 
                                   font='helvetica 14', command=self.shuffle)
        shuffle_button.grid(row=0, column=0)
        
        card_button = tk.Button(button_frame, text="Une carte !", 
                                font='helvetica 14', command=self.player_hit)
        card_button.grid(row=0, column=1, padx=10)
        
        stand_button = tk.Button(button_frame, text='Stand!', font='Helvetica 14')
        stand_button.grid(row=0, column=2)
        
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
        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")
        # print(len(self.deck)) # 52 cartes dans la liste
        
        # Assignation du distributeur et du joueur dans des listes
        self.dealer = []
        self.player = []
        
        # Nombre de cartes posées au distributeur et au joueur
        self.dealer_spot = 0
        self.player_spot = 0
        
        # Donner deux cartes pour le distributeur et le joueur
        self.dealer_hit()
        self.dealer_hit()
        self.player_hit()
        self.player_hit()
        
        # Mise à jour du titre de la fenêtre principale
        root.title(f"{len(self.deck)} cartes")
    
    def dealer_hit(self):
        "Pose des cartes pour le distributeur (max 5 cartes)"
        
        if self.dealer_spot < 5:
            try:
                
                # Choix d'une carte au hasard
                dealer_card = random.choice(self.deck)
                
                # Suppression de la carte jouée dans la liste
                self.deck.remove(dealer_card)
                
                # Ajout d'une carte au distributeur
                self.dealer.append(dealer_card)
                
                if self.dealer_spot == 0:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image1 = self.resize_cards(
                        f'pic/cards/{dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_1.config(image=self.dealer_image1)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                    
                elif self.dealer_spot == 1:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image2 = self.resize_cards(
                        f'pic/cards/{dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_2.config(image=self.dealer_image2)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                elif self.dealer_spot == 2:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image3 = self.resize_cards(
                        f'pic/cards/{dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_3.config(image=self.dealer_image3)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                    
                elif self.dealer_spot == 3:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image4 = self.resize_cards(
                        f'pic/cards/{dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_4.config(image=self.dealer_image4)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                    
                elif self.dealer_spot == 4:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image5 = self.resize_cards(
                        f'pic/cards/{dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_5.config(image=self.dealer_image5)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                "Mise à jour du titre de la fenêtre principale"
                root.title(f'{len(self.deck)} cartes restantes')
                
            except:
                root.title("Plus de cartes en jeu")
    
    def player_hit(self):
        "Pose des cartes pour le joueur (max 5 cartes)"
        
        if self.player_spot < 5:
            try:
                
                # Choix d'une carte au hasard
                player_card = random.choice(self.deck)
                
                # Suppression de la carte jouée dans la liste
                self.deck.remove(player_card)
                
                # Ajout d'une carte au joueur
                self.player.append(player_card)
                
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
    
    def deal_cards(self):
        "Méthode permettant de poser les cartes"
        
        try:
            
            "Pour le distributeur"
            
            # Choix d'une carte au hasard
            card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(card)
            
            # Ajout d'une carte au Dealer
            self.dealer.append(card)
            
            # Récupération de l'image affectée 
            # au composant de la liste self.deck
            self.dealer_image = self.resize_cards(f'pic/cards/{card}.png')
            
            # Affichage de la carte dans le GUI
            self.dealer_label_1.config(image=self.dealer_image)
            
            "Pour le joueur"
            
            # Choix d'une carte au hasard
            card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(card)
            
            # Ajout d'une carte au Dealer
            self.player.append(card)
            
            # Récupération de l'image affectée 
            # au composant de la liste self.deck
            self.player_image = self.resize_cards(f'pic/cards/{card}.png')
            
            # Affichage de la carte dans le GUI
            self.player_label_1.config(image=self.player_image)
            
            "Mise à jour du titre de la fenêtre principale"
            root.title(f'{len(self.deck)} cartes restantes')

        except:
            root.title("Plus de cartes en jeu")
            

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
