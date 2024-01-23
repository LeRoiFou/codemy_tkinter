"""
Titre : Intro To Object Oriented Tkinter - Object Oriented Tkinter 1
Lien : https://www.youtube.com/watch?v=zstcMt9_80w

POO !

Date : 23-01-24
"""

import tkinter as tk

class App(tk.Tk) :
    
    def __init__(self):

        # Héritage de la sous-librairie Tk de tkinter
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("POO!")
        self.geometry('700x450')
        
        # Create status variable
        self.status = True
        
        # Create some widgets
        self.my_label = tk.Label(self, text="Hello World!", font=('Helvetica', 42))
        self.my_label.pack(pady=20)
        
        self.my_button = tk.Button(self, text="Change Text", command=self.change)
        self.my_button.pack(pady=20)
        
        # Create a frame outside this function
        My_frame(self)
        
    def change(self):
        
        if self.status == True:
            self.my_label.config(text="Goodbye World!")
            self.status = False
        
        else:
            self.my_label.config(text="Hello World!")
            self.status = True

class My_frame(tk.Frame):
    
    def __init__(self, parent):

        # Héritage
        super().__init__(parent)
        
        # Put this sucker on the screen
        self.pack(pady=20)
        
        # Create a few buttons
        self.my_button1 = tk.Button(self, text="Change", command=parent.change)
        self.my_button2 = tk.Button(self, text="Change", command=parent.change)
        self.my_button3 = tk.Button(self, text="Change", command=parent.change)
        
        self.my_button1.grid(row=0, column=0, padx=10)
        self.my_button2.grid(row=0, column=1, padx=10)
        self.my_button3.grid(row=0, column=2, padx=10)
        

if __name__ == '__main__':
    
    # Intanciation de la classe App et lancement de l'application
    app =  App()
    app.mainloop()
