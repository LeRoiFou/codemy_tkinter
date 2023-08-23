"""
Titre : Entry Widgets in CustomTkinter - Tkinter CustomTkinter 3
Lien : https://www.youtube.com/watch?v=mwalgzuEfvw



Date : 23-08-2023
"""

import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("EntryWidgets!")
        root.geometry('600x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_label = ctk.CTkLabel(root, text='', font=('Helvetica', 24))
        self.my_label.pack(pady=40)
        
        self.my_entry = ctk.CTkEntry(
            root, 
            placeholder_text="Enter your name",
            height=50,
            width=200,
            font=("Helvetica", 18),
            corner_radius=50,
            text_color='green',
            placeholder_text_color='darkblue',
            fg_color=('blue', 'lightblue'), # outer, inner
            state=ctk.NORMAL,
            
            )
        self.my_entry.pack(pady=20)
        
        my_button = ctk.CTkButton(root, text="submit", command=self.submit)
        my_button.pack(pady=10)
        
        clear_button = ctk.CTkButton(root, text='clear', command=self.clear)
        clear_button.pack(pady=10)
        
    def submit(self):
        
        self.my_label.configure(text=f'Hello {self.my_entry.get()}!')
        self.my_entry.configure(state=ctk.DISABLED)
        
    def clear(self):
        
        self.my_entry.configure(state=ctk.NORMAL)
        self.my_entry.delete(0, ctk.END)
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    