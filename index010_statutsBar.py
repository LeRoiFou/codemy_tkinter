"""
Tkinter - Codemy.com #10 : Adding A Status Bar
Lien : https://www.youtube.com/watch?v=MGu7zKi5azQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=10

En complément du précédent programme, cette fois-ci on ajoute une barre de self.statuts en bas de fenêtre en affichant le n°
de page sur un total de pages

Éditeur : Laurent REYNAUD
Date : 03-11-2020
"""

import tkinter
from PIL import ImageTk, Image  # Module pour importer des images dans tkinter : package à télécharger -> Pillow


class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title('Apprendre à coder avec Codemy.com')
        self.widgets()

    def widgets(self):

        my_image = ImageTk.PhotoImage(Image.open('pic/pic1.png'))
        my_image2 = ImageTk.PhotoImage(Image.open('pic/pic2.png'))
        my_image3 = ImageTk.PhotoImage(Image.open('pic/pic3.png'))
        my_image4 = ImageTk.PhotoImage(Image.open('pic/pic4.png'))
        self.images_list = [my_image, my_image2, my_image3, my_image4]

        self.statuts = tkinter.Label(root, text='Image 1 sur ' + str(len(self.images_list)), bd=1, relief="sunken", anchor='e')

        self.my_label = tkinter.Label(image=my_image)
        self.my_label.grid(row=0, column=0, columnspan=3)

        self.button_back = tkinter.Button(root, text='<<', command=self.back, state="disabled")
        button_exit = tkinter.Button(root, text='Sortie', command=quit)
        self.button_forward = tkinter.Button(root, text='>>', command=lambda: self.forward(2))

        self.button_back.grid(row=1, column=0)
        button_exit.grid(row=1, column=1)
        self.button_forward.grid(row=1, column=2, pady=10)
        self.statuts.grid(row=2, column=0, columnspan=3, sticky='w' and 'e')

    def forward(self, image_number):

        self.my_label.grid_forget()
        self.my_label = tkinter.Label(image=self.images_list[image_number - 1])
        self.button_forward = tkinter.Button(root, text='>>', command=lambda: self.forward(image_number + 1))
        self.button_back = tkinter.Button(root, text='<<', command=lambda: self.back(image_number - 1))

        if image_number == 4:
            self.button_forward = tkinter.Button(root, text='>>', state="disabled")

        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_forward.grid(row=1, column=2)
        self.button_back.grid(row=1, column=0)

        self.statuts = tkinter.Label(root, text='Image ' + str(image_number) + ' sur ' + str(len(self.images_list)), bd=1, 
            relief="sunken", anchor='e')
        self.statuts.grid(row=2, column=0, columnspan=3, sticky='w' and 'e') 


    def back(self, image_number):

        self.my_label.grid_forget()
        self.my_label = tkinter.Label(image=self.images_list[image_number - 1])
        self.button_forward = tkinter.Button(root, text='>>', command=lambda: self.forward(image_number + 1))
        self.button_back = tkinter.Button(root, text='<<', command=lambda: self.back(image_number - 1))

        if image_number == 1:
            self.button_back = tkinter.Button(root, text='<<', state="disabled")

        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_forward.grid(row=1, column=2)
        self.button_back.grid(row=1, column=0)

        self.statuts = tkinter.Label(root, text='Image ' + str(image_number) + ' sur ' + str(len(self.images_list)), bd=1, 
            relief="sunken", anchor='e')
        self.statuts.grid(row=2, column=0, columnspan=3, sticky='w' and 'e')


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()