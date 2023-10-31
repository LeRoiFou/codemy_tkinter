"""
Titre : The TabView Widget - Tkinter CustomTkinter 12
Lien : https://www.youtube.com/watch?v=df30Qro3Iu4

Date : 31-10-2023
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("TabView!")
        root.geometry('700x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create Tabview
        my_tab = ctk.CTkTabview(
            root,
            width=600,
            height=250,
            corner_radius=10,
            fg_color='silver',
            segmented_button_fg_color='red',
            segmented_button_selected_color='green',
            segmented_button_selected_hover_color='pink',
            segmented_button_unselected_color='yellow',
            segmented_button_unselected_hover_color='purple',
            text_color='red',
            state='normal',
            command=self.clicker,
            )
        my_tab.pack(pady=10)
        
        # Create tabs
        tab1 = my_tab.add("Tab 1")
        tab2 = my_tab.add("Tab 2")
        
        # Put stuff in tabs
        self.my_button = ctk.CTkButton(tab1, text="Click Me!")
        self.my_button.pack(pady=40)
        
    def clicker(self):
       
       self.my_button.configure(text="You Clicked The Tab Button!") 
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
