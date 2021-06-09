"""
Tkinter - Codemy.com #72 : Create A Date Picker Calendar
Lien : https://www.youtube.com/watch?v=fqfy-3IoVvs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=72

Création d'un calendrier en recourant au package 'tkcalendar'

Éditeur : Laurent REYNAUD
Date : 10-12-20
"""

import tkinter
import tkcalendar

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('600x400')
        self.widgets()

    def widgets(self):

        """Configuration du calendrier version française"""
        cal = tkcalendar.Calendar(root, selectmode='day', year=2020, month=12, day=10, locale='Fr_fr')
        cal.pack(pady=20, fill='both', expand=1)

        """Configuration du bout 'Obtenir une date'"""
        my_button = tkinter.Button(root, text='Obtenir une date', command=self.grab_date)
        my_button.pack(pady=20)

        """Configuration de l'étiquette 'résultat'"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)

    def grab_date(self):
        """Méthode permettant d'afficher la date sélectionnée à partir du bouton 'Obtenir une date'"""
    
        self.my_label.config(text=cal.get_date())


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
