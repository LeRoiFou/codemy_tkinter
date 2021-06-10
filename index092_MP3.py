"""
Tkinter - Codemy.com #92 : MP3 Player Song Position Slider (part 6)
Lien : https://www.youtube.com/watch?v=CXMcNbo8PLE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=92

Création d'un lecteur mp3 virtuel

Dans ce programme, on créé :
-> On ajuste la position de la chanson avec le curseur
-> On commence à positionner le temps afficher au curseur avec la position de la chanson

Éditeur : Laurent REYNAUD
Date : 13-12-20
"""

from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Ma musique !')
root.geometry('500x450')
root.resizable(False, False)

"""Initialisation de la classe mixer du module pygame pour la musique"""
pygame.mixer.init()


def play_time():
    """Détermination de la durée de la musique
    Cette durée va s'activer lors du lancement de la musique, il faut donc rajouter des instructions supplémentaires
    dans la fonction play(), et dans la fonction stop() on efface le temps affiché dès qu'on active le bouton stop.
    L'instruction time.gmtime() permet de réinitialiser le temps à chaque fois qu'on met en lecture un autre titre"""
    current_time = pygame.mixer.music.get_pos() / 1000  # temps actuel du titre en seconde

    """Création d'une étiquette temporaire pour obtenir des données"""
    slider_label.config(text=f"Curseur : {int(my_slider.get())} et position de la musique : {int(current_time)} ")

    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))  # conversion au format 00:00

    """Détermination de la durée totale du titre avec le module mutagen"""
    song = song_box.get(ACTIVE)  # Activation de la listbox
    song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
    song_mut = MP3(song)  # chargement du titre avec le module mutagen
    global song_length  # cette variable est également utilisée dans la fonction slide()
    song_length = song_mut.info.length  # durée totale du titre en secondes
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))  # conversion au format 00:00

    current_time += 1  # évite le décalage entre le temps écoulé et le défilement de la musique

    if int(my_slider.get()) == int(song_length):
        """Si le chiffrement du curseur est égal à la durée totale du titre : affichage du temps écoulé.. """
        status_bar.config(text=f"Temps écoulé : {converted_song_length}"
                               f" sur une durée totale de {converted_song_length} ")  # config barre de statut
        """Sinon si le chiffrement du curseur est égal au temps écoulé"""
    elif int(my_slider.get()) == int(current_time):
        """Alors le curseur n'a pas été déplacé"""
        """Mise à jour de la position du curseur  
        Dans la création du curseur, on a mis comme argument to=100, mais pour que le curseur s'adapte à la durée totale 
        du titre, on remplace to=100 par to=int(song_lenght) qui est la durée totale du titre en secondes.  
        L'instruction value est cette fois-ci égale au temps écoulé de l'instruction current_time"""
        slider_position = int(song_length)  # variable sur la durée totale du titre en secondes (entiers)
        my_slider.config(to=slider_position, value=int(current_time))  # configuration de l'étiquette du curseur
    else:
        """Sinon le curseur a été déplacé"""
        slider_position = int(song_length)  # variable sur la durée totale du titre en secondes (entiers)
        my_slider.config(to=slider_position, value=int(my_slider.get()))  # configuration de l'étiquette du curseur
        converted_current_time = time.strftime('%M:%S',
                                               time.gmtime(int(my_slider.get())))  # conversion au format 00:00
        status_bar.config(text=f"Temps écoulé : {converted_current_time}"
                               f" sur une durée totale de {converted_song_length} ")  # config barre de statut
        # my_slider.config(value=int(current_time))  # mise à jour de la position du curseur
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    status_bar.after(1000, play_time)  # mise à jour du temps


