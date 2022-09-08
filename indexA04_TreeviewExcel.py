"""
Tkinter - Codemy.com : Open Excel Spreadsheets In Treeview - Tkinter Projects 3
Lien : https://www.youtube.com/watch?v=Ooo3q7MuKMA

Récupération d'un fichier Excel pour le mettre 
dans un treeview à l'aide de Pandas

Éditeur : Laurent REYNAUD
Date : 08-09-22
"""

import customtkinter as ctk
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Treeview & Excel")
        root.geometry('850x400')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Treeview
        self.my_tree = ttk.Treeview(root)
        self.my_tree.pack(pady=20)
        
        # Hack the column height
        self.my_tree.heading('#0', text='\n')
        
        # Set tree style
        style = ttk.Style()
        style.theme_use("default")
        
        # Change style colors
        style.configure('Treeview',
                         background='#707070',
                         foreground='black',
                         rowheight=25,
                         fieldbackground='#707070')
        
        # Change color of headers
        style.configure('Treeview.Heading',
                        background='#535353',
                        foreground='black')
        
        # Change color of selected row
        style.map('Treeview', background=[('selected', '#535353')])
        
        # Button
        my_button = ctk.CTkButton(root, text="Open Excel file",
                                  command=self.open_excel)
        my_button.pack(pady=20)
        
    def open_excel(self):
        
        # Open a file
        my_file = filedialog.askopenfilename(
            title="Open file", filetype=(('Excel Files', '.xlsx'), 
                                         ('All files', '*.*')))
        
        # Grab the file to create a DF
        try:
            df = pd.read_excel(my_file)
        except Exception as e:
            messagebox.showerror("Woah!", f"There was a problem! {e}")
            
        # Clear the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        
        # Get the headers
        self.my_tree['column'] = list(df.columns)
        self.my_tree['show'] = 'headings'
        
        # Show the headers (list comprehension)
        [self.my_tree.heading(col, text=col) 
         for col in self.my_tree['column']]
        
        # Show data
        df_rows = df.to_numpy().tolist()
        [self.my_tree.insert('', 'end', values=row) for row in df_rows]
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
