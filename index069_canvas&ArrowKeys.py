"""
Tkinter - Codemy.com #69 : Move Canvas Shapes With Arrow Keys
Lien : https://www.youtube.com/watch?v=xifcE6xvnyg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=69

Dans ce programme on déplace un cercle créé dans canvas soit avec les touches 'qsdz' soit avec les touches
directionnelles du clavier

Éditeur : Laurent REYNAUD
Date : 09-12-20
"""

import tkinter

class GUI:

    def __init__(self, root):
        self.root = root
        root.title('Mon titre !')
        root.geometry('800x600')
        self.widgets()

    def widgets(self):

        """Tailles et coordonnées en variables"""
        w = 600
        h = 400
        x = w // 2
        y = h // 2

        """Configuration d'un canvas sous fond blanc"""
        self.my_canvas = tkinter.Canvas(root, width=w, height=h, bg='white')
        self.my_canvas.pack(pady=20)

        """Configuration d'un cercle"""
        self.my_circle = self.my_canvas.create_oval(x, y, x + 10, y + 10)

        """Configuration des touches 'qsdz' du clavier pour déplacer le cercle"""
        root.bind("<Key>", self.pressing)

        """Configuration des touches directionnelles du clavier pour déplacer le cercle"""
        root.bind('<Left>', self.left)
        root.bind('<Right>', self.right)
        root.bind('<Up>', self.up)
        root.bind('<Down>', self.down)

    def left(self, event):
        
        """Déplacement de 10 pixels à la gauche"""
        x = -10
        y = 0
        self.my_canvas.move(self.my_circle, x, y)

    def right(self, event):
        
        """Déplacement de 10 pixels à la droite"""
        x = 10
        y = 0
        self.my_canvas.move(self.my_circle, x, y)

    def up(self, event):
        
        """Déplacement de 10 pixels en haut"""
        x = 0
        y = -10
        self.my_canvas.move(self.my_circle, x, y)

    def down(self, event):
        
        """Déplacement de 10 pixels en bas"""
        x = 0
        y = 10
        self.my_canvas.move(self.my_circle, x, y)

    def pressing(self, event):
       
        """Déplacement avec les touches 'qsdz'"""
        x = 0
        y = 0
        if event.char == 'q': x = -10  # déplacement à gauche
        if event.char == 's': y = 10  # déplacement en bas
        if event.char == 'd': x = 10  # déplacement à droite
        if event.char == 'z': y = -10  # déplacement en haut
        self.my_canvas.move(self.my_circle, x, y)


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = GUI(root)
    root.mainloop()
