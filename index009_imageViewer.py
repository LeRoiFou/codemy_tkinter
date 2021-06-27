"""
Tkinter - Codemy.com #9 : Build an Image Viewer App With Python and TKinter
Lien : https://www.youtube.com/watch?v=zg4c92pNFeo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=9

Dans ce programme on apprend à défiler les images

Éditeur : Laurent REYNAUD
Date : 01-11-2020
"""

import tkinter
from PIL import ImageTk, Image  


class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title('Apprendre à coder avec Codemy.com')
        self.widgets()

    def widgets(self):
        
        # téléchargement des images
        my_image = ImageTk.PhotoImage(Image.open('pic/pic1.png'))
        my_image2 = ImageTk.PhotoImage(Image.open('pic/pic2.png'))
        my_image3 = ImageTk.PhotoImage(Image.open('pic/pic3.png'))
        my_image4 = ImageTk.PhotoImage(Image.open('pic/pic4.png'))

        # assignation d'une variable sous forme d'une liste 
        # des images téléchargées
        self.images_list = [my_image, my_image2, my_image3, my_image4]

        # affichage des images sous la forme du widget Label
        self.my_label = tkinter.Label(image=my_image)
        self.my_label.grid(row=0, column=0, columnspan=3)

        # boutons d'exécution
        self.button_back = tkinter.Button(
            root, 
            text='<<', 
            command=self.back, 
            state='disabled')
        button_exit = tkinter.Button(
            root, 
            text='Sortie', 
            command=root.quit)
        self.button_forward = tkinter.Button(
            root, text='>>', 
            command=lambda: self.forward(2))

        # affichages des boutons
        self.button_back.grid(row=1, column=0)
        button_exit.grid(row=1, column=1)
        self.button_forward.grid(row=1, column=2)

    def forward(self, image_number):
        # fonction permettant d'afficher l'image suivante

        # réinitialisation des widgets
        self.my_label.grid_forget()
        self.my_label = tkinter.Label(
            image=self.images_list[image_number - 1])
        self.button_forward = tkinter.Button(
            root, 
            text='>>', 
            command=lambda: self.forward(image_number + 1))
        self.button_back = tkinter.Button(
            root, 
            text='<<', 
            command=lambda: self.back(image_number - 1))

        if image_number == 4:
            self.button_forward = tkinter.Button(
                root, 
                text='>>', 
                state='disabled')

        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_forward.grid(row=1, column=2)
        self.button_back.grid(row=1, column=0)

    def back(self, image_number):
        # fonction permettant d'afficher l'image précédente

        # réinitialisation des widgets
        self.my_label.grid_forget()
        self.my_label = tkinter.Label(
            image=self.images_list[image_number - 1])
        self.button_forward = tkinter.Button(
            root, 
            text='>>', 
            command=lambda: self.forward(image_number + 1))
        self.button_back = tkinter.Button(
            root, 
            text='<<', 
            command=lambda: self.back(image_number - 1))

        if image_number == 1:
            self.button_back = tkinter.Button(
                root, 
                text='<<', state='disabled')

        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_forward.grid(row=1, column=2)
        self.button_back.grid(row=1, column=0)


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()