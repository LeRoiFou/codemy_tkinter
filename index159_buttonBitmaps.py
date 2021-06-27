"""
Tkinter - Codemy.com #159 : 
Button Bitmaps - Python Tkinter GUI Tutorial #159
Lien : https://www.youtube.com/watch?v=5oCBzMXIcPo

Dans ce programme on apprend à afficher des 'bitmaps' (images) 
sur les boutons qui sont issus du programme python.
Pour cela, on a recours à l'instruction 'bitmap' et 
il y a 9 types de bitmaps disponibles :
-> error
-> gray75
-> gray50
-> gray12
-> hourglass
-> info
-> questhead
-> question
-> warning

Ces images sont un peu 'rétro', il est plus appréciable de télécharger
des images à insérer sur les boutons...

Éditeur : Laurent REYNAUD
Date : 06-01-21
"""

import tkinter

root = tkinter.Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('300x900')

"""Assignation d'une liste des 9 bitmaps"""
my_list = [
    'error', 
    'gray75', 
    'gray50', 
    'gray12', 
    'hourglass', 
    'info', 
    'questhead', 
    'question', 
    'warning']

"""Boucle for pour afficher tous les types de bitmaps"""
for i in my_list:
    my_button = tkinter.Button(
        root, 
        bitmap=i, 
        width=50, 
        height=50, 
        fg='darkblue')
    my_button.pack(pady=10)

root.mainloop()
