"""
Tkinter - Codemy.com #169 : Build A Wikipedia Search App - Python Tkinter GUI Tutorial #169
Lien : https://www.youtube.com/watch?v=iBiAmmqIcyk

Dans ce programme on a recours au module 'wikipedia' afin d'afficher la définition sur Wikipedia d'un mot recherché

package installé : wikipedia
lien API wikipedia : https://pypi.org/project/wikipedia/

Éditeur : Laurent REYNAUD
Date : 11-03-21
"""

import tkinter
import wikipedia as wiki  # un module Wikipedia !!!

root = tkinter.Tk()
root.title('Wikipedia')
root.geometry('700x675')

wiki.set_lang('fr')  # accès aux données Wikipedia en français


def clear():
    """Fonction pour effacer la saisie faite dans le champ de recherche et dans la zone de texte"""

    my_entry.delete(0, 'end')  # champ de recherche effacé
    my_text.delete(0.0, 'end')  # zone de texte effacé


def search():
    """Fonction pour rechercher la définition sur Wikipedia d'un mot souhaité"""

    data = wiki.page(my_entry.get())  # récupération du mot saisi dans le champ de recherche
    # data = wiki.summary(my_entry.get(), sentences=10)  # résumé du mot recherché sur 10 lignes
    clear()  # appel de la fonction clear pour effacer les saisies dans les champs de recherche et de zone de texe
    my_text.insert(0.0, data.content)  # affichage dans la zone de texte de la définition du mot recherché
    # my_text.insert(0.0, data)  # affichage dans la zone de texte du résumé du mot recherché
    # my_text.insert(0.0, data.title)  # affichage dans la zone de texte du titre uniquement du mot recherché


"""Champ de recherche et cadre pour le titre"""

my_label_frame = tkinter.LabelFrame(root, text='Rechercher sur Wikipedia')  # cadre pour le champ de recherche
my_label_frame.pack(pady=20)

my_entry = tkinter.Entry(my_label_frame, font='Helvetica 18', width=47, justify='center')  # champ de recherche
my_entry.pack(pady=20, padx=20)

"""Zone de texte, barres de défilements et cadre pour le texe"""

my_frame = tkinter.Frame(root)  # cadre pour la zone de texte et les barres de défilement
my_frame.pack(pady=5)

text_scroll = tkinter.Scrollbar(my_frame)  # barre de défilement verticale
text_scroll.pack(side='right', fill='y')

hor_scroll = tkinter.Scrollbar(my_frame, orient='horizontal')  # barre de défilement horizontale
hor_scroll.pack(side='bottom', fill='x')

my_text = tkinter.Text(my_frame, yscrollcommand=text_scroll.set, wrap='none',
                       xscrollcommand=hor_scroll.set)  # zone de texte
my_text.pack()

text_scroll.config(command=my_text.yview)  # configuration barre de défilement verticale
hor_scroll.config(command=my_text.xview)  # configuration barre de défilement horizontale

"""Boutons et cadre pour les boutons"""

button_frame = tkinter.Frame(root)  # cadre pour les boutons
button_frame.pack(pady=10)

search_button = tkinter.Button(button_frame, text='Chercher', font='Helvetica 32', fg='#3a3a3a',
                               command=search)  # bouton pour chercher
search_button.grid(row=0, column=0, padx=20)

clear_button = tkinter.Button(button_frame, text='Effacer', font='Helvetica 32', fg='#3a3a3a',
                               command=clear)  # bouton pour effacer
clear_button.grid(row=0, column=1, padx=20)

root.mainloop()
