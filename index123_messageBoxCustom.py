"""
Tkinter - Codemy.com #123 : 
Custom Message Box Popups - Python Tkinter GUI Tutorial #123
Lien : https://www.youtube.com/watch?v=tpwu5Zb64lQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=123

Dans ce programme on customise le widget messagebox qui ne peut être 
modifié lorsqu'on a recours à cette instruction
(widget information, danger, alerte...), 
il faut donc crééer un faux widget messagebox

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuraiton de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('300x300')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration du bouton d'exécution"""
        my_button = tkinter.Button(
            root, 
            text='Clique !', 
            command=self.clicker)
        my_button.pack(pady=50)

        """Etiquette"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)
        
    def clicker(self):
        """Affichage d'un message box customisé"""

        """Configuration de la nouvelle fenêtre"""
        self.pop = tkinter.Toplevel(root)
        self.pop.title('Affichage')
        self.pop.geometry('250x200')
        self.pop.iconbitmap('images/Logo.ico')
        self.pop.config(bg='green')

        """Configuration de l'image à insérer"""
        self.me = tkinter.PhotoImage(file='images/LogoBis50x67.png')

        """Message 'titre'"""
        pop_label = tkinter.Label(
            self.pop, 
            text='Voulez-vous appuyer ?', 
            bg='green', 
            fg='white', 
            font='Helvetica 12')
        pop_label.pack(pady=10)

        """Cadre"""
        my_frame = tkinter.Frame(self.pop, bg='green')
        my_frame.pack(pady=50)

        """Affichage de l'image"""
        me_pic = tkinter.Label(my_frame, image=self.me, borderwidth=0)
        me_pic.grid(row=0, column=0, padx=10)

        """Bouton OUI"""
        yes = tkinter.Button(
            my_frame, 
            text='OUI', 
            bg='orange', 
            command=lambda: self.choice('OUI'))
        yes.grid(row=0, column=1, padx=10)
        
        """Bouton NON"""
        no = tkinter.Button(
            my_frame, 
            text='NON', 
            bg='yellow', 
            command=lambda: self.choice('NON'))
        no.grid(row=0, column=2, padx=10)
        
    def choice(self, option):
        """Lorsqu'on clique sur le bouton OUI / NON 
        dans le faux widget messagebox, 
        une message s'affiche dans la fenêtre principale"""
        
        # fermeture de la fenêtre du faux widget messagebox
        self.pop.destroy()  
        
        if option == 'OUI':
            self.my_label.config(text="Tu as cliqué sur 'OUI'")
        
        else:
            self.my_label.config(text="Tu as cliqué sur 'NON'")
    

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
