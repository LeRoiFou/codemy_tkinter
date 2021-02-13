"""
Tkinter - Codemy.com #10 : Adding A Status Bar
Lien : https://www.youtube.com/watch?v=MGu7zKi5azQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=10

En complément du précédent programme, cette fois-ci on ajoute une barre de statuts en bas de fenêtre en affichant le n°
de page sur un total de pages

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

from tkinter import *
from PIL import ImageTk, Image  # Module pour importer des images dans tkinter : package à télécharger -> Pillow

root = Tk()
root.title('Apprendre à coder avec Codemy.com')

my_image = ImageTk.PhotoImage(Image.open('pic/pic1.png'))
my_image2 = ImageTk.PhotoImage(Image.open('pic/pic2.png'))
my_image3 = ImageTk.PhotoImage(Image.open('pic/pic3.png'))
my_image4 = ImageTk.PhotoImage(Image.open('pic/pic4.png'))
images_list = [my_image, my_image2, my_image3, my_image4]

statuts = Label(root, text='Image 1 sur ' + str(len(images_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_image)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global statuts

    my_label.grid_forget()
    my_label = Label(image=images_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 4:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    statuts = Label(root, text='Image ' + str(image_number) + ' sur ' + str(len(images_list)), bd=1, relief=SUNKEN,
                    anchor=E)
    statuts.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    global statuts

    my_label.grid_forget()
    my_label = Label(image=images_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    statuts = Label(root, text='Image ' + str(image_number) + ' sur ' + str(len(images_list)), bd=1, relief=SUNKEN,
                    anchor=E)
    statuts.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Sortie', command=quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
statuts.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
