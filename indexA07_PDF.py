"""
Tkinter - Codemy.com : How To Extract Text From PDF Files - Tkinter Projects 6
Lien : https://www.youtube.com/watch?v=i1dJTrDuGVc

Module PyPDF2 installé

Éditeur : Laurent REYNAUD
Date : 05-10-22
"""

import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("PDF")
        root.geometry('550x650')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Text box
        self.my_text = tk.Text(root, width=60, height=25)
        self.my_text.pack(pady=20)
        
        # LabelFrame and entry box
        my_label_frame = tk.LabelFrame(root, text="Select Page to Open")
        my_label_frame.pack(pady=10)
        
        my_label = tk.Label(my_label_frame, text="Page Number: ")
        my_label.grid(column=0, row=0, pady=10, padx=10)
        
        self.my_entry = tk.Entry(my_label_frame)
        self.my_entry.grid(column=1, row=0, padx=10, pady=10)
        
        # Open Button
        my_button = tk.Button(root, text="Open PDF", command=self.open_pdf)
        my_button.pack(pady=20)
        
        # Page Number Label
        self.pages_label = tk.Label(root, text="")
        self.pages_label.pack(pady=20)
    
    def open_pdf(self):
        
        # Get file name
        my_file = filedialog.askopenfilename(
            title="Open File", filetype=(("PDF Files", ".pdf"),
                                          ("All files", "*.*")))
        
        try:
            # Open file
            pdf_file = PyPDF2.PdfFileReader(my_file)
            
            # Get the number of pages
            number_of_pages = len(pdf_file.pages)
            
            # Update or pages label
            self.pages_label.config(
                text=f"Showing {self.my_entry.get()} of {number_of_pages-1} pages...")
        
            # Select page to read
            page = pdf_file.getPage(int(self.my_entry.get()))
            
            # Get the content from the page
            content = page.extractText()
            
            # Clear the text box
            self.my_text.delete(1.0, 'end')
            
            # Output pdf to text
            self.my_text.insert(1.0, content)
            
        except Exception as e:
            
            messagebox.showerror("Woah!", 
                                 f"There was a problem! {e}")
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
