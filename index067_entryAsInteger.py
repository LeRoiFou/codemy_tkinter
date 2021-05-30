"""
Tkinter - Codemy.com #67 : How to Validate an Entry Widget as an Integer
Lien : https://www.youtube.com/watch?v=IbpInH4q4Sg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=67

Programme permettant de convertir une chaîne de caractères en un entier à partir du champ de saisie

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

import tkinter

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('400x400')
        self.widgets()

    def widgets(self):

        # Configuration étiquette titre"""
        my_label = tkinter.Label(root, text='Entrez un chiffre')
        my_label.pack(pady=20)

        # Configuration champ de saisie"""
        self.my_box = tkinter.Entry(root, justify='center')
        self.my_box.pack(pady=10)

        # Configuration bouton à actionner"""
        my_button = tkinter.Button(root, text='Entre un chiffre', command=self.number)
        my_button.pack(pady=5)

        # Configuration étiquette résultat"""
        self.answer = tkinter.Label(root, text='')
        self.answer.pack(pady=20)

    def number(self):
        # méthode permettant de valider ou non si la saisie dans l'entry est un entier ou non
        try:
            int(self.my_box.get())
            self.answer.config(text="C'est un chiffre ! Félicitations !")

        except ValueError:
            self.answer.config(text="Ce n'est pas un chiffre ! hoooooooooouuuuuuuu !!!!!!")


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
