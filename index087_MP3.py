"""
Tkinter - Codemy.com #87 : Build An MP3 Player With Tkinter pt1
Lien : https://www.youtube.com/watch?v=88IJCBKlAPA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=87

Création d'un lecteur mp3 virtuel

Dans ce programme on créé le lecteur mp3 virtuel avec :
-> un menu avec ajout d'une musique dans la listbox
-> une listbox
-> des boutons en forme d'images
-> lecture de la musique
-> arrêt de la musique

Éditeur : Laurent REYNAUD
Date : 11-12-20
"""

import tkinter
import pygame
from tkinter import filedialog

root = tkinter.Tk()
root.title('Ma musique !')
root.geometry('500x300')
root.resizable(False, False)

"""Initialisation de la classe mixer du module pygame pour la musique"""
pygame.mixer.init()


def add_song():
    """Récupère un fichier .mp3 directement sur la carte SD et affichage de la musique ajoutée dans la listbox"""
    song = filedialog.askopenfilename(initialdir='F:/MUSIQUES/',
                                      title='Choisir une musique',
                                      filetypes=(('Fichiers .mp3', '*.mp3'), ('Tous fichiers', '*.*')))
    song = song.replace('F:/MUSIQUES/', '')  # suppression à l'affichage du répertoire F:/MUSIQUES/
    song = song.replace('.mp3', '')  # suppression de l'extension .mp3 du fichier
    song_box.insert(END, song)  # ajout du titre de la chanson dans la listbox


def play():
    """Lecture d'un fichier .mp3"""
    try:
        song = song_box.get('active')  # activitation de la listbox
        song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
        pygame.mixer.music.load(song)  # chargement de la musique
        pygame.mixer.music.play(loops=0)  # lecture de la musique sans boucle
    except pygame.error:
        pass


def stop():
    """Arrêt de lecture d'un fichier .mp3"""
    pygame.mixer.music.stop()  # arrêt de la musique
    song_box.select_clear('active')  # suppression de la sélection du fichier joué


"""Configuration d'une box de playlist :  
-> selectbackground = couleur de la ligne du titre de la musique lorsqu'elle est sélectionnée 
-> selectforeground = couleur de l'écriture du titre de la musique lorsqu'elle est sélectionnée"""
song_box = tkinter.Listbox(root, bg='black', fg='green', width=60, selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)

"""Configuration des boutons en tant qu'image pour la musique"""
back_btn_img = tkinter.PhotoImage(file='images/back50.png')
forward_btn_img = tkinter.PhotoImage(file='images/Forward50.png')
play_btn_img = tkinter.PhotoImage(file='images/play50.png')
pause_btn_img = tkinter.PhotoImage(file='images/pause50.png')
stop_btn_img = tkinter.PhotoImage(file='images/stop50.png')

"""Configuration des cadres des touches de contrôle pour la musique"""
controls_frame = tkinter.Frame(root)
controls_frame.pack()

"""Configuration des touches de contrôle des images pour la musique"""
back_btn = tkinter.Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_btn = tkinter.Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_btn = tkinter.Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_btn = tkinter.Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_btn = tkinter.Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

"""Configuration d'un menu"""
my_menu = tkinter.Menu(root)
root.config(menu=my_menu)

"""Ajout des musiques dans le menu"""
add_song_menu = tkinter.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Ajouter des musiques', menu=add_song_menu)
add_song_menu.add_command(label='Ajouter une musique à la playlist', command=add_song)

root.mainloop()
