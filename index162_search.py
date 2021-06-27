"""
Tkinter - Codemy.com #162 : 
Basic Search and Autofill - Python Tkinter GUI Tutorial #162
Lien : https://www.youtube.com/watch?v=0CXQ3bbBLVk

Dans ce programme lorsqu'on saisit dans le champ Entry, 
dans la zone de liste s'affiche les mots avec les premiers
caractères saisis

Éditeur : Laurent REYNAUD
Date : 14-01-21
"""

import tkinter

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('500x300')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Configuration du titre"""
        my_label = tkinter.Label(
            root, 
            text='Commencer à écrire', 
            font='Helvetica 14', 
            fg='grey')
        my_label.pack(pady=20)

        """Configuration du champ de saisie"""
        self.my_entry = tkinter.Entry(
            root, 
            font='Helvetica 20', 
            justify='center')
        self.my_entry.pack()

        """Configuration de la zone de liste"""
        self.my_list = tkinter.Listbox(root, width=50)
        self.my_list.pack(pady=40)

        """Assignation d'une liste de pizzas"""
        self.toppings = [
            'Pepperoni', 
            'Poivrons', 
            'Champignons', 
            'Fromage', 
            'Oignons', 
            'Jambon', 
            'Oeuf']

        """Appel de la fonction update() déterminée ci-dessus"""
        self.update(self.toppings)

        """Lien entre la zone de liste et le champ de saisi"""
        self.my_list.bind('<<ListboxSelect>>', self.fillout)

        """Lien entre le champ de saisi et la zone de liste"""
        self.my_entry.bind('<KeyRelease>', self.check)
        
    def update(self, data):
        """Méthode permettant d'ajouter la liste des pizzas
        dans la zone de liste"""

        """Réinitialisation de la zone de liste"""
        self.my_list.delete(0, 'end')

        """Ajout des données de la liste"""
        for item in data:
            self.my_list.insert('end', item)

    def fillout(self, e):
        """Cette méthode a pour but d'afficher dans la zone de saisie,
        la pizza sélectionnée dans la zone de liste"""

        """Réinitialisation du champ de saisie"""
        self.my_entry.delete(0, 'end')

        """Insertion dans le champ de saisi, la pizza sélectionnée
        dans la zone de liste"""
        self.my_entry.insert(0, self.my_list.get('active'))

    def check(self, e):
        """Cette méthode permet d'afficher dans la zone de liste,
        les pizzas à partir des premiers caractères saisis"""

        """Assignation du texte saisi dans le champ entry"""
        typed = self.my_entry.get()

        if typed == '':  # si rien n'est saisi
            """Les données de la zone de liste sont inchangées"""
            data = self.toppings

        else:  # sinon...
            """Initialisation d'une liste vide"""
            data = []
            """Pour chaque caractère de la liste de pizza"""
            for item in self.toppings:
                """Si le caractère saisi est un caractère
                de la liste de pizza"""
                if typed.lower() in item.lower():
                    """Ajout du caractère dans la liste 'data'"""
                    data.append(item)

        """Appel de la fonction update()"""
        self.update(data)


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
