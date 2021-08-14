"""
Tkinter - Codemy.com #186 : Timed Background Images
Lien : https://www.youtube.com/watch?v=UV6rHVw-GwA

Dans ce programme on apprend à défiler des images de fond d'écran
(voir également index147 pour l'affichage d'image de fond d'écran)

Éditeur : Laurent REYNAUD
Date : 14-08-21
"""

import tkinter as tk


class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Défilment des images')
        root.geometry('290x174')
        
        self.widgets()
        self.next()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Récupération des photos
        self.our_images = [
            tk.PhotoImage(file='pic/pic1.png'),
            tk.PhotoImage(file='pic/pic2.png'),
            tk.PhotoImage(file='pic/pic3.png')
        ]
        
        # Canvas
        self.my_canvas = tk.Canvas(
            root, 
            width=290, 
            height=174, 
            highlightthickness=0 # Suppression bordure blanche
            )
        self.my_canvas.pack(fill='both', expand=True)
        
        # Ajout des images
        self.my_canvas.create_image(
            0, 
            0, 
            image=self.our_images[0], anchor='nw')
        
        # Compteur pour la méthode ci-après
        self.count = -1       
        
    def next(self):
        "Compteur pour changement d'image"
           
        if self.count == 2:
            self.my_canvas.create_image(
            0, 
            0, 
            image=self.our_images[0], anchor='nw')
            self.count = 0
        else: 
            self.my_canvas.create_image(
            0, 
            0, 
            image=self.our_images[self.count+1], anchor='nw')
            self.count += 1
        
        root.after(1_000, self.next)


if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
