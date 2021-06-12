"""
Tkinter - Codemy.com #100 : Read And Write To Text Files
Lien : https://www.youtube.com/watch?v=Z_0ISFfT_eM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=100

Dans ce programme on continue avec le widget text box mais cette fois-ci on apprend à récuper un texte issue d'un
fichier texte et de l'afficher dans le widget text box et pouvoir également rectifier le texte et l'enregistrer dans le
fichier d'origine

Ci-dessous les différentes instructions après avoir cibler le fichier à prendre en compte :
-> r : lire
-> r+ : lire et écrire
-> w : écrire
-> w+ : écrire et lire
-> a : ajouter
-> a+ : ajouter et lire

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
        root.geometry('500x450')
        self.widgets()
        
    def widgets(self):
        
        """Configuration de la boîte à texte"""
        self.my_text = tkinter.Text(root, 
                               width=40, 
                               height=10, 
                               font='helvetica 16')
        self.my_text.pack(pady=20)

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
        
    def open_text(self):
        """Méthode permettant de récupérer un fichier texte 
        et de l'afficher dans le widget textbox"""
        
        # voir tuto n° 15_DialogBox.py
        text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                            title='Ouvrir un fichier texte',
                                            filetypes=(('Fichiers .txt', '*.txt'),))  
        # ouverture du fichier, lecture du fichier
        text_file = open(text_file, 'r')  
        stuff = text_file.read()
        self.my_text.insert('end', stuff)
        text_file.close()

    def save_txt(self):
        """Méthode permettant de sauvegarder les modifications 
        faites dans le widget textbox dans le fichier ouvert"""
        
        # voir tuto n° 15_DialogBox.py
        text_file = filedialog.askopenfilename(initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
                                            title='Enregistrer sous',
                                            filetypes=(('Fichiers .txt', '*.txt'),))  
        # ouverture du fichier, écriture du fichier
        text_file = open(text_file, 'w')  
        text_file.write(self.my_text.get(1.0, 'end'))

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()










