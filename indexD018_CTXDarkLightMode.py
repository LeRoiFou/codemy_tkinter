"""
Titre : Switching Between Light and Dark Mode - Tkinter CustomTkinter 19
Lien : https://www.youtube.com/watch?v=EwL2BwEdduE

Changement d'apparence de la fenêtre principale : dark / light

Date : 19-12-23
"""

import customtkinter as ctk
import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Light and Dark Mode!")
        root.geometry('700x450')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_text = ctk.CTkTextbox(root, width=600, height=300)
        self.my_text.insert(tk.END, "This is Dark Mode...")
        self.my_text.pack(pady=20)
        
        my_button = ctk.CTkButton(
            root, text="Change Light/Dark", command=self.change)
        my_button.pack(pady=20)
        
        self.mode = 'dark'
        
        colors = ['blue' ,'dark-blue', 'green']
        my_option = ctk.CTkOptionMenu(
            root, values=colors, command=self.change_colors)
        my_option.pack(pady=10)
        
    def change(self):
        
        if self.mode == 'dark' :
            ctk.set_appearance_mode('light')
            self.mode = 'light'
            self.my_text.delete(0.0, tk.END)
            self.my_text.insert(tk.END, "This is Light Mode...")
        else:
            ctk.set_appearance_mode('dark')
            self.mode = 'dark'
            self.my_text.delete(0.0, tk.END)
            self.my_text.insert(tk.END, "This is Dark Mode...")
            
    def change_colors(self, choice):
        ctk.set_default_color_theme(choice)
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
