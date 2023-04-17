import customtkinter as ctk
import locale

class Gui:
    
    def __init__(self, root):
        
        self.root = root
        root.geometry('500x250')
        
        self.widgets()
        
    def widgets(self):
        
        # create tabs
        tabview = ctk.CTkTabview(root)
        tabview.pack()
        
        tabview.add('Onglet1')
        tabview.add('Onglet2')
        tabview.add('Onglet3')

if __name__ == '__main__':
    
    # La librairie "locale" n'est pas compatible avec la librairie customtkinter...
    locale.setlocale(locale.LC_ALL, 'fr_FR' )
    root = ctk.CTk()
    gui = Gui(root)
    root.mainloop()
