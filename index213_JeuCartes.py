"""
Tkinter - Codemy.com #213 : Blackjack Player Stand and Dealer Hit
Lien : https://www.youtube.com/watch?v=IZusv0XiKwA

Dans ce programme, on attribue une commande au bouton d'exécution 'Arrêter de tirer'
afin d'établir la position du croupier selon le jeu du joueur.
Lors du prochain programme, il faut 'ajuster' la valeur de la carte de l'As pour le croupier
lorsqu'il tire une carte supplémentaire

Éditeur : Laurent REYNAUD
Date : 09-03-22
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
        
        # Cadre pour le crouper
        dealer_frame = tk.LabelFrame(my_frame, text='Croupier', bd=0)
        dealer_frame.pack(padx=20, ipadx=20)
        
        # Cartes du croupier
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
        
        self.dealer_label_5 = tk.Label(dealer_frame, text='')
        self.dealer_label_5.grid(row=0, column=5, pady=20, padx=20)
        
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
        shuffle_button = tk.Button(
            button_frame, text="Rejouer", font='helvetica 14', 
            width=20, command=self.shuffle)
        shuffle_button.grid(row=0, column=0)
        
        self.card_button = tk.Button(
            button_frame, text="Tirer une autre carte", font='helvetica 14', 
            width=20, command=self.player_hit)
        self.card_button.grid(row=0, column=1, padx=10)
        
        self.stand_button = tk.Button(
            button_frame, text='Arrêter de tirer', font='Helvetica 14',
            width=20, command=self.stand)
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
    
    def shuffle(self):
        "Bouton d'exécution : rejouer"
        
        # Total du score attribué à chaque participant
        self.player_total = 0
        self.dealer_total = 0
        
        # Assignation d'un dictionnaire du statut des participants :
        # 'no' signifie que lors du lancement du jeu, aucun joueur
        # n'est désigné pour l'instant gagnant
        self.blackjack_status = {'Croupier':'no', 'Joueur':'no'}
        
        # Réactivation des boutons après qu'un participant ait gagné
        self.card_button.config(state=ACTIVE)
        self.stand_button.config(state=ACTIVE)
        
        # Suppression de toutes les cartes du précédent jeu
        self.dealer_label_1.config(image='')
        self.dealer_label_2.config(image='')
        self.dealer_label_3.config(image='')
        self.dealer_label_4.config(image='')
        self.dealer_label_5.config(image='')
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
        
        # Assignation du croupier et du joueur dans des listes
        self.dealer = []
        self.player = []
        
        # Assignation des scores du croupier et du joueur dans des listes
        self.dealer_score = []
        self.player_score = []
        
        # Assignation du nombre de cartes posées au croupier et au joueur
        self.dealer_spot = 0
        self.player_spot = 0
        
        # Donner deux cartes pour le croupier
        self.dealer_hit()
        self.dealer_hit()
        
        # Donner deux cartes pour le joueur
        self.player_hit()
        self.player_hit()
        
        # Mise à jour du titre de la fenêtre principale
        root.title(f"Reste {len(self.deck)} cartes")
    
    def player_hit(self):
        """Bouton d'exécution : 'Tirer une autre carte'
        Pose d'une carte au joueur (max 5 cartes)"""
        
        # Si moins de 5 cartes ont été posées
        if self.player_spot < 5:
            try:
                
                # Choix d'une carte au hasard
                self.player_card = random.choice(self.deck)
                
                # Suppression de la carte jouée dans la liste
                self.deck.remove(self.player_card)
                
                # Ajout d'une carte au joueur
                self.player.append(self.player_card)
                
                # Récupération du n° de la carte
                pcard = int(self.player_card.split('_', 1)[0])
                
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
                
                # Si c'est la 1ère carte posée
                if self.player_spot == 0:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image1 = self.resize_cards(
                        f'pic/cards/{self.player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_1.config(image=self.player_image1)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                # Si c'est la 2ème carte posée        
                elif self.player_spot == 1:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image2 = self.resize_cards(
                        f'pic/cards/{self.player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_2.config(image=self.player_image2)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                # Si c'est la 3ème carte posée
                elif self.player_spot == 2:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image3 = self.resize_cards(
                        f'pic/cards/{self.player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_3.config(image=self.player_image3)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                # Si c'est la 4ème carte posée       
                elif self.player_spot == 3:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image4 = self.resize_cards(
                        f'pic/cards/{self.player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_4.config(image=self.player_image4)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                # Si c'est la 5ème carte posée     
                elif self.player_spot == 4:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.player_image5 = self.resize_cards(
                        f'pic/cards/{self.player_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.player_label_5.config(image=self.player_image5)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.player_spot += 1
                
                "Mise à jour du titre de la fenêtre principale"
                root.title(f'{len(self.deck)} cartes restantes')
                
            except:
                root.title("Plus de cartes en jeu")
            
            # Score réalisé par le joueur    
            self.blackjack_shuffle("Joueur")
    
    def stand(self):
        "Bouton d'exécution : 'Arrêter de tirer'"
        
        # Total du score attribué à chaque participant
        self.player_total = 0
        self.dealer_total = 0
        
        # Pour chaque valeur de points de ou des carte(s) posée(s)
        for score in self.dealer_score:
            # ajout de la valeur de ces points aux points des autres cartes
            self.dealer_total += score
            
        # Pour chaque valeur de points de ou des carte(s) posée(s)
        for score in self.player_score:
            # ajout de la valeur de ces points aux points des autres cartes
            self.player_total += score

        # Désactivation des boutons
        self.card_button.config(state=DISABLED)
        self.stand_button.config(state=DISABLED)
        
        # Si la valeur des points obtenus par le croupierr >= 17 points
        if self.dealer_total >= 17:
            # Si le croupier a + de 21 points (perdu)
            if self.dealer_total > 21:
                # Message informant que le joueur a gagné
                messagebox.showinfo("Vous avez gagné !", 
                                    f"Vous avez gagné ! Croupier : {self.dealer_total} // Joueur : {self.player_total}")
            # Si le croupier et le joueur ont le même nombre de points
            elif self.dealer_total == self.player_total:
                # Message informant qu'il y a égalité
                messagebox.showinfo("Ex-aequo!", 
                                    f"Ex-aequo! Croupier : {self.dealer_total} // Joueur : {self.player_total}")
            # Si le croupier a + de points que le joueur
            elif self.dealer_total > self.player_total:
                # Message informant que le croupier a gagné
                messagebox.showinfo("Le croupier a gagné !", 
                                    f"Le croupier a gagné ! Croupier : {self.dealer_total} // Joueur : {self.player_total}")
            # Sinon le croupier a perdu
            else:
                # Message informant que le joueur a gagné
                messagebox.showinfo("Vous avez gagné !", 
                                    f"Vous avez gagné ! Croupier : {self.dealer_total} // Joueur : {self.player_total}")
        # Si la valeur des points obtenus par le cropier < 17 points
        else:
            # Pose d'une nouvelle carte pour le croupier
            self.dealer_hit()
            # Exécution automatique du bouton 'Arrêter de tirer'
            self.stand()
    
    def dealer_hit(self):
        "Pose d'une carte au croupier (max 5 cartes)"
        
        # Si moins de 5 cartes ont été posées
        if self.dealer_spot < 5:
            try:
                
                # Choix d'une carte au hasard
                self.dealer_card = random.choice(self.deck)
                
                # Suppression de la carte jouée dans la liste
                self.deck.remove(self.dealer_card)
                
                # Ajout d'une carte au croupier
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
                
                # Si c'est la 1ère carte posée
                if self.dealer_spot == 0:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image1 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_1.config(image=self.dealer_image1)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                # Si c'est la 2ème carte posée    
                elif self.dealer_spot == 1:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image2 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_2.config(image=self.dealer_image2)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                # Si c'est la 3ème carte posée
                elif self.dealer_spot == 2:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image3 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_3.config(image=self.dealer_image3)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                # Si c'est la 4ème carte posée    
                elif self.dealer_spot == 3:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image4 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_4.config(image=self.dealer_image4)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                # Si c'est la 5ème carte posée    
                elif self.dealer_spot == 4:
                    
                    # Récupération de l'image affectée 
                    # au composant de la liste self.deck
                    self.dealer_image5 = self.resize_cards(
                        f'pic/cards/{self.dealer_card}.png')
                    
                    # Affichage de la carte dans le GUI
                    self.dealer_label_5.config(image=self.dealer_image5)
                    
                    # Incrémentation pour poser une nouvelle carte
                    self.dealer_spot += 1
                
                # Mise à jour du titre de la fenêtre principale
                root.title(f'{len(self.deck)} cartes restantes')
                
            except:
                root.title("Plus de cartes en jeu")
            
            # Score réalisé par le croupier    
            self.blackjack_shuffle("Croupier")
 
    def blackjack_shuffle(self, gamer):
        "Résultat du score obtenu au blackjack"
       
        # Total du score attribué à chaque participant
        self.player_total = 0
        self.dealer_total = 0

        # Statut du croupier
        if gamer == "Croupier":
            # Si le nombre de cartes posé est au nombre de 2
            if len(self.dealer_score) == 2:
                # Si le score des 2 cartes est de 21 points (blackjack !)
                if self.dealer_score[0] + self.dealer_score[1] == 21 :
                    # Mise à jour du statut du 'croupier' : yes = gagné
                    self.blackjack_status['Croupier'] = 'yes'
        
        # Statut du joueur
        if gamer == "Joueur":
           
            # Si le nombre de cartes posé est au nombre de 2
            if len(self.player_score) == 2:
                # Si le score des 2 cartes est de 21 points (blackjack !)
                if self.player_score[0] + self.player_score[1] == 21 :
                    # Mise à jour du statut du 'Joueur' : yes = gagné
                    self.blackjack_status['Joueur'] = 'yes'
            
            # S'il y a plus de deux cartes de posées
            else:
                
                # Pour chaque valeur de points de ou des carte(s) posée(s)
                for score in self.player_score:
                    # ajout de la valeur de ces points aux points des autres cartes
                    self.player_total += score
                    
                    # Si le score total est de 21 points (blackjack !)
                    if self.player_total == 21 :
                        self.blackjack_status['Joueur'] = 'yes'
                        
                    # Si le score total est > à 21 points
                    elif self.player_total > 21:
                        # Pour la valeur affectée à chaque carte
                        for card_num, card in enumerate(self.player_score):
                            # Si la carte vaut 11 points (carte 'As')
                            if card == 11:
                                # Changement de la valeur de la carte 'As'
                                self.player_score[card_num] = 1
                                # Réinitialisation du score total du joueur
                                self.player_total = 0
                                # Mise à jour du score total
                                for score in self.player_score:
                                    self.player_total += score
                                # Si le score total est > 21 points
                                if self.player_total > 21:
                                  self.blackjack_status['Joueur'] = 'bust'
                                 
                        # Sinon...
                        else:
                            if self.player_total == 21: 
                                self.blackjack_status['Joueur'] = 'yes' 
                            if self.player_total > 21:
                                self.blackjack_status['Joueur'] = 'bust' 
        
        # Si le nombre de cartes posées est de 2 par participant            
        if len(self.dealer_score) == 2 and len(self.player_score) == 2:
            
            # Si le score des 2 cartes des 2 participants est de 21 points (ex-aequo)
            if (self.blackjack_status['Croupier'] == 'yes'
                and 
                self.blackjack_status['Joueur'] == 'yes'):
                # Message informant qu'il y a égalité
                messagebox.showinfo("Ex-aequo !", 
                                    "Il y a égalité !")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)
            
            # Si le score des 2 cartes du 'croupier' est de 21 points
            elif self.blackjack_status['Croupier'] == 'yes':
                # Message informant que le croupier a gagné
                messagebox.showinfo("Le croupier a gagné !", 
                                    "BlackJack ! Le croupier a gagné !")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)
                
            # Si le score des 2 cartes du 'joueur' est de 21 points
            elif self.blackjack_status['Joueur'] == 'yes':
                # Message informant que le joueur a gagné
                messagebox.showinfo("Le joueur a gagné !", 
                                    "BlackJack! Le joueur a gagné !")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)
        
        # Sinon pour toutes nouvelles cartes posées (> 2 cartes)        
        else:
            
            # Si le score des 2 participants est de 21 points (ex-aequo)
            if (self.blackjack_status['Croupier'] == 'yes'
                and 
                self.blackjack_status['Joueur'] == 'yes'):
                # Message informant qu'il y a égalité
                messagebox.showinfo("Ex-aequo!", 
                                    "Il y a égalité !")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)
            
            # Si le score des cartes du 'croupier' est de 21 points
            elif self.blackjack_status['Croupier'] == 'yes':
                # Message informant que le croupier a gagné
                messagebox.showinfo("Le croupier a gagné !", 
                                    "BlackJack ! 21 ! Le croupier a gagné !")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)
                
            # Si le score des cartes du 'joueur' est de 21 points
            elif self.blackjack_status['Joueur'] == 'yes':
                # Message informant que le dealer a gagné
                messagebox.showinfo("Le joueur a gagné !", 
                                    "BlackJack ! 21 ! Le joueur a gagné !")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)
                
        # Si le score total est > à 21 points
        if self.blackjack_status['Joueur'] == 'bust':
            # Message informant que le croupier a gagné
                messagebox.showinfo("Le joueur a perdu !", 
                                    f"Le joueur a perdu ! Total {self.player_total} points")
                # Désactivation des boutons
                self.card_button.config(state=DISABLED)
                self.stand_button.config(state=DISABLED)    

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
