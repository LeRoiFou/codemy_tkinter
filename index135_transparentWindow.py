"""
Tkinter - Codemy.com #135 : 
Transparent Windows With TKinter - Python Tkinter GUI Tutorial #135
Lien : https://www.youtube.com/watch?v=qDVxLMuNs7E&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=135

Dans ce programme on apprend à rendre transparent une fenêtre. 
On ne peut que rendre transparent la fenêtre principale
et non les widgets individuellement

Éditeur : Laurent REYNAUD
Date : 25-12-20
"""

import tkinter
import tkinter.ttk as ttk

class Gui:
    
    def __init__(self, root):
        'Constructeur'
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x550')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Etiquette titre"""
        my_label = tkinter.Label(root, text='Salut !', font='Helvetica 20')
        my_label.pack(pady=20)

        """Curseur pour le d° de transparence de la fenêtre"""
        self.my_slider = ttk.Scale(
            root, 
            from_=0.1,
            to=1.0, 
            value=0.7, 
            orient='horizontal', 
            command=self.slide)
        self.my_slider.pack(pady=20)

        """Etiquette d'affichage du degré de transparence"""
        self.slide_label = tkinter.Label(root, text='')
        self.slide_label.pack(pady=10)

        """Bouton pour ouvrir un nouvelle fenêtre"""
        new_window = tkinter.Button(
            root, 
            text='Nouvelle fenêtre', 
            command=self.new_window)
        new_window.pack(pady=20)
        
    def slide(self, *args):
        """Méthode permettant d'ajuster le d° de transparence 
        de la fenêtre principale"""
        
        root.attributes(
            '-alpha',
            self.my_slider.get())
        self.slide_label.config(text=round(self.my_slider.get(), 2))

    def make_solid(self, e):
        """Méthode permettant d'annuler la transparence de la 2ème fenêtre"""
        
        self.new.attributes('-alpha',
                    1.0  # absence de transparence
                    )

    def new_window(self):
        """Méthode permettant d'ouvrir une nouvelle fenêtre"""
        
        self.new = tkinter.Toplevel()
        self.new.attributes('-alpha',
                    0.5  # degré de transparence
                    )
        
        # lorsqu'on clique sur cette nouvelle fenêtre, 
        # celle-ci n'est plus transparente
        self.new.bind('<Button-1>', self.make_solid)  


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
