"""
Titre : https://www.youtube.com/watch?v=bK9Xxa_nkO8
Lien : Custom Fonts Widget - Tkinter CustomTkinter 16

Modification de la police d'écriture avec le widget ctk.CTkFont()

Date : 28-11-2023
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Custom Fonts Widget!")
        root.geometry('400x200')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_font = ctk.CTkFont(
            family='Helvetica', size=44, weight='bold', slant='italic',
            underline=True, overstrike=True)
        
        self.my_label = ctk.CTkLabel(root, text="This is Text", font=self.my_font)
        self.my_label.pack(pady=40)
        
        my_button = ctk.CTkButton(
            root, text="Change Text", command=self.change)
        my_button.pack()
        
    def change(self):
        
        self.my_font.configure(
            underline=False, overstrike=False, size=22, slant='roman',)
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
