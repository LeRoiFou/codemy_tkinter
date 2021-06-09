"""
Tkinter - Codemy.com #73 : Don't .pack On The Same Line!
Lien : https://www.youtube.com/watch?v=5_VNqv-uH6o&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=73

Dans ce programme, lorsque l'instruction .pack() est sur la même ligne que la configuration du widget, le programme peut
ne pas marcher : il est donc déconseiller de mettre sur la même ligne la configuration du wigket + l'emplacement
L'erreur qui apparaîtra sur l'instruction d'emplacement se trouve sur la même ligne que l'instruction de configuration
du widget est de type 'NoneType'

Éditeur : Laurent REYNAUD
Date : 10-12-20
"""

import tkinter

root = tkinter.Tk()
root.title('Mon titre !')
root.geometry('600x400')


def grab():
    my_label.config(text=my_box.get())


my_box = tkinter.Entry(root, font='Helvetica 28')
my_box.pack(pady=20)

my_button = tkinter.Button(root, text='Appuie', command=grab).pack(pady=20)

my_label = tkinter.Label(root, text='').pack(pady=20)

root.mainloop()
