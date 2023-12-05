"""
Titre : Images in CustomTkinter - Tkinter CustomTkinter 17
Lien : https://www.youtube.com/watch?v=GMHtpH68Glo

Date : 05-12-23
"""

import customtkinter as ctk
from PIL import Image

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Images!")
        root.geometry('400x550')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_image = ctk.CTkImage(
            light_image=Image.open('pic/aspen.png'), 
            dark_image=Image.open('pic/aspen.png'),
            size=(180, 250), # width, height
            )
        
        my_label = ctk.CTkLabel(root, text="", image=my_image)
        my_label.pack(pady=10)
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
