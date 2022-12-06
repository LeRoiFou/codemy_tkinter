"""
Tkinter - Codemy.com : How To Add PNG Image Files To PDF - Tkinter Projects 14
Lien : https://www.youtube.com/watch?v=P2jrY0EAx44

pip install fpdf
pip install pillow


Date : 06-12-22
"""

import tkinter as tk
from fpdf import FPDF
from PIL import Image, ImageTk
from tkinter import filedialog

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Save Image as PDF!")
        root.geometry('600x600')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_label = tk.Label(
            root, text="Open Image", font='Helvetica 28')
        self.my_label.pack(pady=50)
        
        open_button = tk.Button(
            root, text="Open Image", command=self.opener)
        open_button.pack(pady=10)
        
        open_button = tk.Button(
            root, text="Save to PDF", command=self.saver)
        open_button.pack()
        
    def opener(self):
        
        # Open file dialog box
        input_path = filedialog.askopenfilename(
            title="Open Image", 
            filetypes=(('PNG', '.png'), ("All Files", '*.*')))
        
        # Set file path global to use it lateur
        self.image_path = input_path
        
        if input_path :
            
            if input_path.endswith(".png"):
                
                # Get Image
                self.get_image = ImageTk.PhotoImage(Image.open(input_path))
                
                # Add Image to Label
                self.my_label.config(image=self.get_image)
            
            else:
                
                # Add PNG to end of path
                input_path = f"{input_path}.png"
                
                # Get Image
                self.get_image = ImageTk.PhotoImage(Image.open(input_path))
                
                # Add Image to Label
                self.my_label.config(image=self.get_image)
    
    def saver(self):
        
        # Open file dialog to save PDF
        input_path = filedialog.asksaveasfilename(
            title="Save PDF", 
            filetypes=(('PDF', '.pdf'), ("All Files", '*.*')))
        
        if input_path:
            
            if input_path.endswith('.pdf'):
                
                # Create fpdf instance
                pdf = FPDF()
                
                # Create a pdf page
                pdf.add_page()
                
                # Add image to page
                pdf.image(self.image_path, x=50, y=50, w=50, h=50)
                
                # Save pdf
                pdf.output(input_path, 'F')
                
                # Update label
                self.my_label.config(image='', text='DONE!')
            
            else:
                
                # add PDF file extension
                input_path = f"{input_path}.pdf"

                # Create fpdf instance
                pdf = FPDF()
                
                # Create a pdf page
                pdf.add_page()
                
                # Add image to page
                pdf.image(self.image_path, x=50, y=50, w=50, h=50)
                
                # Save pdf
                pdf.output(input_path, 'F')
                
                # Update label
                self.my_label.config(image='', text='DONE!')

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
