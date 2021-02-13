"""
Tkinter - Codemy.com #75 : Tkinter Mouse On Hover Image Animation
Lien : https://www.youtube.com/watch?v=-NSQR3VRiq4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=75

Dans ce programme, à chaque fois que la souris va sur le cadre photo ou quitte le cadre photo, l'image change.
Le cadre photo est un bouton que l'on peut cliquer dessus et à ce moment là un message apparaît.

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

from tkinter import *

root = Tk()
root.title('Mon titre !')
root.geometry('500x300')


def change(event):
    """Fonction permettant de changer l'image lorsque la souris va sur le cadre photo. Les instructions ci-dessous sont
    identiques à celles du chargement d'une photo et l'affichage de cette photo en tant qu'étiquette décrites
    ci-après, exceptées que l'image est sous la forme d'un bouton"""
    my_pic = PhotoImage(file='pic/pic2.png')
    my_label.config(image=my_pic)
    my_label.image = my_pic


def change_back(event):
    """Fonction permettant de changer l'image lorsque la souris quitte le cadre photo. Les instructions ci-dessous sont
    identiques à celles du chargement d'une photo et l'affichage de cette photo en tant qu'étiquette décrites
    ci-après, exceptées que l'image est sous la forme d'un bouton"""
    my_pic = PhotoImage(file='pic/pic1.png')
    my_label.config(image=my_pic)
    my_label.image = my_pic


def do_something():
    my_label2 = Label(root, text='Tu as cliqué sur le bouton !')
    my_label2.pack()


"""Chargement d'une photo et affichage en tant que bouton"""
my_pic = PhotoImage(file='pic/pic1.png')  # pic = photo
my_label = Button(root, image=my_pic, command=do_something)
my_label.pack(pady=20)

"""Relations entre tkinter et la souris"""
my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)

root.mainloop()
