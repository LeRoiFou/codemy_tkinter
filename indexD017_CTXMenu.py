"""
Titre : Option Menu - Tkinter CustomTkinter 18
Lien : https://www.youtube.com/watch?v=R1IiIAp8wAY

Date : 12-12-23
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Menu!")
        root.geometry('700x450')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Set the options for our OptionMenu
        colors = ['Red', 'Green', 'Blue']
        
        self.my_option = ctk.CTkOptionMenu(
            root, 
            values=colors, 
            # command=self.color_picker,
            height=50,
            width=200,
            font=('Helvetica', 18),
            fg_color='white',
            dropdown_font=('Helvetica', 18),
            corner_radius=50,
            button_color='red',
            button_hover_color='green',
            dropdown_hover_color='green',
            dropdown_fg_color='blue',
            dropdown_text_color='orange',
            text_color='red',
            hover=True,
            anchor='center', # n-s-e-w-center
            state='normal',
            text_color_disabled='black',
            dynamic_resizing=False,
            )
        self.my_option.pack(pady=40)
        
        self.my_label = ctk.CTkLabel(root, text='')
        self.my_label.pack(pady=10)
        
        pick_button = ctk.CTkButton(
            root, text="Make Choice", command=self.color_picker2)
        pick_button.pack(pady=10)
        
        yellow_button = ctk.CTkButton(
            root, text="Pick Yellow", command=self.yellow)
        yellow_button.pack(pady=10)
        
    def color_picker(self, choice):
        
        self.my_label.configure(text=choice, text_color=choice)
        
    def color_picker2(self):
        
        self.my_label.configure(text=self.my_option.get(), 
                                text_color=self.my_option.get())
        
    def yellow(self):
        
        self.my_option.set('Yellow')
        
        self.my_label.configure(text=self.my_option.get(), 
                                text_color=self.my_option.get())
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
