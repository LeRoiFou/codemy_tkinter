"""
Tkinter - Codemy.com #198 : Create A Mortgage Calculator
Lien : https://www.youtube.com/watch?v=URozV-5yL-g



Éditeur : Laurent REYNAUD
Date : 17-11-2021
"""

import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Calculatrice financière')
        root.geometry('500x400')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        #region Cadre pour les commandes ci-après
        my_label_frame = tk.LabelFrame(
            root,
            text="Calculatrice financière")
        my_label_frame.pack(pady=30)
        
        #region Cadre pour saisir les données
        my_frame = tk.Frame(my_label_frame)
        my_frame.pack(
            pady=20, 
            padx=10)
        
        # Montant emprunté
        amount_label = tk.Label(
            my_frame,
            text="Montant emprunté")
        amount_label.grid(
            row=0, column=0)
        
        self.amount_entry = tk.Entry(
            my_frame,
            font='Helvetica 18',
            justify='center')
        self.amount_entry.grid(
            row=0, column=1)
        
        # Taux d'intérêt
        interest_label = tk.Label(
            my_frame,
            text="Taux d'intérêt")
        interest_label.grid(
            row=1, column=0)
        
        self.interest_entry = tk.Entry(
            my_frame,
            font='Helvetica 18',
            justify='center')
        self.interest_entry.grid(
            row=1, column=1, pady=20)
        
        # Nombre de jours
        term_label = tk.Label(
            my_frame,
            text="Nombre de jours")
        term_label.grid(
            row=2, column=0)
        
        self.term_entry = tk.Entry(
            my_frame,
            font='Helvetica 18',
            justify='center')
        self.term_entry.grid(
            row=2, column=1)
        
        #endregion
        
        my_button = tk.Button(
            my_label_frame, 
            text="Calculer l'annuité",
            command=self.payement)
        my_button.pack(pady=20)
        
        #endregion
        
        # Affichage du résultat
        self.payment_label = tk.Label(
            root,
            text="",
            font='Helvetica 18')
        self.payment_label.pack(pady=20)
        
    def payement(self):
        "Calcul de l'annuité"
        
        # Si chaque donnée est saisie...
        if (self.amount_entry.get() 
            and self.interest_entry.get() 
            and  self.term_entry.get()):
            
            # Année en entier
            years = int(self.term_entry.get())
            
            # Année x 12
            months = years * 12
            
            # Taux d'intérêts en nombre réel
            rate = float(self.interest_entry.get())
            
            # Montant emprunté en entier
            loan = int(self.amount_entry.get())
            
            # Taux mensuel
            monthly_rate = rate / 100 / 12
            
            # Calcul de l'annuité
            payment =((monthly_rate / (1 - (1 + monthly_rate))) 
                      ** (-months) * loan)
            
            # Mise en forme
            payment = f'{payment:,.2f}'
            
            # Affichage du résultat
            self.payment_label.config(
                text=f"Payement mensuel : {payment} €")
            
        else:
            self.payment_label.config(
                text="Hé ! Tu as oublié de tout saisir !")

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
