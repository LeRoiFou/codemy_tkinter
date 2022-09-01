"""
Tkinter - Codemy.com : Magic 8-Ball App - Tkinter Projects 2
Lien : https://www.youtube.com/watch?v=FpGHXkjfw9U



Éditeur : Laurent REYNAUD
Date : 01-09-22
"""

import customtkinter as ctk
from PIL import Image, ImageTk
import random
import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        
        self.root = root
        root.title("Magic 8 Ball!")
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Shake The 8 ball Function
        
        # Define our images
        self.ball = ImageTk.PhotoImage(Image.open('images/8ball.png'))
        ball_img = tk.Label(root, image=self.ball, bd=0)
        ball_img.pack(pady=35)
        
        # Set results
        self.results = tk.Label(root, text='', font='Helvetica 28', bg="#1a1a1a")
        self.results.pack(pady=20)
        
        # Define our button
        my_button = ctk.CTkButton(root, text="Shake 8-Ball", width=190, height=40,
                                  compound='top', command=self.shake)
        my_button.pack(pady=30)
        
    def shake(self):
        
        answers = {
            "It is certain": "green",
            "It is decidedly so": "green",
            "Without a doubt":"green",
            "Yes definitely":"green",
            "You may rely on it":"green",
            "As I see it, yes":"green",
            "Most likely":"green",
            "Outlook good":"green",
            "Yes":"green",
            "Signs point to yes":"green",

            "Reply hazy, try again":"yellow",
            "Ask again later":"yellow",
            "Better not tell you now":"yellow",
            "Cannot predict now":"yellow",
            "Concentrate and ask again":"yellow",

            "Don't count on it!":"red",
            "My reply is no!":"red",
            "My sources say no!":"red",
            "Outlook not so good!":"red",
            "Very doubtful!":"red"}
        
        # Convert dictionary to list
        answer_list = list(answers.items())
        
        # Shuffle the list 
        # (équivalent à un ensemble mais avec des doublons)
        random.shuffle(answer_list)
        
        # Output to the screen
        self.results.config(text=answer_list[0][0], 
                            fg=answer_list[0][1])

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
