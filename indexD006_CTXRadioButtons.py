"""
Titre : Radio Buttons in CustomTkinter - Tkinter CustomTkinter 7
Lien : https://www.youtube.com/watch?v=A48414Lz7NM


Date : 26-09-2023
"""

import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Radio Buttons!")
        root.geometry('700x400')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_label = ctk.CTkLabel(
            root, text="Do You Like Pizza?!", font=('Helvetica', 18))
        my_label.pack(pady=40)
        
        self.radio_var = ctk.StringVar(value='other')
        my_rad1 = ctk.CTkRadioButton(
            root, text="Yes I Do", value='Yes', variable=self.radio_var,
            # width=50,
            # height=50,
            radiobutton_width=50,
            radiobutton_height=50,
            corner_radius=1,
            border_width_unchecked=2,
            border_width_checked=5,
            border_color='red',
            hover_color='pink',
            fg_color='green',
            hover=True,
            text_color='red',
            font=('Helvetica', 18),
            state=tk.NORMAL,
            text_color_disabled='green',
            )
        my_rad1.pack(pady=10)
        
        my_rad2 = ctk.CTkRadioButton(
            root, text="No I Don't", value='No', variable=self.radio_var,)
        my_rad2.pack(pady=10)
        
        my_button = ctk.CTkButton(
            root, text="Select", command=self.get_rad)
        my_button.pack(pady=10)
        
        self.my_label2 = ctk.CTkLabel(root, text='', font=('Helvetica', 18))
        self.my_label2.pack(pady=10)
        
        
    def get_rad(self):
        
        if self.radio_var.get() == 'other':
            self.my_label2.configure(text="Please Make A Selection!")
        elif self.radio_var.get() == 'Yes':
            self.my_label2.configure(text="Of Course! You Like Pizza!")
        else:
            self.my_label2.configure(text="What's Wrong With You?!")
        
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    