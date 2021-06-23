"""
Tkinter - Codemy.com #113 : Tic Tac Toe Game
Lien : https://www.youtube.com/watch?v=xx0qmpuA-vM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=113

Jeu du morpion !

Éditeur : Laurent REYNAUD
Date : 20-12-20
"""

import tkinter
# pour les boîtes de message (information, avertissement...)
from tkinter import messagebox  

class Gui:
    
    def __init__(self, root):
        
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Jeu du morpion !')
        # root.geometry('1200x710')
        
        self.widgets()
        self.reset() # réinitialisation du jeu
        
    def widgets(self):
        
        # assignation d'une variable = vrai
        self.clicked = True  
        
        # assignation d'un compteur qui ne doit pas dépasser 9 coups à jouer
        self.count = 0 
        
        """Configuration d'un menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Création d'un menu Options"""
        options_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Options', menu=options_menu)
        options_menu.add_command(
            label='Réinitialiser le jeu', 
            command=self.reset)
        
    def disable_all_buttons(self):
        """Méthode permettant de désactiver toutes les autres cases
        dès qu'un joueur a gagné avant les 9 coups"""
        
        self.b1.config(state='disabled')
        self.b2.config(state='disabled')
        self.b3.config(state='disabled')
        self.b4.config(state='disabled')
        self.b5.config(state='disabled')
        self.b6.config(state='disabled')
        self.b7.config(state='disabled')
        self.b8.config(state='disabled')
        self.b9.config(state='disabled')

    def checkifwon(self):
        """Méthode permettant de vérifier si quelqu'un a gagné"""

        self.winner = False  # pas de gagnant

        """Les 3 'X' sont alignées"""
        
        if (self.b1['text'] == 'X' 
            and self.b2['text'] == 'X' 
            and self.b3['text'] == 'X'):
            self.b1.config(bg='blue')
            self.b2.config(bg='blue')
            self.b3.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b4['text'] == 'X' 
              and self.b5['text'] == 'X' 
              and self.b6['text'] == 'X'):
            self.b4.config(bg='blue')
            self.b5.config(bg='blue')
            self.b6.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b7['text'] == 'X' 
              and self.b8['text'] == 'X' 
              and self.b9['text'] == 'X'):
            self.b7.config(bg='blue')
            self.b8.config(bg='blue')
            self.b9.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b1['text'] == 'X' 
              and self.b4['text'] == 'X' 
              and self.b7['text'] == 'X'):
            self.b1.config(bg='blue')
            self.b4.config(bg='blue')
            self.b7.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b2['text'] == 'X' 
              and self.b5['text'] == 'X' 
              and self.b8['text'] == 'X'):
            self.b2.config(bg='blue')
            self.b5.config(bg='blue')
            self.b8.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b3['text'] == 'X' 
              and self.b6['text'] == 'X' 
              and self.b9['text'] == 'X'):
            self.b3.config(bg='blue')
            self.b6.config(bg='blue')
            self.b9.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b1['text'] == 'X' 
              and self.b5['text'] == 'X' 
              and self.b9['text'] == 'X'):
            self.b1.config(bg='blue')
            self.b5.config(bg='blue')
            self.b9.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b3['text'] == 'X' 
              and self.b5['text'] == 'X' 
              and self.b7['text'] == 'X'):
            self.b3.config(bg='blue')
            self.b5.config(bg='blue')
            self.b7.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'X' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  

            """Les 3 'O' sont alignées"""
            
        elif (self.b1['text'] == 'O' 
              and self.b2['text'] == 'O' 
              and self.b3['text'] == 'O'):
            self.b1.config(bg='blue')
            self.b2.config(bg='blue')
            self.b3.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
        
        elif (self.b4['text'] == 'O' 
              and self.b5['text'] == 'O' 
              and self.b6['text'] == 'O'):
            self.b4.config(bg='blue')
            self.b5.config(bg='blue')
            self.b6.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b7['text'] == 'O' 
              and self.b8['text'] == 'O' 
              and self.b9['text'] == 'O'):
            self.b7.config(bg='blue')
            self.b8.config(bg='blue')
            self.b9.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b1['text'] == 'O' 
              and self.b4['text'] == 'O' 
              and self.b7['text'] == 'O'):
            self.b1.config(bg='blue')
            self.b4.config(bg='blue')
            self.b7.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b2['text'] == 'O' 
              and self.b5['text'] == 'O' 
              and self.b8['text'] == 'O'):
            self.b2.config(bg='blue')
            self.b5.config(bg='blue')
            self.b8.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b3['text'] == 'O' 
              and self.b6['text'] == 'O' 
              and self.b9['text'] == 'O'):
            self.b3.config(bg='blue')
            self.b6.config(bg='blue')
            self.b9.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
             # appel de la fonction permettant de désactiver 
             # les autres cases non cochées
            self.disable_all_buttons() 
        
        elif (self.b1['text'] == 'O' 
              and self.b5['text'] == 'O' 
              and self.b9['text'] == 'O'):
            self.b1.config(bg='blue')
            self.b5.config(bg='blue')
            self.b9.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  
            
        elif (self.b3['text'] == 'O' 
              and self.b5['text'] == 'O' 
              and self.b7['text'] == 'O'):
            self.b3.config(bg='blue')
            self.b5.config(bg='blue')
            self.b7.config(bg='blue')
            self.winner = True
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Les 'O' ont gagné !\nFélicitations !")
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  

    def b_click(self, b):
        """Méthode permettant de sélectionner une case
        L'instruction ci-dessous du bouton :
        b['text'] = ' '
        équivaut à l'instruction ci-dessous d'une étiquette :
        l.config(text=' ')"""

        if b['text'] == ' ' and self.clicked == True:
            """Si la case est vide et que l'on clique"""
            
            # le bouton affiche la lettre 'X'
            b['text'] = 'X'  
            
            # arrêt de la condition 'if' : 
            # la sélection du bouton suivant n'affichera pas 'X'
            self.clicked = False  
            
            # compteur de coup joué (limité à 9 coups)
            self.count += 1  
            
            # appel de la fonction permettant de vérifier si un joueur a gagné
            self.checkifwon()  
        
        elif b['text'] == ' ' and self.clicked == False:
            """Si la case est vide et que l'on a pas cliqué"""
            
            # le bouton affiche la lettre 'O'
            b['text'] = 'O'  
            
            # arrêt de la condition 'elif' : 
            # la sélection du bouton suivant n'affichera pas 'O'
            self.clicked = True  
            
            # compteur de coup joué (limité à 9 coups)
            self.count += 1  
            
            # appel de la fonction permettant de vérifier si un joueur a gagné
            self.checkifwon()  
        
        else:
            """Sinon si la case n'est pas vide et que l'on clique dessus"""
            
            messagebox.showerror(
                'Jeu du morpion !', 
                'Hé ! Cette case a déjà été cochée !\nNooob !!!')

        if self.count == 9 and self.winner == False:
            """Si on arrive à la case 9 et que personne n'a gagné"""
            
            messagebox.showinfo(
                'Jeu du morpion !', 
                "Personne n'a gagné !\nNullos !!!")
            
            # appel de la fonction permettant de désactiver 
            # les autres cases non cochées
            self.disable_all_buttons()  

    def reset(self):
        """Méthode permettant de réinitiliser le jeu"""

        """Les 9 cases du jeu construites sous la forme de boutons"""
        
        self.b1 = tkinter.Button(
            root, text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b1))
        
        self.b2 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b2))
        
        self.b3 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b3))

        self.b4 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b4))
        
        self.b5 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b5))
        
        self.b6 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b6))

        self.b7 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b7))
        
        self.b8 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b8))
        
        self.b9 = tkinter.Button(
            root, 
            text=' ', 
            font='Helevetica 20', 
            height=3, 
            width=6, 
            bg='SystemButtonFace',
            command=lambda: self.b_click(self.b9))

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
