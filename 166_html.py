"""
Tkinter - Codemy.com #166 : How To Use HTML In Your Tkinter App - Python Tkinter GUI Tutorial #166
Lien : https://www.youtube.com/watch?v=d6UitRCstiQ

Packages installés : requests, Pillow, tkhtmlview
Dans ce programme on apprend à lier une interface graphique avec un fichier HTML

Éditeur : Laurent REYNAUD
Date : 11-02-2021
"""

from tkhtmlview import HTMLLabel  # module qui requiert les packages requests et Pillow pour les liens HTML

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('600x650')

"""Configuration d'une étiquette en HTML qui comprend : 
-> le lien @ du cours à partir d'une certaine séquence ; 
-> téléchargement de l'image du site codemy.com (clique droit puis copier l'adresse de l'image) ; 
-> une liste ordonnée 
"""
my_label = HTMLLabel(root,
                     html="<h1><pre><a href=https://youtu.be/d6UitRCstiQ?t=377>Coder avec HTML</a></pre></h1>"  # lien @
                          "<img src=https://cdn.codemy.com/wp-content/uploads/2015/01/sp21212.png>"  # image téléchargée
                          "<ol><li>Un</li><li>Deux</li><li>Trois</li><li>Houlala !!!</li></ol>"  # liste ordonnée
                     )
my_label.pack(pady=20, padx=20, fill="both", expand=True)

root.mainloop()
