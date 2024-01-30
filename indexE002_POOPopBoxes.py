"""
Titre : Popup Boxes - Object Oriented Tkinter 2
Lien : https://www.youtube.com/watch?v=5ixG5tv5AJQ

Date : 30-01-24
"""

import tkinter as tk
from tkinter import messagebox

class App(tk.Tk) :
    
    def __init__(self):
        
        # Héritage de la sous-librairie Tk de tkinter
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("POO - Popup Boxes!")
        self.geometry('700x450')
        
        self.my_label = tk.Label(
            self, text="Enter Your Name:", font=('Helvetica', 24),)
        self.my_label.pack(pady=20)
        
        self.my_entry = tk.Entry(self, width=30, font=('Helvetica', 24),)
        self.my_entry.pack(pady=20)
        
        self.my_button = tk.Button(self, text="Popup", command=self.popup)
        self.my_button.pack(pady=20)
        
    def popup(self):
        
        if self.my_entry.get():
            messagebox.showinfo("Hello", f"Hello {self.my_entry.get()}")
            
        else:
            messagebox.showerror(
                "Error", "You forgot to type in your name! Try again!")

if __name__ == '__main__':
    
    # Intanciation de la classe App et lancement de l'application
    app =  App()
    app.mainloop()
