"""
Tkinter - Codemy.com : Build A Spell Checker App - Tkinter Projects 9
Lien : https://www.youtube.com/watch?v=bj_VHe-iVYk

Module installé :
pip install textblob

Date : 26-10-2022
"""

import tkinter as tk
from textblob import TextBlob

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Spell Checker!")
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_text = tk.Text(root, width=50)
        self.my_text.pack(pady=20)
        
        my_button = tk.Button(
            root, text="Fix Spelling Erros", command=self.spellerize)
        my_button.pack(pady=20)
        
    def spellerize(self):
        
        # Grab text from box
        get_text = self.my_text.get(1.0, 'end')
        
        # Delete textbox text
        self.my_text.delete(1.0, 'end')
        
        # Convert text to blob
        blobby = TextBlob(get_text)
        
        # Fix spelling errors
        self.my_text.insert(1.0, blobby.correct())

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