def add_song():
    """Récupère un fichier .mp3 et affichage de la musique ajoutée dans la listbox"""
    song = filedialog.askopenfilename(initialdir='F:/MUSIQUES/',
                                      title='Choisir une musique',
                                      filetypes=(('Fichiers .mp3', '*.mp3'), ('Tous fichiers', '*.*')))
    song = song.replace('F:/MUSIQUES/', '')  # suppression à l'affichage du répertoire F:/MUSIQUES/
    song = song.replace('.mp3', '')  # suppression de l'extension .mp3 du fichier
    song_box.insert(END, song)  # ajout du titre de la chanson dans la listbox


def add_many_songs():
    """Récupère plusieurs fichiers .mp3 et affichage des musiques ajoutées dans la lisbtox
    Cette fois-ci on utilise dans l'instruction filedialog, la méthode askopenfilenames (au pluriel) qui permet de
    récupérer plusieurs fichiers, au lieu de la méthode askopenfilename (au singulier) qui permet de récupérer qu'un
    seul fichier"""
    songs = filedialog.askopenfilenames(initialdir='F:/MUSIQUES/',
                                        title='Choisir plusieurs musiques',
                                        filetypes=(('Fichiers .mp3', '*.mp3'), ('Tous fichiers', '*.*')))
    """Liste des chansons à récupérer avec le recours de la boucle for"""
    for song in songs:
        song = song.replace('F:/MUSIQUES/', '')  # suppression à l'affichage du répertoire F:/MUSIQUES/
        song = song.replace('.mp3', '')  # suppression de l'extension .mp3 du fichier
        song_box.insert(END, song)  # ajout du titre de la chanson dans la listbox


def play():
    """Lecture du titre sélectionné de la playlist"""
    song = song_box.get(ACTIVE)  # activitation de la listbox
    song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
    pygame.mixer.music.load(song)  # chargement de la musique
    pygame.mixer.music.play(loops=0)  # lecture de la musique sans boucle
    play_time()  # appel de la fonction pour afficher la durée du titre


def stop():
    """Arrêt de lecture du titre sélectionné de la playlist"""
    pygame.mixer.music.stop()  # arrêt de la musique
    song_box.select_clear(ACTIVE)  # suppression de la sélection du fichier joué
    # status_bar.config(text='')  # le temps affiché est effacé


def next_song():
    """Lecture du titre suivant de la playlist
    Dans cette fonction on a recours aux listes pour pouvoir récupérer le titre suivant celui qu'on a sélectionné"""
    next_one = song_box.curselection()  # déclaration en variable du titre sélectionné
    next_one = next_one[0] + 1  # n° d'indice du titre qui se situe APRES le titre sélectionné
    song = song_box.get(next_one)  # le n° d'indice est transformé en nom du titre suivant celui qui est sélectionné
    song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
    pygame.mixer.music.load(song)  # chargement de la musique
    pygame.mixer.music.play(loops=0)  # lecture de la musique sans boucle
    song_box.select_clear(0, END)  # effacement de la barre de sélection du titre
    song_box.activate(next_one)  # activation dans la listbox du titre suivant celui initialement sélectionné
    song_box.selection_set(next_one, last=None)  # déplacement de la barre de sélection au titre suivant


def previous_song():
    """Lecture du titre précédent de la playlist
    Dans cette fonction on a recours aux listes pour pouvoir récupérer le titre suivant celui qu'on a sélectionné.
    La fonction est identique que la fonction next_song() sauf qu'au lieu d'augmenter l'indice de 1, on le diminue
    cette fois-ci de 1"""
    next_one = song_box.curselection()  # déclaration en variable du titre sélectionné
    next_one = next_one[0] - 1  # n° d'indice du titre qui se situe AVANT le titre sélectionné
    song = song_box.get(next_one)  # le n° d'indice est transformé en nom du titre suivant celui qui est sélectionné
    song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
    pygame.mixer.music.load(song)  # chargement de la musique
    pygame.mixer.music.play(loops=0)  # lecture de la musique sans boucle
    song_box.select_clear(0, END)  # effacement de la barre de sélection du titre
    song_box.activate(next_one)  # activation dans la listbox du titre suivant celui initialement sélectionné
    song_box.selection_set(next_one, last=None)  # déplacement de la barre de sélection au titre suivant


