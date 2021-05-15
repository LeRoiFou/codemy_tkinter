"""
Tkinter - Codemy.com #27 : Numpy & Matplotlib
Lien : https://www.youtube.com/watch?v=8exB6Ly3nx0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=27

Le module matplotlib permet de présenter des graphiques, pour plus d'information, voir le site :
https://matplotlib.org/

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

import tkinter
import numpy as np
import matplotlib.pyplot as plt

root = tkinter.Tk()
root.geometry('400x200')
root.title("#27 : Numpy & Matplotlib")


def graph():
    house_prices = np.random.normal(200_000, 25_000, 5_000)
    plt.hist(house_prices, 200)
    plt.show()


my_button = tkinter.Button(root, text='Graphique !', command=graph)
my_button.pack()

root.mainloop()