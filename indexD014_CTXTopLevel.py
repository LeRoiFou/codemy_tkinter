"""
Titre : New Top Level Windows - Tkinter CustomTkinter 15
Lien : https://www.youtube.com/watch?v=FyPOqu3akDw


Date : 21-11-2023
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("New Top Level!")
        root.geometry('400x200')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_button = ctk.CTkButton(
            root, text="Open New Window", command=self.new)
        my_button.pack(pady=40)
        
    def new(self):
        
        self.new_window = ctk.CTkToplevel(root, fg_color='white')
        self.new_window.title("This is a new window!")
        self.new_window.geometry('400x200')
        self.new_window.resizable(True, False) # Width, Height
        
        # Close the window
        self.new_button = ctk.CTkButton(
            self.new_window, text="Close Window", command=self.close)
        self.new_button.pack(pady=40)
        
    def close(self):
        
        self.new_window.destroy()
        self.new_window.update()
        
        
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
