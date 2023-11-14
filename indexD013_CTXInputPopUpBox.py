"""
Titre : Input Popup Boxes - Tkinter CustomTkinter 14
Lien : https://www.youtube.com/watch?v=_fAvcEzITR0

Date : 14-11-2023
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Input Popup Boxes!")
        root.geometry('400x200')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create a button
        my_button = ctk.CTkButton(root, text="Click Me!", command=self.input)
        my_button.pack(pady=40)
        
        # Create a label
        self.my_label = ctk.CTkLabel(root, text='')
        self.my_label.pack(pady=10)
        
    def input(self):
        
        dialog = ctk.CTkInputDialog(
            text="What is your Name?", 
            title="Hello There!",
            fg_color='white',
            button_fg_color='red',
            button_hover_color='pink',
            button_text_color='black',
            entry_fg_color='green',
            entry_border_color='red',
            entry_text_color='black',
            )
        
        thing = dialog.get_input()
        
        if thing:
            self.my_label.configure(text=f"Hello {thing}")
        else:
            self.my_label.configure(text=f"You forgot to type anything!")
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
