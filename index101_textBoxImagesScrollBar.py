"""
Tkinter - Codemy.com #101 : Add Images to Text Box Widgets
Lien : https://www.youtube.com/watch?v=bdKxTH7Y-38&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=101

Dans ce programme on apprend à ajouter une image dans le text box 
et à mettre une barre de défilement

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

import tkinter
from tkinter import filedialog

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x600')
        self.widgets()
        
    def widgets(self):
        
        """Création d'un cadre pour le textbox 
        et la barre de défilement"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=10)

        """Création d'une barre de défilement pour le texbox"""
        text_scroll = tkinter.Scrollbar(my_frame)
        text_scroll.pack(side='right', fill='y')

        """Configuration de la boîte à texte
        -> selectbackground : surbrillance en rouge du texte sélectionné
        -> selectforeground : écriture en noir du texte en surbrillance 
        de couleur rouge
        -> yscrollcommand=text_scroll.set :
        liaison avec la barre de défilement"""
        
        self.my_text = tkinter.Text(my_frame, 
                                    width=40, 
                                    height=10, 
                                    font='helvetica 16',
                                    selectbackground='red',  
                                    selectforeground='black',
                    yscrollcommand=text_scroll.set  
                    )
        self.my_text.pack(pady=20)

        """Configuration de la barre de défilement"""
        text_scroll.config(command=self.my_text.yview)

        """Configuration du bouton d'exécution 
        permettant d'ouvrir un fichier texte"""
        open_button = tkinter.Button(root, 
                                     text='Ouvrir un fichier texte', 
                                     command=self.open_text)
        open_button.pack(pady=20)

        """Configuration du bouton de sauvegarde 
        des données saisies dans le widget text box"""
        save_button = tkinter.Button(root, 
                                     text='Sauvegarder', 
                                     command=self.save_txt)
        save_button.pack(pady=20)

        """Configuration du bouton d'exécution 
        pour insérer une image dans le text box"""
        image_button = tkinter.Button(root, 
                                      text='Ajouter une image', 
                                      command=self.add_image)
        image_button.pack(pady=5)
        
    def open_text(self):
        """Méthode permettant de récupérer un fichier texte 
        et de l'afficher dans le widget textbox"""
        
        # voir tuto n° 15_DialogBox.py
        my_path = 'C:/Users/LRCOM/PycharmProjects/tests/pieces'
        text_file = filedialog.askopenfilename(initialdir=my_path,
                                            title='Ouvrir un fichier texte',
                                            filetypes=(('Fichiers .txt', 
                                                        '*.txt'),))  
        # ouverture du fichier, lecture du fichier
        text_file = open(text_file, 'r')  
        stuff = text_file.read()
        self.my_text.insert('end', stuff)
        text_file.close()

    def save_txt(self):
        """Méthode permettant de sauvegarder les modifications 
        faites dans le widget textbox dans le fichier ouvert"""
        
        my_path = 'C:/Users/LRCOM/PycharmProjects/tests/pieces'
        text_file = filedialog.askopenfilename(initialdir=my_path,
                                            title='Enregistrer sous',
                                            filetypes=(('Fichiers .txt', 
                                                        '*.txt'),))
        # ouverture du fichier, écriture du fichier
        text_file = open(text_file, 'w')  
        text_file.write(self.my_text.get(1.0, 'end'))

    def add_image(self):
        """Ajout d'une image dans le text box"""
        
        # chargement de l'image
        self.my_image = tkinter.PhotoImage(file='images/shrek.png')
        # insertion à la position du curseur de la souris  
        position = self.my_text.index('insert')  
        # insertion de l'image dans le widget textbox
        self.my_text.image_create(position, image=self.my_image)  


if __name__=="__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
