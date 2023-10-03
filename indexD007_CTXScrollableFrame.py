"""
Lien : https://www.youtube.com/watch?v=Envp9yHb2Ho
Cours : Scrollable Frames!! - Tkinter CustomTkinter 8

Insertion d'une barre de déroulement sur la fenêtre 🫢

Date : 03-10-23
"""
import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Scrollable Frames!!")
        root.geometry('700x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create a scrollable frame
        my_frame = ctk.CTkScrollableFrame(
            root, 
            orientation='vertical', # orientation de la barre de déroulement
            width=300, # largeur de la fenêtre
            height=200, # hauteur de la fenêtre
            label_text="Hello World!", # Titre
            label_fg_color='blue', # Couleur de fond du titre
            label_text_color='yellow', # Couleur de texte du titre
            label_font=('Helvetica', 18), # Type et taille de police
            label_anchor='w', # nw, center... positition du texte du titre
            border_width=3, # épaisseur bordure de la fenêtre
            border_color='green', # couleur bordure de la fenêtre
            fg_color='red', # couleur de fond de la fenêtre
            scrollbar_fg_color='yellow', # couleur barre de déroulement
            scrollbar_button_color='pink', # couleur mini barre de déroulement
            scrollbar_button_hover_color='blue', # idem mais en passant sur la barre
            corner_radius=20, # arrondi des bordures de la fenêtre
            )
        my_frame.pack(pady=40)
        
        # For loop for buttons
        [ctk.CTkButton(my_frame, text='This is a Button!!',).pack(pady=10)
         for _ in range(20)]

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
