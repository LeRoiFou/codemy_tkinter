"""
Tkinter - Codemy.com #126 : How To Center a Tkinter Window On The Screen - Python Tkinter GUI Tutorial #126
Lien : https://www.youtube.com/watch?v=TdTks2eSx3c&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=126

Dans ce programme on apprend à centrer une fenêtre à l'écran du portable : le programme ci-dessous est celui réalisé
avec FORMATION VIDEO - 20_Fenetre-2

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')

largeur_ecran = int(root.winfo_screenwidth())  # largeur de l'écran
hauteur_ecran = int(root.winfo_screenheight())  # hauteur de l'écran
largeur_fenetre = 800  # largeur de la fenêtre
hauteur_fenetre = 600  # hauteur de la fenêtre

posX = (largeur_ecran // 2) - (largeur_fenetre // 2)  # voir la formule ci-dessus dans DocStrings
posY = (hauteur_ecran // 2) - (hauteur_fenetre // 2)  # voir la formule ci-dessus dans DocStrings

centrage = f"{largeur_fenetre}x{hauteur_fenetre}+{posX}+{posY}"

root.geometry(centrage)

root.mainloop()
