"""
Tkinter - Codemy.com : Build A QR Code Generator App - Tkinter Projects 10
Lien : https://www.youtube.com/watch?v=OKA-XkZtYpg

Modules installés :
pip install pyqrcode
pip install pypng

Date : 05-11-22
"""

import pyqrcode
from PIL import Image, ImageTk
import png
import tkinter as tk
from tkinter import filedialog

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Title!")
        root.geometry('500x550')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create GUI
        self.my_entry = tk.Entry(
            root, font='Helvetica 18', justify='center')
        self.my_entry.pack(pady=20)
        
        my_button = tk.Button(
            root, text='Create QR Code', command=self.create_code)
        my_button.pack(pady=20)
        
        my_button2 = tk.Button(
            root, text="Clear", command=self.clear_all)
        my_button2.pack()
        
        self.my_label = tk.Label(root, text='')
        self.my_label.pack(pady=20)
        
    def create_code(self):
        
        # File Dialog
        input_pass = filedialog.asksaveasfilename(
            title="Save Image", filetypes=(('PNG file', '.png'),
                                            ('All files', '*.*')))
        
        if input_pass:
            if input_pass.endswith('.png'):
                # Create QR Code from entry box
                get_code = pyqrcode.create(self.my_entry.get())
                # Save as PNG File
                get_code.png(input_pass, scale=5)
            else:
                # Add that .png to the end of the file name
                input_pass = f'{input_pass}.png'
                # Create QR Code from entry box
                get_code = pyqrcode.create(self.my_entry.get())
                # Save as PNG File
                get_code.png(input_pass, scale=5)
                
        # Put QR code on screen
        self.get_image = ImageTk.PhotoImage(Image.open(input_pass))
        
        # Add image to label
        self.my_label.config(image=self.get_image)
        
        # Delete entry box
        self.my_entry.delete(0, 'end')
        
        # Flash up a finished message
        self.my_entry.insert(0, 'Finished!')
            
    def clear_all(self):
        
        self.my_entry.delete(0, 'end')
        self.my_label.config(image='')

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
