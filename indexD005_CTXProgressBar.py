"""
Titre : Progress Bars in CustomTkinter - Tkinter CustomTkinter 6
Lien : https://www.youtube.com/watch?v=HUdPRoGlNwc



Date : 19-09-2023
"""

import tkinter as tk
import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Progress Bar!")
        root.geometry('750x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_progressbar = ctk.CTkProgressBar(
            root, 
            width=300,
            height=50,
            corner_radius=100,
            border_width=2,
            border_color='red',
            fg_color='green',
            progress_color='pink',
            orientation='horizontal', # remise à zéro
            mode='indeterminate', # aller - retour
            # mode='determinate', # up and down !
            determinate_speed=.5, # avancement par 1 unité
            indeterminate_speed=1, # vitesse d'avancement
            )
        self.my_progressbar.set(0) # indicateur par défaut
        self.my_progressbar.pack(pady=40)
        
        my_button = ctk.CTkButton(
            root, text="Click Me!", command=self.clicker)
        my_button.pack(pady=10)
        
        start_button = ctk.CTkButton(
            root, text='Start', command=self.start)
        start_button.pack(pady=10)
        
        stop_button = ctk.CTkButton(
            root, text='Stop', command=self.stop)
        stop_button.pack(pady=10)
        
        self.my_label = ctk.CTkLabel(root, text='',  font=('Helvetica', 18))
        self.my_label.pack(pady=10)
        
    def clicker(self):
        
        # Avancememnt de la barre de progression
        self.my_progressbar.step() 
        
        # Affichage du niveau d'avancement de la barre de progression
        self.my_label.configure(text=int(self.my_progressbar.get()*100))
        
    def start(self):
        
        self.my_progressbar.start()
    
    def stop(self):
        
        self.my_progressbar.stop()

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    