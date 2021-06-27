"""
Tkinter - Codemy.com #169 : 
Build A Wikipedia Search App - Python Tkinter GUI Tutorial #169
Lien : https://www.youtube.com/watch?v=iBiAmmqIcyk

Dans ce programme on a recours au module 'wikipedia' afin d'afficher
la définition sur Wikipedia d'un mot recherché

package installé : wikipedia
lien API wikipedia : https://pypi.org/project/wikipedia/

Éditeur : Laurent REYNAUD
Date : 11-03-21
"""

import tkinter
import wikipedia as wiki  # un module Wikipedia !!!

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Wikipedia')
        root.geometry('700x675')
        
        # accès aux données Wikipedia en français
        wiki.set_lang('fr')  
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Champ de recherche et cadre pour le titre"""
         # cadre pour le champ de recherche
        my_label_frame = tkinter.LabelFrame(
            root, 
            text='Rechercher sur Wikipedia') 
        my_label_frame.pack(pady=20)

        # champ de recherche
        self.my_entry = tkinter.Entry(
            my_label_frame, 
            font='Helvetica 18', 
            width=47, 
            justify='center') 
        self.my_entry.pack(pady=20, padx=20)

        """Zone de texte, barres de défilements et cadre pour le texe"""

        # cadre pour la zone de texte et les barres de défilement
        my_frame = tkinter.Frame(root)  
        my_frame.pack(pady=5)

        # barre de défilement verticale
        text_scroll = tkinter.Scrollbar(my_frame)  
        text_scroll.pack(side='right', fill='y')

        # barre de défilement horizontale
        hor_scroll = tkinter.Scrollbar(my_frame, orient='horizontal')  
        hor_scroll.pack(side='bottom', fill='x')

        # zone de texte
        self.my_text = tkinter.Text(
            my_frame, 
            yscrollcommand=text_scroll.set, 
            wrap='none',
            xscrollcommand=hor_scroll.set)  
        self.my_text.pack()

        # configuration barre de défilement verticale
        text_scroll.config(command=self.my_text.yview)  
        
        # configuration barre de défilement horizontale
        hor_scroll.config(command=self.my_text.xview)  

        """Boutons et cadre pour les boutons"""

        # cadre pour les boutons
        button_frame = tkinter.Frame(root)  
        button_frame.pack(pady=10)

        # bouton pour chercher
        search_button = tkinter.Button(
            button_frame, 
            text='Chercher', 
            font='Helvetica 32', 
            fg='#3a3a3a',
            command=self.search)  
        search_button.grid(row=0, column=0, padx=20)

        # bouton pour effacer
        clear_button = tkinter.Button(
            button_frame, 
            text='Effacer', 
            font='Helvetica 32', 
            fg='#3a3a3a',
            command=self.clear)  
        clear_button.grid(row=0, column=1, padx=20)
        
    def clear(self):
        """Fonction pour effacer la saisie faite dans le champ
        de recherche et dans la zone de texte"""

        self.my_entry.delete(0, 'end')  # champ de recherche effacé
        self.my_text.delete(0.0, 'end')  # zone de texte effacé

    def search(self):
        """Fonction pour rechercher la définition sur Wikipedia 
        d'un mot souhaité"""

        # récupération du mot saisi dans le champ de recherche
        data = wiki.page(self.my_entry.get())  
        # data = wiki.summary(self.my_entry.get(), sentences=10)  
        # # résumé du mot recherché sur 10 lignes
        
        # appel de la fonction clear pour effacer les saisies 
        # dans les champs de recherche et de zone de texte
        self.clear()  
        
        # affichage dans la zone de texte de la définition du mot recherché
        self.my_text.insert(0.0, data.content)  
        
        # affichage dans la zone de texte du résumé du mot recherché
        # self.my_text.insert(0.0, data)  
        
        # affichage dans la zone de texte du titre uniquement du mot recherché
        # self.my_text.insert(0.0, data.title)  


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