def delete_song():
    """Suppression d'un titre de la playlist"""
    song_box.delete(ANCHOR)  # suppression du titre sélectionné
    pygame.mixer.music.stop()  # dès que le titre est supprimé, la lecture de la musique de ce titre s'arrête


def delete_all_songs():
    """Suppression de tous les titres de la playlist"""
    song_box.delete(0, END)  # suppression de tous les titres de la playlist
    pygame.mixer.music.stop()  # dès que le titre est supprimé, la lecture de la musique de ce titre s'arrête


"""Variable globale 'paused' = cette variable va être utilisée dans la fonction ci-après, la fonction pause n'étant pas  
en lien avec le reste de la programmation, elle doit donc être déclarée en tant que variable globale"""
global paused
paused = False  # si on met True, lorsqu'on appuye une 1er fois sur le bouton pause, celui-ci ne fonctionnera pas


def pause(is_paused):
    """Pause de la lecture d'un fichier .pm3
    Dans cette fonction on est en présence de deux instructions :
    -> pygame.mixer.music.pause() : mettre en pause la musique
    -> pygame.mixer.music.unpause() : arrête de la pause de la musique
    Or, le programme doit pouvoir distinguer que lorsqu'on appuye sur le bouton pause, la musique se met en pause et
    lorsqu'on appuye à nouveau sur le bouton pause, la musique s'arrête de se mettre en pause.
    C'est la raison pour laquelle la fonction dispose d'une part d'un argument en paramètre et d'autre part on utilise
    un booléen"""
    global paused  # appel de la variable globale
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()  # arrêt de la pause de la musique
        paused = False  # si on ne met pas cette instruction, le bouton n'est plus activable
    else:
        pygame.mixer.music.pause()  # pause de la musique
        paused = True  # si on ne met pas cette instruction, le bouton n'est plus activable


def slide(*args):
    """Position du curseur par rapport à la musique"""
    # slider_label.config(text=f"{int(my_slider.get())} sur une durée totale de {int(song_length)}")
    song = song_box.get(ACTIVE)  # activitation de la listbox
    song = f"F:/MUSIQUES/{song}.mp3"  # récupération du chemin complet du fichier .mp3
    pygame.mixer.music.load(song)  # chargement de la musique
    """En ajoutant l'instruction start, la chanson du titre va être jouée au regard de la position du curseur, mais la 
    position du curseur se réinitialise au début"""
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))  # lecture de la musique sans boucle


"""Configuration d'une box de playlist :   
-> selectbackground = couleur de la ligne du titre de la musique lorsqu'elle est sélectionnée  
-> selectforeground = couleur de l'écriture du titre de la musique lorsqu'elle est sélectionnée"""
song_box = Listbox(root, bg='black', fg='red', width=60, selectbackground='gray', selectforeground='black')
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
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
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

"""Ajout des musiques à partir du menu"""
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Ajouter des musiques', menu=add_song_menu)
add_song_menu.add_command(label='Ajouter une musique de la playlist', command=add_song)
add_song_menu.add_command(label='Ajouter plusieurs musiques de la playlist', command=add_many_songs)

"""Suppression des musiques à partir du menu"""
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Supprimer des musiques', menu=remove_song_menu)
remove_song_menu.add_command(label='Supprimer une musique de la playlist', command=delete_song)
remove_song_menu.add_command(label='Supprimer toutes les musiques de la playlist', command=delete_all_songs)

"""Création d'une barre de statut"""
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

"""Création d'un curseur  
Dans la fonction play() on 'met à jour' l'instruction to=100 par to=song_length qui est la durée totale du titre"""
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, length=360, command=slide)
my_slider.pack(pady=30)

"""Création d'une étiquette concernant le curseur"""
slider_label = Label(root, text='0')
slider_label.pack(pady=10)

root.mainloop()
