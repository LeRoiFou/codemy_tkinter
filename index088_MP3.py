"""
Tkinter - Codemy.com #88 : MP3 Player Pause Button pt2
Lien : https://www.youtube.com/watch?v=xknYbrbdKnA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=88

Création d'un lecteur mp3 virtuel

Dans ce programme on créé :
-> une fonction pour mettre en pause la musique avec le recours d'une fonction lambda et d'un booléen ;
-> une fonction permettant de récupérer d'un coup plusieurs musiques

Éditeur : Laurent REYNAUD
Date : 12-12-20
"""

from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Ma musique !')
root.geometry('500x300')
root.resizable(False, False)

"""Initialisation de la classe mixer du module pygame pour la musique"""
pygame.mixer.init()


def add_song():
    """Récupère un fichier .mp3 et affichage de la musique ajoutée dans la listbox"""
    song = filedialog.askopenfilename(initialdir='F:/MUSIQUES/',
                                      title='Choisir une musique',
                                      filetypes=(('Fichiers .mp3', '*.mp3'), ('Tous fichiers', '*.*')))
    song = song.replace('F:/MUSIQUES/', '')  # suppression à l'affichage du répertoire F:/MUSIQUES/
    song = song.replace('.mp3', '')  # suppression de l'extension .mp3 du fichier
    song_box.insert(END, song)  # ajout du titre de la chanson dans la listbox


def add_many_songs():
    """Récupère plusieurs fichiers .mp3 et affichage des musiques ajoutées dans la lisbtox : cette fois-ci on utilise
    dans l'instruction filedialog, la méthode askopenfilenames (au pluriel) qui permet de récupérer plusieurs fichiers,
    au lieu de la méthode askopenfilename (au singulier) qui permet de récupérer qu'un seul fichier"""
    songs = filedialog.askopenfilenames(initialdir='F:/MUSIQUES/',
                                        title='Choisir plusieurs musiques',
                                        filetypes=(('Fichiers .mp3', '*.mp3'), ('Tous fichiers', '*.*')))
    """Liste des chansons à récupérer avec le recours de la boucle for"""
    for song in songs:
        song = song.replace('F:/MUSIQUES/', '')  # suppression à l'affichage du répertoire F:/MUSIQUES/
        song = song.replace('.mp3', '')  # suppression de l'extension .mp3 du fichier
        song_box.insert(END, song)  # ajout du titre de la chanson dans la listbox


def play():
    """Lecture d'un fichier .mp3"""
    try:
        song = song_box.get(ACTIVE)  # activitation de la listbox
        song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
        pygame.mixer.music.load(song)  # chargement de la musique
        pygame.mixer.music.play(loops=0)  # lecture de la musique sans boucle
    except pygame.error:
        pass


def stop():
    """Arrêt de lecture d'un fichier .mp3"""
    pygame.mixer.music.stop()  # arrêt de la musique
    song_box.select_clear(ACTIVE)  # suppression de la sélection du fichier joué


"""Variable globale 'paused' = cette variable va être utilisée dans la fonction ci-après, la fonction pause n'étant pas 
en lien avec le reste de la programmation, elle doit donc être déclarée en tant que variable globale"""
global paused
paused = False  # si on met True, lorsqu'on appuye une 1er fois sur le bouton pause, celui-ci ne fonctionnera pas


def pause(is_paused):
    """Pause de la lecture d'un fichier .pm3 : dans cette fonction on est en présence de deux instructions :
    -> pygame.mixer.music.pause() : mettre en pause la musique
    -> pygame.mixer.music.unpause() : arrête de la pause de la musique
    Or, le programme doit pouvoir distinguer que lorsqu'on appuye sur le bouton pause, la musique se met en pause et
    lorsqu'on appuye à nouveau sur le bouton pause, la musique s'arrête de se mettre en pause. C'est la raison pour
    laquelle d'une part que la fonction dispose d'un argument en paramètre et d'autre part on utilise un booléen"""
    global paused  # appel de la variable globale
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()  # arrêt de la pause de la musique
        paused = False  # si on ne met pas cette instruction, le bouton n'est plus activable
    else:
        pygame.mixer.music.pause()  # pause de la musique
        paused = True  # si on ne met pas cette instruction, le bouton n'est plus activable


"""Configuration d'une box de playlist :  
-> selectbackground = couleur de la ligne du titre de la musique lorsqu'elle est sélectionnée 
-> selectforeground = couleur de l'écriture du titre de la musique lorsqu'elle est sélectionnée"""
song_box = Listbox(root, bg='black', fg='green', width=60, selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)

"""Configuration des boutons en tant qu'image pour la musique"""
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/Forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

"""Configuration du cadre des touches de contrôle pour la musique"""
controls_frame = Frame(root)
controls_frame.pack()

"""Configuration des touches de contrôle des images pour la musique : 
La commande pause est sous la forme d'une fonction lambda car elle possède un argument dans ses paramètres"""
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

"""Configuration d'un menu"""
my_menu = Menu(root)
root.config(menu=my_menu)

"""Ajout des musiques dans le menu"""
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Ajouter des musiques', menu=add_song_menu)
add_song_menu.add_command(label='Ajouter une musique à la playlist', command=add_song)
add_song_menu.add_command(label='Ajouter plusieurs musiques à la playlist', command=add_many_songs)

root.mainloop()
