"""
Tkinter - Codemy.com : Domain Name Lookup Tool - Tkinter Projects 8
Lien : https://www.youtube.com/watch?v=wlbg0DObECE

Module installé : pip install python-whois (nom du domaine)
https://pypi.org/project/python-whois/

Date : 20-10-22
"""

import tkinter as tk
import whois

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Domain Name!")
        root.geometry('500x550')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_frame = tk.LabelFrame(root, text="Lookup Domain Name")
        my_frame.pack(pady=20)
        
        self.my_entry = tk.Entry(my_frame, font='Helvetica 18')
        self.my_entry.grid(row=0, column=0, pady=10, padx=10)
        
        my_button = tk.Button(
            my_frame, text="Lookup Domain",command=self.lookup)
        my_button.grid(row=0, column=1, padx=10)
        
        self.my_text= tk.Text(root, width=50)
        self.my_text.pack()
        
    def lookup(self):
        
        # Delete text in box
        self.my_text.delete(1.0, 'end')
        
        # Get domain info
        domain = self.my_entry.get()
        domain_info = whois.whois(domain)
        
        # Loop the output (changement affichage sous la forme d'un dictionnaire)
        for key, value in domain_info.items():
            
            # Output to text box
            self.my_text.insert(1.0, f'{key} - {value}' + '\n\n')
    
if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
