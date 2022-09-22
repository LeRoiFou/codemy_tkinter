"""
Tkinter - Codemy.com : How To Create Custom Widget Styles - Tkinter Projects 5
Lien : https://www.youtube.com/watch?v=hoiMu6wto1c

Dans ce programme on insère un style de widget personnalisé dans un widget,
l'instruction Style du sous-module ttk de tkinter

Éditeur : Laurent REYNAUD
Date : 22-09-22
"""

import tkinter as tk
from tkinter import ttk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Titre !")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Define a Style Widget
        style = ttk.Style()
        style.theme_use("classic")
        
        # Widget Style
        style.configure("laurent.TButton",
                        foreground="white",
                        background="#003066", # dark blue
                        font="Helvetica 24",
                        padding=[10,10,10,10])
        
        '''
        Widget Style Names :
        Button: TButton
        Checkbutton: TCheckbutton
        Combobox: TCombobox
        Entry: TEntry
        Frame: TFrame
        Label: TLabel
        LabelFrame: TLabelFrame
        Menubutton: TMenubutton
        Notebook: TNotebook
        PanedWindow: TPanedwindow
        Progressbar:  Horizontal.TProgressbar or Vertical.TProgressbar
        Radiobutton: TRadiobutton
        Scale: Horizontal.TScale or Vertical.TScale
        Scrollbar: Horizontal.TScrollbar or Vertical.TScrollbar
        Separator: TSeparator
        Sizegrip: TSizegrip
        Treeview: Treeview
        '''
        
        # Select widget : change style
        style.map("laurent.TButton", background=[('active', '#004ea5')]) # light blue
        
        # Create some Buttons
        
        # Button1 : style personnalisé
        my_button1 = ttk.Button(root, text="Login", style="laurent.TButton")
        my_button1.pack(pady=40)
        
        my_button2 = ttk.Button(root, text="Exit")
        my_button2.pack(pady=20)
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
