"""
Titre : Check Boxes in CustomTkinter - Tkinter CustomTkinter 4
Lien : https://www.youtube.com/watch?v=fpziK1QintE

Dans ce programme, on utilise la librairie customtkinter, et on peut obtenir
des commandes directement avec l'instruction command sans recourir à une fonction

Date : 05-09-2023
"""

import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("CheckBoxes!")
        root.geometry('750x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # CheckBox State
        self.check_var = ctk.StringVar(value='off')
        
        # Checkbox Text
        self.text_var = ctk.StringVar(value='Would You Like to play Again?')
        
        self.my_check = ctk.CTkCheckBox(
            root, 
            text='Would You Like to play Again?', 
            variable=self.check_var,
            onvalue='on', 
            offvalue='off', 
            checkbox_width=50, checkbox_height=50,
            font=('helvetica', 18), 
            corner_radius=50,
            fg_color='red',
            hover_color='green',
            text_color='yellow',
            # hover=False,
            textvariable=self.text_var,
            )
        self.my_check.pack(pady=40)
        
        my_button = ctk.CTkButton(root, text="Submit", command=self.game)
        my_button.pack(pady=20)
        
        clear_button = ctk.CTkButton(root, text="Clear", command=self.clear_me)
        clear_button.pack(pady=20)
        
        toogle_button = ctk.CTkButton(
            root, text="Toggle", command=self.my_check.toggle)
        toogle_button.pack(pady=20)
        
        select_button = ctk.CTkButton(
            root, text="Select", command=self.my_check.select)
        select_button.pack(pady=20)
        
        self.my_label = ctk.CTkLabel(root, text='')
        self.my_label.pack(pady=20)
           
    def game(self):
        
        if self.check_var.get() == 'on':
            self.my_label.configure(text="You clicked the thing!")
        else:
            self.my_label.configure(text="You didn't click the thing!")
            
        self.text_var.set("Awesome!!")
            
    def clear_me(self):
        
        self.my_check.deselect()
        
        self.text_var.set("Would You Like to play Again?")

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    