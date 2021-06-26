"""
Tkinter - Codemy.com #150 : 
How To Ring The System Bell - Python Tkinter GUI Tutorial #150
Lien : https://www.youtube.com/watch?v=jBhDWcQRyu4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=150

Dans ce programme on apprend à faire sonner le son d'une cloche 
lorsqu'on appuye sur le bouton d'exécution

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Définition de l'image"""
        self.bell = tkinter.PhotoImage(file='images/bell.png')

        """Ajout de l'image à la fenêtre"""
        bell_label = tkinter.Label(root, image=self.bell)
        bell_label.pack(pady=20)

        """Ajout d'un bouton"""
        my_button = tkinter.Button(
            root, 
            text='Sonner la cloche !', 
            command=self.ring, 
            font='Helvetica 24', 
            fg='#4d4d4d')
        my_button.pack(pady=20)
        
    def ring(self):
        """Méthode permettant de faire sonner une cloche 
        en appuyant sur le bouton d'exécution"""
        
        root.bell()
        

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
