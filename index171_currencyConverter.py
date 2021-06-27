"""
Tkinter - Codemy.com #171 : 
Build A Currency Converter App - Python Tkinter GUI Tutorial #171
Lien : https://www.youtube.com/watch?v=1VVlRgDZ0bg

Dans ce programme on apprend à convertir une devise en une autre devise, 
pour cela on a recours à une API
(interface de programmation applicative)

Éditeur : Laurent REYNAUD
Date : 18-03-21
"""

import tkinter
from tkinter import ttk
from tkinter import messagebox
import locale

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Devises')
        root.geometry('500x520')
                      
        # Configuration des onglets
        self.widgets()
        self.widgets_tab1()
        self.widgets_tab2()
        
    def widgets(self):
        "Configuration des widgets pour les deux onglets"
        
        # onglets
        self.my_notebook = ttk.Notebook(root)
        self.my_notebook.pack(pady=5)

        # cadre pour chaque onglet
        self.currency_frame = tkinter.Frame(
            self.my_notebook,
            width=480, 
            height=480)
        self.currency_frame.pack(fill='both', expand=1)
        self.conversion_frame = tkinter.Frame(
            self.my_notebook, 
            width=480, 
            height=480)
        self.conversion_frame.pack(fill='both', expand=1)

        # ajout des onglets
        self.my_notebook.add(self.currency_frame, text='Devises')
        self.my_notebook.add(self.conversion_frame, text='Conversion')

        # désactivation du 2ème onglet
        self.my_notebook.tab(1, state='disabled')
        
    def widgets_tab1(self):
        "Configuration des widgets de l'onglet n° 1 : devises"
        
        # cadre pour saisir la devise à convertir
        home = tkinter.LabelFrame(self.currency_frame, text='Votre devise')
        home.pack(pady=20)

        # champ de saisi du cours
        self.home_entry = tkinter.Entry(
            home, 
            font='Helvetica 24', 
            justify='center')
        self.home_entry.pack(pady=10, padx=10)

        # cadre pour la conversion de la devise
        conversion = tkinter.LabelFrame(
            self.currency_frame, 
            text='Conversion de la devise')
        conversion.pack(pady=20)

        # titre pour la conversion
        conversion_label = tkinter.Label(
            conversion, 
            text='Devise à convertir en...')
        conversion_label.pack(pady=10)

        # champ de saisi du cours à convertir
        self.conversion_entry = tkinter.Entry(
            conversion, 
            font='Helvetica 24', 
            justify='center')
        self.conversion_entry.pack(pady=10, padx=10)

        # titre pour le taux de conversion
        rate_label = tkinter.Label(
            conversion, 
            text='Taux de conversion')
        rate_label.pack(pady=10)

        # champ de saisi pour le taux
        self.rate_entry = tkinter.Entry(
            conversion, 
            font='Helvetica 24', 
            justify='center')
        self.rate_entry.pack(pady=10, padx=10)

        # cadre pour le bouton
        button_frame = tkinter.Frame(self.currency_frame)
        button_frame.pack(pady=20)

        # boutons
        lock_button = tkinter.Button(
            button_frame, 
            text='Bloquer', 
            command=self.lock)
        lock_button.grid(row=0, column=0, padx=10)

        unlock_button = tkinter.Button(
            button_frame, 
            text='Débloquer', 
            command=self.unlock)
        unlock_button.grid(row=0, column=1, padx=10)
        
    def widgets_tab2(self):
        "Configuration des widgets de l'onglet n° 2 : conversion"
        
        # cadre pour le montant à saisir
        self.amount_label = tkinter.LabelFrame(
            self.conversion_frame, 
            text='Montant à convertir')
        self.amount_label.pack(pady=20)

        # champ de saisi pour le montant
        self.amount_entry = tkinter.Entry(
            self.amount_label, 
            font='Helvetica 24', 
            justify='center')
        self.amount_entry.pack(pady=10, padx=10)

        # bouton pour convertir
        self.convert_button = tkinter.Button(
            self.amount_label, 
            text='Convertir',
            command=self.convert)
        self.convert_button.pack(pady=20)

        # Cadre du montant converti
        self.converted_label = tkinter.LabelFrame(
            self.conversion_frame, 
            text='Montant converti')
        self.converted_label.pack(pady=20)

        # champ de saisi du montant converti
        self.converted_entry = tkinter.Entry(
            self.converted_label, 
            font='Helvetica 24', 
            justify='center', 
            bd=0, 
            bg='systembuttonface')
        self.converted_entry.pack(pady=10, padx=10)

        # bouton pour effacer
        clear_button = tkinter.Button(
            self.conversion_frame, 
            text='Effacer', 
            command=self.clear)
        clear_button.pack(pady=20)

        # fausse étiquette pour l'espacement
        spacer = tkinter.Label(
            self.conversion_frame, 
            text='', width=68)
        spacer.pack()
        
    def lock(self):
        
        # si un des champs du 1er onglet n'est pas rempli...
        if (not self.home_entry.get() 
            or not self.conversion_entry.get() 
            or not self.rate_entry.get()):
            
            messagebox.showwarning(
                'Attention !', "Tu n'as pas rempli tous les champs !")
            
        else:
            
            # désactivation du champ du cours
            self.home_entry.config(state='disabled')
            
            # désactivation des champ du cours à convertir et taux du cours
            self.conversion_entry.config(state='disabled')
            self.rate_entry.config(state='disabled')
            
            # activation du 2ème onglet
            self.my_notebook.tab(1, state='normal')
            
            # changement des titres des cadres du 2ème onglet
            self.amount_label.config(
                text=(f"Cours en {self.home_entry.get()} \
à convertir en {self.conversion_entry.get()}"))
            self.converted_label.config(
                text=f"Équivaut en {self.conversion_entry.get()}")
            # changement du texte du bouton permettant 
            # de convertir le montant saisi
            self.convert_button.config(
                text=f"Conversion de la devise {self.home_entry.get()}")

    def unlock(self):
        
        # activation des champs du cours, 
        # du cours à convertir et du taux du cours
        self.home_entry.config(state='normal')
        
        self.conversion_entry.config(state='normal')
        
        self.rate_entry.config(state='normal')
        
        #  désactivation du 2ème onglet
        self.my_notebook.tab(1, state='disabled')

    def convert(self):
        
        # réinitialisation du champ de saisie du montant coverti
        self.converted_entry.delete(0, 'end')
        
        # assignation de la conversion du montant
        # du cours actuel x taux de la devise
        conversion = float(
            self.rate_entry.get()) * float(self.amount_entry.get())
        
        # conversion en deux décimales
        conversion = round(conversion, 2)
        
        # format numérique avec séparateur de milliers
        locale.setlocale(locale.LC_ALL, 'fr_FR')
        conversion = locale.currency(conversion, False, True, False)
        
        # mise à jour du montant converti
        self.converted_entry.insert(0, conversion)

    def clear(self):
        
        # réinitiation des champs de saisies
        self.amount_entry.delete(0, 'end')
        self.converted_entry.delete(0, 'end')
 

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
