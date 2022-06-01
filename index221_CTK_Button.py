"""
Tkinter - Codemy.com #221 : Modern Buttons With Images
Lien : https://www.youtube.com/watch?v=6VbzpWL49Q4

Toujours avec customtkinter, cette-fois on modernise les boutons avec des images

Instruction 'compound' : position de l'image dans le bouton

Éditeur : Laurent REYNAUD
Date : 01-06-22
"""

import customtkinter as ctk
from PIL import Image, ImageTk  # <- import PIL for the images

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Customisation des boutons")
        root.geometry('500x170')
        
        # Customisation de la fenêtre avec customtkinter
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Chargement des images
        add_folder_image = ImageTk.PhotoImage(
            Image.open('images/add-folder.png').resize((20,20), Image.ANTIALIAS))
        add_list_image = ImageTk.PhotoImage(
        Image.open('images/add-list.png').resize((20,20), Image.ANTIALIAS))
        
        # Boutons d'exécution
        button_1 = ctk.CTkButton(root, image=add_folder_image, text="Ajout 1...",
                                 width=190, height=40, compound='left')
        button_1.pack(pady=20, padx=20)
        button_2 = ctk.CTkButton(root, image=add_list_image, text="Ajout 2...",
                                 width=190, height=40, compound='right',
                                 fg_color='#D35B58', hover_color="#C77C78")
        button_2.pack(pady=20, padx=20)
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
