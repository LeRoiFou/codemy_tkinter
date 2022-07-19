"""
Tkinter - Codemy.com #222 : Build a Quick Language Detection App
Lien : https://www.youtube.com/watch?v=Dhky5WuulRE

Détection du langage utilisé :)

Modules installés : langdetect, langcodes[data]

Éditeur : Laurent REYNAUD
Date : 19-07-22
"""

import tkinter as tk
from langdetect import detect
import langcodes as codes

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Quick language detection")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_text = tk.Text(root, height=10, width=50)
        self.my_text.pack(pady=20)
        
        my_button = tk.Button(root, text="Choisis un langage",
                              command=self.check_lang)
        my_button.pack(pady=20)
        
        self.my_label = tk.Label(root, text='')
        self.my_label.pack(pady=10)
        
    def check_lang(self):
        
        if self.my_text.compare("end-1c", "==", "1.0"):
            self.my_label.config(
                text="Hé ! Tu as oublié de saisir quelque chose :(")
        else:
            code = detect(self.my_text.get(1.0, 'end'))
            my_result = codes.Language.make(language=code).display_name()
            self.my_label.config(text=f"Votre langage est : '{my_result}'")
        
        
if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
