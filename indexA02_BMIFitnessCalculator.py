"""
Build A BMI Fitness Calculator - Tkinter Projects 1
Lien : https://www.youtube.com/watch?v=NHL6ZcZDjG4



Éditeur : Laurent REYNAUD
Date : 24-08-22
"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("BMI Fitness calculator")
        root.geometry('500x650')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Define our image
        self.meter = ImageTk.PhotoImage(Image.open('images/meter2.png'))
        meter_img = tk.Label(root, image=self.meter, bd=0)
        meter_img.pack(pady=20)
        
        # Define entry boxes
        self.h_entry = ctk.CTkEntry(root, placeholder_text="Height In Inches",
                               width=200, height=30, border_width=1, 
                               corner_radius=10)
        self.h_entry.pack(pady=20)
        
        self.w_entry = ctk.CTkEntry(root, placeholder_text="Weight in Pounds",
                               width=200, height=30, border_width=1, 
                               corner_radius=10)
        self.w_entry.pack(pady=20)
        
        # Buttons
        button_1 = ctk.CTkButton(root, text="Calculate BMI",
                                 width=190, height=40, compound='top',
                                 command=self.get_bmi)
        button_1.pack(pady=20)
        
        button_2 = ctk.CTkButton(root, text="Clear screen",
                                 width=190, height=40, fg_color='#D35B58',
                                 hover_color='#C77C78',
                                 command=self.clear_screen)
        button_2.pack(pady=20)
        
        # Result
        self.results = ctk.CTkLabel(root, text="",
                               text_font='Helvetica 28')
        self.results.pack(pady=50)
        
    def clear_screen(self):
        
        self.h_entry.delete(0, tk.END)
        self.w_entry.delete(0, tk.END)
        self.results.config(text="")

    def get_bmi(self):
        
        # Calculate BMI
        # (weight_pounds/height_inches^2) * 703
        our_height = int(self.h_entry.get()) * int(self.h_entry.get())
        our_weight = int(self.w_entry.get()) 
        bmi = (our_weight / our_height) * 703
        bmi_rounded = round(bmi, 1)
        
        self.results.config(text=f"{str(bmi_rounded)}")
        
        # Logic
        if bmi_rounded < 18.5 :
               self.results.config(text=f"{str(bmi_rounded)}\nUnderweight", 
                                   text_color="#54b1e1")
        elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
                self.results.config(text=f"{str(bmi_rounded)}\nNormal", 
                                   text_color="#b3d686")
        elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
                self.results.config(text=f"{str(bmi_rounded)}\nOverweight", 
                            text_color="#fed429")
        elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
                self.results.config(text=f"{str(bmi_rounded)}\nObese", 
                                   text_color="#fbaf42")
        elif bmi_rounded >= 35.0:
                self.results.config(text=f"{str(bmi_rounded)}\nExtreme Obese", 
                                   text_color="#f25356")

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
