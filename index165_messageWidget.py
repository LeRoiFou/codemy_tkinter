"""
Tkinter - Codemy.com #165 : 
How To Use The Message Widget For Blocks of Text 
- Python Tkinter GUI Tutorial #165
Lien : https://www.youtube.com/watch?v=frNj1E-MA14

Dans ce programme on apprend à utiliser le widget Message 
qui permet de faire de la saisie sur plusieurs lignes sans
recourir à l'instruction '\n' qu'on utilise avec le widget Label

Pour une seule ligne -> Label // Entry
Pour plusieurs lignes -> Message // Text

Éditeur : Laurent REYNAUD
Date : 03-02-21
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('400x900')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Premier cadre"""
        frame1 = tkinter.LabelFrame(
            root, 
            text='Justifié à droite')
        frame1.pack(pady=20)

        self.my_message1 = tkinter.Message(
            frame1, 
            text=("C'est un long texte parce que je veux regarder\
ce que j'écris, ce n'est pas cool ?"),
            font='helvetica 18',
            aspect=150,  # largeur du widget
            justify='right'  # alignement du texte
            )
        self.my_message1.pack(pady=10, padx=10)

        """Deuxième cadre"""
        frame2 = tkinter.LabelFrame(root, text='Justifié à gauche')
        frame2.pack(pady=20)

        my_message2 = tkinter.Message(
            frame2, 
            text=("C'est un long texte parce que je veux regarder\
ce que j'écris, ce n'est pas cool ?"),
            font='helvetica 18',
            aspect=100,  # largeur du widget
            justify='left'  # alignement du texte
            )
        my_message2.pack(pady=10, padx=10)

        """Troisième cadre"""
        frame3 = tkinter.LabelFrame(root, text='Centré')
        frame3.pack(pady=20)

        my_message3 = tkinter.Message(
            frame3, 
            text=("C'est un long texte parce que je veux regarder\
ce que j'écris, ce n'est pas cool ?"),
            font='helvetica 18',
            aspect=200,  # largeur du widget
            justify='center'  # alignement du texte
            )
        my_message3.pack(pady=10, padx=10)

        """Bouton"""
        my_button = tkinter.Button(
            root, 
            text='Changer le text', 
            command=self.change)
        my_button.pack(pady=20)
        
    def change(self):
        """Fonction permettant de changer le texte"""
        self.my_message1.config(
            text='Et maintenant le texte a été complètement modifié !',
            aspect=200  # changement de la largeur du widget
            )

        
if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
