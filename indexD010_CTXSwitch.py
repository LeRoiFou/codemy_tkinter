"""
Titre : The Switch Widget! - Tkinter CustomTkinter 11
Lien : https://www.youtube.com/watch?v=a0MVOloNLB4

Cours sur le bouton On/Off

Date : 24-10-2023
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("The Switch Widget!")
        root.geometry('700x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create a StringVar
        self.switch_var = ctk.StringVar(value='on')
        
        # Create Switch
        self.my_switch = ctk.CTkSwitch(
            root, 
            text='Switch', 
            command=self.switcher, 
            variable=self.switch_var,
            onvalue='on', 
            offvalue='off',
            # width=200,
            # height=100,
            switch_width=200,
            switch_height=25,
            # corner_radius=10,
            border_color='orange',
            border_width=5,
            fg_color='red',
            progress_color='green',
            button_color='pink',
            button_hover_color='yellow',
            font=("Helvetica", 24),
            text_color='blue',
            state='normal',
            
            )
        self.my_switch.pack(pady=40)
        
        # Create a Label
        self.my_label = ctk.CTkLabel(root, text='')
        self.my_label.pack(pady=20)
        
        # Create a Button
        my_button = ctk.CTkButton(
            root, text="Click Me!", command=self.clicker)
        my_button.pack(pady=10)
        
    def switcher(self):
        
        self.my_label.configure(text=self.switch_var.get())
        
    def clicker(self):
        
        # self.my_switch.deselect()
        # self.my_switch.select()
        self.my_switch.toggle()
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    