"""
Tkinter - Codemy.com #143 : 
How To Read A PDF File With Tkinter - Python Tkinter GUI Tutorial #143
Lien : https://www.youtube.com/watch?v=JKnFT-OEflA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=143

Dans ce programme on apprend à ouvrir un fichier en pdf... 
en recourant au package PyPDF2

Pour avoir plus d'information, voir la documentation : 
https://pythonhosted.org/PyPDF2/

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter
from tkinter import filedialog
import PyPDF2

class Gui:
    
    def __init__(self, root):
        'Constructeur de la classe'
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x500')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Textbox"""
        self.my_text = tkinter.Text(root, height=30, width=60)
        self.my_text.pack(pady=10)

        """Menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Menu fichier"""
        file_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Fichier', menu=file_menu)
        file_menu.add_command(label='Ouvrir', command=self.open_pdf)
        file_menu.add_command(label='Effacer', command=self.clear_pdf)
        file_menu.add_separator()
        file_menu.add_command(label='Sortir', command=root.quit)
        
    def open_pdf(self):
        """Méthode permettant d'ouvrir un fichier pdf"""

        """Chemin pour ouvrir un fichier pdf"""
        open_file = filedialog.askopenfilename(
            initialdir='C:/Users/LRCOM/PycharmProjects/tests/pieces',
            title='Ouvrir un fichier PDF',
            filetypes=(('Fichier PDF', '*.pdf'), ('Tous fichiers', '*.*')))

        """Vérification s'il y a un fichier"""
        if open_file:
            
            """Ouvrir le fichier pdf"""
            pdf_file = PyPDF2.PdfFileReader(open_file)
            
            """Page du pdf à lire"""
            page = pdf_file.getPage(0)
            
            """Extraction du texte depuis le pdf"""
            page_stuff = page.extractText()
            
            """Ajouter le texte au widget testbox"""
            self.my_text.insert(1.0, page_stuff)

    def clear_pdf(self):
        """Méthode permettant de réinitialiser le widget text box"""
        
        self.my_text.delete(1.0, 'end')

        
if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
