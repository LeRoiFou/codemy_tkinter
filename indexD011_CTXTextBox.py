"""
Titre : The TextBox Widget! - Tkinter CustomTkinter 13
Lien : https://www.youtube.com/watch?v=IkjAkTMHrUw


Date : 07-11-2023
"""

import customtkinter as ctk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("TextBox!")
        root.geometry('700x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_text = ctk.CTkTextbox(
            root,
            width=600,
            height=200,
            corner_radius=1,
            border_width=10,
            border_color='#003660',
            border_spacing=10,
            fg_color='silver',
            text_color='black',
            font=('Helvetica', 18),
            wrap='word', # char default, word, none (fin de texte...)
            activate_scrollbars=True, # True default
            scrollbar_button_color='blue',
            scrollbar_button_hover_color='red',
            )
        self.my_text.pack(pady=20)
        
        my_frame = ctk.CTkFrame(root)
        my_frame.pack(pady=10)
        
        delete_button = ctk.CTkButton(my_frame, text="Delete", command=self.delete)
        copy_button = ctk.CTkButton(my_frame, text="Copy", command=self.copy)
        paste_button = ctk.CTkButton(my_frame, text="Paste", command=self.paste)
        
        delete_button.grid(row=0, column=1)
        copy_button.grid(row=0, column=2, padx=10)
        paste_button.grid(row=0, column=3)
        
        self.thing = ''
        
    def delete(self):
        
        self.my_text.delete(0.0, 'end')
    
    def copy(self):
        
        self.thing = self.my_text.get(0.0, 'end')
    
    def paste(self):
        
        if self.thing:
            self.my_text.insert('end', self.thing)
        else:
            self.my_text.insert('end', "There is nothig to paste!")
        

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
