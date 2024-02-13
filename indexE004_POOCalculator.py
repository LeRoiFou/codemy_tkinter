"""
Titre : Let's Build A Calculator - Object Oriented Tkinter 4
Lien : https://www.youtube.com/watch?v=okX83SSTL_s



Date : 13-02-24
"""

import tkinter as tk

class App(tk.Tk) :
    
    def __init__(self):
        
        # Héritage de la sous-librairie Tk de tkinter
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("Calculator!")
        self.geometry('500x850')

        # Create widgets
        self.my_entry = tk.Entry(self, width=25, font=('Helvetica', 24))
        self.my_entry.pack(pady=20)
        
        # Create a new frame to hold the button
        MyFrame(self)
    
    # Clear the entry box
    def clear(self):
        self.my_entry.delete(0, tk.END)
    
    # Flip numbers postive or negative
    def pos_neg(self):
        
        if self.my_entry.get():
        
            # Get whatever is in the entry box
            number = int(self.my_entry.get())
            
            # Delete entry box
            self.my_entry.delete(0, tk.END)
            
            # Flip the number sign -/+
            self.my_entry.insert(0, (-1)*number)
        
        
# Button Frame Class
class MyFrame(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Pack the frame
        self.pack()
        
        # Define the buttons
        self.button_1 = tk.Button(
            self, text="1", font=('Helvetica', 24))
        self.button_2 = tk.Button(
            self, text="2", font=('Helvetica', 24))
        self.button_3 = tk.Button(
            self, text="3", font=('Helvetica', 24))
        
        self.button_4 = tk.Button(
            self, text="4", font=('Helvetica', 24))
        self.button_5 = tk.Button(
            self, text="5", font=('Helvetica', 24))
        self.button_6 = tk.Button(
            self, text="6", font=('Helvetica', 24))
        
        self.button_7 = tk.Button(
            self, text="7", font=('Helvetica', 24))
        self.button_8 = tk.Button(
            self, text="8", font=('Helvetica', 24))
        self.button_9 = tk.Button(
            self, text="9", font=('Helvetica', 24))
        
        self.button_0 = tk.Button(
            self, text="0", font=('Helvetica', 24))
        self.button_negative = tk.Button(
            self, text="+/-", font=('Helvetica', 24), command=parent.pos_neg)
        self.button_equal = tk.Button(
            self, text="=", font=('Helvetica', 24))
        
        self.button_plus = tk.Button(
            self, text="+", font=('Helvetica', 24))
        self.button_minus = tk.Button(
            self, text="-", font=('Helvetica', 24))
        self.button_multiply = tk.Button(
            self, text="x", font=('Helvetica', 24))
        
        self.button_divide = tk.Button(
            self, text="/", font=('Helvetica', 24))
        self.button_clear = tk.Button(
            self, text="Clear", font=('Helvetica', 24), command=parent.clear)
        
        # Grid the buttons to the screen
        self.button_1.grid(row=0, column=0, ipadx=40, ipady=20, padx=(0, 10))
        self.button_2.grid(row=0, column=1, ipadx=40, ipady=20)
        self.button_3.grid(row=0, column=2, ipadx=40, ipady=20, padx=(10, 0))
        
        self.button_4.grid(row=1, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_5.grid(row=1, column=1, ipadx=40, ipady=20)
        self.button_6.grid(row=1, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)
        
        self.button_7.grid(row=2, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_8.grid(row=2, column=1, ipadx=40, ipady=20)
        self.button_9.grid(row=2, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)
        
        self.button_0.grid(row=3, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_negative.grid(row=3, column=1, ipadx=31, ipady=20)
        self.button_equal.grid(row=3, column=2, ipadx=40, ipady=20, padx=(10, 0), 
                               pady=10)
        
        self.button_plus.grid(row=4, column=0, ipadx=40, ipady=20, padx=(0, 10), 
                              pady=10)
        self.button_minus.grid(row=4, column=1, ipadx=40, ipady=20)
        self.button_multiply.grid(row=4, column=2, ipadx=40, ipady=20, padx=(10, 0), 
                                  pady=10)
        
        self.button_divide.grid(row=5, column=0, ipadx=42, ipady=20, padx=(0, 10), 
                                pady=10)
        self.button_clear.grid(row=5, column=1, columnspan=2, ipadx=84, ipady=20, 
                               padx=(10, 0), pady=10)

if __name__ == '__main__':
    
    # Intanciation de la classe App et lancement de l'application
    app =  App()
    app.mainloop()
