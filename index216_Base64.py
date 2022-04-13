"""
Tkinter - Codemy.com #216 : Build A Base64 Encrypt and Decrypt Tool
Lien : https://www.youtube.com/watch?v=0NfDGNcuyAQ

Décryptage de mots saisis en base64 -> pour envoyer des messages secrets :p
Module installé : pybase64

Éditeur : Laurent REYNAUD
Date : 13-04-22
"""

import tkinter as tk
from tkinter import messagebox
import pybase64

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Build A Base64 Encrypt and Decrypt Tool")
        root.geometry('500x400')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_frame = tk.Frame(root)
        my_frame.pack(pady=20)
        
        enc_button = tk.Button(my_frame, text="Encrypt", font='Helvetica 18', command=self.encrypt)
        enc_button.grid(row=0, column=0)
        
        dec_button = tk.Button(my_frame, text="Decrypt", font='Helvetica 18', command=self.decrypt)
        dec_button.grid(row=0, column=1, padx=20)
        
        clear_button = tk.Button(my_frame, text="Clear", font='Helvetica 18', command=self.clear)
        clear_button.grid(row=0, column=2)
        
        enc_label = tk.Label(root, text="Encrypt/Decrypt Text...", font='Helvetica 14')
        enc_label.pack()
        
        self.my_text = tk.Text(root, width=57, height=10)
        self.my_text.pack(pady=10)
        
        password_label = tk.Label(root, text="Enter You Password...", font='Helvetica 14')
        password_label.pack()
        
        self.my_entry = tk.Entry(root, font='Helvetica 18', width=35, show='*')
        self.my_entry.pack(pady=10)
        
    def encrypt(self):
        "Bouton d'exécution Encrypt"
        
        # Récupération du texte de la zone de texte
        secret = self.my_text.get(1.0, 'end')
        
        # Réinitialisation de la zone de texte
        self.my_text.delete(1.0, 'end')
        
        # Si le mot de passe saisi est 'laurent'...
        if self.my_entry.get() == 'laurent':
            # Conversion en byte
            secret = secret.encode("ascii")
            # Conversion en base 64
            secret = pybase64.b64encode(secret)
            # Décodage en ascii
            secret = secret.decode('ascii')
            # Insertion dans la zone de texte : cryptage
            self.my_text.insert('end', secret)
        
        else:
            # Message en cas de mot de passe saisi incorrect
            messagebox.showwarning('Incorrect !', "Incorrect Password, Try Again!")
        
    
    def decrypt(self):
        "Bouton d'exécution Decrypt"
        
        # Récupération du texte de la zone de texte
        secret = self.my_text.get(1.0, 'end')
        
         # Réinitialisation de la zone de texte
        self.my_text.delete(1.0, 'end')
        
        # Si le mot de passe saisi est 'laurent'...
        if self.my_entry.get() == 'laurent':
            # Conversion en byte
            secret = secret.encode("ascii")
            # Déconversion en base 64
            secret = pybase64.b64decode(secret)
            # Décodage en ascii
            secret = secret.decode('ascii')
            # Insertion dans la zone de texte : décryptage
            self.my_text.insert('end', secret)
        
        else:
            # Message en cas de mot de passe saisi incorrect
            messagebox.showwarning('Incorrect !', "Incorrect Password, Try Again!")
        
    
    def clear(self):
        "Bouton d'exécution Clear"
        
        # Réinitialisation des saisies faites
        self.my_text.delete(1.0, 'end')
        self.my_entry.delete(0, 'end')
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
