"""
Titre : Combo Boxes in CustomTkinter - Tkinter CustomTkinter 5
Lien : https://www.youtube.com/watch?v=xgSJWPE4DVc


Date : 12-09-2023
"""

import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Combo Boxes!")
        root.geometry('700x450')
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_label = ctk.CTkLabel(
            root, text="Pick A Color", font=('Helvetica', 18))
        self.my_label.pack(pady=40)
        
        colors = ['Red', 'Green', 'Blue']
        self.my_combo = ctk.CTkComboBox(
            root, 
            values=colors,
            height=50,
            width=200,
            font=('Helvetica', 18),
            dropdown_font=('Helvetica', 18),
            corner_radius=50,
            border_width=2,
            border_color='red',
            button_color='silver',
            button_hover_color='yellow',
            dropdown_hover_color='green',
            dropdown_fg_color='blue',
            dropdown_text_color='orange',
            text_color='purple',
            hover=True,
            justify='right',
            state=tk.NORMAL,
            )
        self.my_combo.pack(pady=0)
        
        my_button = ctk.CTkButton(
            root, text="Pick A Color", command=self.color_picker2)
        my_button.pack(pady=20)
        
        yellow_button = ctk.CTkButton(
            root, text="Pick Yellow!", command=self.color_picker_yellow)
        yellow_button.pack(pady=20)
        
        self.output_label = ctk.CTkLabel(root, text='', font=('Helvetica', 18))
        self.output_label.pack(pady=20)
        
        
    def color_picker(self, choice):    
        self.output_label.configure(text=choice, text_color=choice)
    
    def color_picker2(self):
        self.output_label.configure(
            text=self.my_combo.get(), text_color=self.my_combo.get())
        
    def color_picker_yellow(self):
        
        # Valeur unique pour le composant
        self.my_combo.set("Yellow")
        
        self.output_label.configure(
            text=self.my_combo.get(), text_color=self.my_combo.get())

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    