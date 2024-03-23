"""
Titre : Create Custom Widgets and Components! - Object Oriented Tkinter 6
Lien : https://www.youtube.com/watch?v=CVIsMU7wVjI

Dans ce programme, on créé une classe avec la configuration de ses propres
composants

Date : 22-03-24
"""

import tkinter as tk

root = tk.Tk()
root.title("Create Custom Widgets and Components!")
root.geometry('700x450')

class MyWidget(tk.Frame) :
    
    def __init__(self, parent, label_text, button_text, button_name):
        
        # Héritage
        super().__init__(master=parent)
        
        # Set up our grid stuff
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1, uniform='z')
        
        # Create our widgets
        tk.Label(self, text=label_text, font=("Helvetica", 18)).grid(
            row=0, column=0, sticky="nsew")
        tk.Button(self, text=button_text, 
                  command=lambda : self.change(button_name)).grid(
            row=0, column=1, sticky="nsew")
        self.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Modification du titre de la page principale 
    def change(self, name):
        if name == "my_button1":
            root.title("Button 1!")
        elif name == "my_button2":
            root.title("Button 2!")
        elif name == "my_button3":
            root.title("Button 3!")
        else:
            root.title("Something else...")
        
MyWidget(root, "Text1", "Button 1", "my_button1")
MyWidget(root, "Text2", "Button 2", "my_button2")
MyWidget(root, "Text3", "Button 3", "my_button3")
MyWidget(root, "Text3", "Button 4", "my_button4")

if __name__ == '__main__':
    
    root.mainloop()
