"""
Titre : Sliders - Tkinter CustomTkinter 10
Lien : https://www.youtube.com/watch?v=SiOVaR2ve_M

Cours sur le curseur

Date : 17-10-2023
"""

import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Segmented Buttons!")
        root.geometry('700x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_slider = ctk.CTkSlider(
            root, 
            from_=0,
            to=100,
            command=self.sliding,
            orientation='horizontal',
            number_of_steps=10,
            width=400,
            height=50,
            # border_width=10,
            fg_color='red',
            progress_color='green',
            button_color='yellow',
            button_hover_color='orange',
            state=tk.NORMAL,
            hover=True,
            )
        my_slider.pack(pady=40)
        
        # Define starting point
        my_slider.set(0)
        
        self.my_label = ctk.CTkLabel(
            root, text=int(my_slider.get()), font=('Helvetica', 18))
        self.my_label.pack(pady=20)
        
    def sliding(self, value):
        # value = valeur du curseur
        
        self.my_label.configure(text=int(value))
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    