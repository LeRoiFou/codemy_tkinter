"""
Tkinter - Codemy.com #62 : Add Scrollbars to List Boxes  - 08 minutes 20 secondes
Lien : https://www.youtube.com/watch?v=8ijKnxkaoHE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=62

Création d'une barre de défilement à la verticale située à droite de la zone de liste

Éditeur : Laurent REYNAUD
Date : 03-12-20
"""

import tkinter

class GUI:

    def __init__(self, root):
        self.root =root
        root.title('Mon titre !')
        root.geometry('400x500')
        self.widgets_listbox()
        self.widgets_buttons()

    def widgets_listbox(self):
        
        # Création d'un cadre"""
        my_frame = tkinter.Frame(root)

        # Création de la barre de défilement"""
        my_scrollbar = tkinter.Scrollbar(my_frame, orient='vertical')

        """Configuration de la zone de liste : avec l'instruction selectmode on peut : 
        -> sélectionner plusieurs données avec MULTIPLE 
        -> étendre la sélection avec EXTENDED 
        """

        # connection zone de liste & barre de défil.
        self.my_listbox = tkinter.Listbox(my_frame, width=50, yscrollcommand=my_scrollbar.set,
                             selectmode='multiple') 

        # Configuration de la barre de défilement

         # défilement de haut en bas de la zone de liste
        my_scrollbar.config(command=self.my_listbox.yview)

        # barre de défilement à droite sur toute la largeur de la zone de liste
        my_scrollbar.pack(side='right', fill='y')  
        my_frame.pack()

        """Placement de la zone de liste qui s'effectue après le placement de la barre
        de défilement. À l'inverse la barre de défilement se trouve en-dessous 
        de la zone de liste"""
        self.my_listbox.pack(pady=15)

        """connection zone de liste & barre de défil.Insertion dans la zone de 
        liste d'un message"""
        self.my_listbox.insert('end', '1er message')
        self.my_listbox.insert('end', '2nd message')

        """connection zone de liste & barre de défil.Liste de messages à insérer dans 
        la zone de liste en première position"""
        my_list = ['Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois', 
        'Un', 'Deux', 'Trois', 'Un', 'Deux','Trois', 'Un', 'Deux', 'Trois', 'Un', 'Deux', 'Trois']

        for item in my_list:
            # 1ère position de la liste mais affichage inversée des données de la liste
            self.my_listbox.insert(0, item)  

        # Nouvelle entrée positionnée en 3ème ligne

        # cette donnée va être placée en 3ème position
        self.my_listbox.insert(2, 'Une nouvelle entrée')

    def widgets_buttons(self):
        
        my_button = tkinter.Button(root, text='Supprimer', command=self.delete)
        my_button.pack(pady=10)

        my_button2 = tkinter.Button(root, text='Sélectionner', command=self.select)
        my_button2.pack(pady=10)

        # étiquette configurée dans la fonction select() et la fonction select_all()
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=5)

        my_button3 = tkinter.Button(root, text='Tout supprimer', command=self.delete_all)
        my_button3.pack(pady=10)

        my_button4 = tkinter.Button(root, text='Tout sélectionner', command=self.select_all)
        my_button4.pack(pady=10)

        my_button5 = tkinter.Button(root, text='Suppression multiple', command=self.delete_multiple)
        my_button5.pack(pady=10)

    def delete(self):
        # Méthode permettant de supprimer une des données de la zone de liste

        # 'anchor' permet de sélectionner le texte mis en surlignage
        self.my_listbox.delete('anchor')  

    def select(self):
        # Méthode permettant d'afficher en étiquette la donnée sélectionnée dans la zone de liste

        # 'anchor' permet de sélectionner le texte mis en surlignage
        self.my_label.config(text=self.my_listbox.get('anchor'))  

    def delete_all(self):
        # Méthode supprimant TOUTES les données de la zone de liste

        # 0, END supprime toutes les données à la différence de 'anchor'
        self.my_listbox.delete(0, 'end')

    def select_all(self):
        
        result = ''

        # pour chaque donnée de la liste sélectionnée...
        for item in self.my_listbox.curselection():
            # affichage de chaque donnée par ligne distincte
            result = result + str(self.my_listbox.get(item)) + '\n'  
        self.my_label.config(text=result)

    def delete_multiple(self):
        """la fonction reversed permet de prendre d'un seul coup toutes les données 
        sélectionnées. À défaut de cette instruction, les données à supprimer seront 
        effacées une par une à chaque fois qu'on appuye sur le bouton 'suppression multiple'"""
        
        # pour chaque donnée de la liste sélectionnée...
        for item in reversed(self.my_listbox.curselection()):  
            self.my_listbox.delete(item)

if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()



  








