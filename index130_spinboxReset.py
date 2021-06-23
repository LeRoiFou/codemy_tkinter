"""
Tkinter - Codemy.com #130 : 
How To Reset A Spinbox With Tkinter 
- Python Tkinter GUI Tutorial #130

Lien : https://www.youtube.com/watch?v=GjVZUIayxQg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=130

Dans ce programme on apprend à réinitialiser une valeur par défaut
du widget spinbox (champ de saisi avec à l'extrêmité une barre de défilement
-> voir tuto n° 98)

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Titre !')
        root.geometry('500x350')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Variable de contrôle permettant d'afficher une valeur par défaut
        du spinbox : ici la valeur par défaut est 20"""
        var = tkinter.IntVar(root)
        var.set(20)

        """Spinbox'"""
        self.my_spin = tkinter.Spinbox(
            root, 
            from_=0, 
            to=100, 
            justify='center', 
            font='Helvetica 20', 
            textvariable=var)
        self.my_spin.pack(pady=20)

        """Bouton"""
        my_button = tkinter.Button(
            root, 
            text='Réinitialiser les données', 
            command=self.reset)
        my_button.pack(pady=20)

        """Deuxième variable de contrôle mais cette fois-ci avec
        une str utilisée pour le 2ème spinbox"""
        var2 = tkinter.StringVar(root)
        var2.set('John')

        """Spinbox n° 2"""
        self.my_spin2 = tkinter.Spinbox(
            root, 
            values=('John', 'Albert', 'Erin', 'Dean', 'Walter'),
            justify='center', 
            font='Helvetica 20', 
            textvariable=var2)
        self.my_spin2.pack(pady=20)

        """Bouton n° 2"""
        my_button2 = tkinter.Button(
            root, 
            text='Réinitialiser les données', 
            command=self.reset2)
        my_button2.pack(pady=20)
        
    def reset(self):
        """Méthode permettant de réinitialiser la valeur 
        par défaut du widget spinbox"""
        
        var = tkinter.IntVar(root)
        var.set(0)
        self.my_spin.config(textvariable=var)

    def reset2(self):
        """Méthode permettant de réinitialiser la valeur 
        par défaut du widget spinbox"""
        
        var2 = tkinter.StringVar(root)
        var2.set('Erin')
        self.my_spin2.config(textvariable=var2)


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
