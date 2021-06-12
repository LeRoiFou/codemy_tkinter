"""
Tkinter - Codemy.com #99 : Text Box Widgets in Tkinter
Lien : https://www.youtube.com/watch?v=Qrmab6lSzU4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=99

Le widget Text Box permet de saisir du texte sur plusieurs 
lignes à la différence du champ de saisi Entry

Éditeur : Laurent REYNAUD
Date : 17-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x450')
        self.widgets()
        
    def widgets(self):
        
        """Configuration de la boîte de texte"""
        self.my_text = tkinter.Text(root,
                            width=40,
                            height=10,
                            font='Helvetica 16')
        self.my_text.pack(pady=20)

        """Création d'un cadre pour les boutons détaillés ci-après"""
        button_frame = tkinter.Frame(root)
        button_frame.pack()

        """Création d'un bouton d'exécution permetttant d'effacer 
        le texte dans le widget text box"""
        clear_button = tkinter.Button(button_frame,
                                    text='Effacer le texte',
                                    command=self.clear)
        clear_button.grid(row=0, column=0)

        """Création d'un bouton d'exécution permettant de récupérer
        et d'afficher le texte saisi dans le widget text box"""
        get_text_buttuon = tkinter.Button(button_frame,
                                        text='Récup texte saisi', 
                                        command=self.get_text)
        get_text_buttuon.grid(row=0, column=1, padx=20)

        """Affichage du texte saisi dans le widget text box : 
        cette étiquette est configurée dans la fonction get_text()"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)
    
    def clear(self):
        """Méthode permettant d'effacer le texte dans le widget text box"""
        """Attention : au lieu de 0 dans la plupart des widgets, 
        c'est 1.0 pour le text box !"""
        
        self.my_text.delete(1.0, 'end')  

    def get_text(self):
        """Méthode permettant de récupérer le texte saisi 
        dans le widget text box et d'afficher le texte saisi"""
        
        # récupération de la 1ère ligne à la 4ème ligne
        self.my_label.config(text=self.my_text.get(1.0, 5.0))  
        

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
