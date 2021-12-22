"""
Tkinter - Codemy.com #203 : Add Text To Images With Pillow 
Lien : https://www.youtube.com/watch?v=bmzDUQRPEdE

Dans ce programme on apprend à ajouter du texte dans une image

Éditeur : Laurent REYNAUD
Date : 22-12-21
"""

import tkinter as tk
from PIL import Image, ImageFont, ImageDraw

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Textes insérés dans une image")
        root.geometry('600x600')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Charger une image
        self.my_image = tk.PhotoImage(file='pic/toblerone.png')
        
        # Titre
        self.my_label = tk.Label(
            root,
            image=self.my_image)
        self.my_label.pack(pady=20)
        
        # Zone de saisie
        self.my_entry = tk.Entry(
            root,
            justify='center',
            font='Helvetica 24')
        self.my_entry.pack(pady=20)
        
        # Bouton d'exécution
        my_button = tk.Button(
            root,
            text="Insérer le texte dans l'image",
            command=self.add_it,
            font='Helvetica 24')
        my_button.pack(pady=20)
        
    def add_it(self):
        "Insertion d'un texte dans une image"
        
        # Ouvrir une image
        self.my_image = Image.open('pic/toblerone.png')
        
        # Mise en forme du texte (type police et taille)
        text_font = ImageFont.truetype('arial.ttf', 46)
        
        # Obtention du texte saisi
        text_to_add = self.my_entry.get()
        
        # Editer l'image
        edit_image = ImageDraw.Draw(self.my_image)
        
        # Position du texte dans l'image
        edit_image.text(
            (150, 300), 
            text_to_add, 
            ('red'), 
            font=text_font)
        
        # Sauvegarde de l'image
        self.my_image.save('pic/toblerone2.png') 
        
        # Réinitialisation de la zone de saisie
        self.my_entry.delete(0, 'end')
        
        # Nouvelle saisie dans la zone de saisie
        self.my_entry.insert(0, "Fichier sauvegardé...")
        
        # Délai d'affichage de l'image modifiée
        self.my_label.after(2_000, self.show_pic)
        
    def show_pic(self):
        "Affichage de l'image modifiée"

        # Récupération de l'image modifiée
        self.my_image2 = tk.PhotoImage(file='pic/toblerone2.png')
        
        # Affichage de l'image modifiée
        self.my_label.config(image=self.my_image2)
        
        # Réinitialisation de la zone de saisie
        self.my_entry.delete(0, 'end')
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
