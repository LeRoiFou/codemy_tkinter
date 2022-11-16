"""
Tkinter - Codemy.com : How To Use Emoji's in Your Tkinter App - Tkinter Projects 12
Lien : https://www.youtube.com/watch?v=3YmZWV7iBJE

Modules installés : 
pip install emoji

Lien pour tous les emojis :
https://carpedm20.github.io/emoji/

Date : 16-11-22
"""

import emoji
import tkinter as tk


class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Emoji's!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create a Label
        my_label = tk.Label(
            root, 
            text=f"{emoji.emojize(':astonished_face:')} {emoji.emojize(':face_screaming_in_fear:')} {emoji.emojize(':face_screaming_in_fear:')}", 
            font='Helvetica 32', fg='red')
        my_label.pack(pady=50)

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
