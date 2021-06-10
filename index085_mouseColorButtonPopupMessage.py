"""
Tkinter - Codemy.com #85 : Button Mouse On-Hover Popup Message
Lien : https://www.youtube.com/watch?v=o_YumT2iWBc&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=85

Dans ce programme, qu'on la souris survole le bouton, celui-ci change 
de couleur et un message (explicatif du bouton) apparaît en bas à droite de la fenêtre

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('500x400')
        self.widgets()
        
    def widgets(self):
        
        """Configuration du bouton d'exécution"""
        self.my_button = tkinter.Button(root, 
                                        text='Survole moi !', 
                                        font='Helvetica 28')
        self.my_button.pack(pady=50)

        """Configuration du renvoi de texte situé en bas à droite de la fenêtre"""
        self.status_label = tkinter.Label(root, 
                                          text='', 
                                          bd=1, 
                                          relief='sunken', 
                                          anchor='e')
        self.status_label.pack(fill='x', side='bottom', ipady=2)

        """Lien avec la souris et tkinter"""
        # souris survolant le bouton
        self.my_button.bind('<Enter>', self.button_hover)  
        # souris ne survolant plus le bouton
        self.my_button.bind('<Leave>', self.button_hover_leave)  
        
    def button_hover(self, event):
        """Méthode s'exécutant lorsque la souris survole 
        le bouton d'exécution"""
        
        # le bouton change de couleur
        self.my_button['bg'] = 'white'  
        # un message popup s'affiche en bas à droite
        self.status_label.config(text='Je suis en train de survoler le bouton !')  

    def button_hover_leave(self, event):
        """Méthode permettant de réinitialiser la couleur du bouton 
        ainsi que la suppression du message popup"""
        
        # réinitialisation de la couleur du bouton
        self.my_button['bg'] = 'SystemButtonFace'  
        # suppression du message popup
        self.status_label.config(text='')  
        

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
