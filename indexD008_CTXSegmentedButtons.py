"""
Titre : Segmented Buttons - Tkinter CustomTkinter 9
Lien : https://www.youtube.com/watch?v=BHa-WakZ31c

Des boutons collés les uns au autres 🫢 avec un nouveau composant :
CTkSegmentedButton

Date : 10-10-2023
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
        
        # Our button values
        my_values = ['John', 'April', 'Wes']
        
        # Create the button
        my_seg_button = ctk.CTkSegmentedButton(
            root, 
            values=my_values, 
            command=self.clicker,
            width=300,
            height=100,
            font=('Helvetica', 18),
            corner_radius=3,
            border_width=5,
            fg_color='red',
            selected_color='green',
            selected_hover_color='purple',
            unselected_color='pink',
            unselected_hover_color='orange',
            text_color='yellow',
            state=tk.NORMAL,
            text_color_disabled='blue',
            dynamic_resizing=True,
            )
        my_seg_button.pack(pady=40)
        
        # Set default selection
        # my_seg_button.set('John')
        
        # Label
        self.my_label = ctk.CTkLabel(root, text='', font=('Helvetica', 18))
        self.my_label.pack(pady=20)
        
    def clicker(self, value):
        
        self.my_label.configure(text=f'Hello {value}')

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    