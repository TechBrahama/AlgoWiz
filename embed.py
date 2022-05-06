import os
import pygame
import tkinter as tk
from tkinter import *

from colors import *

root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500,bg=BLUE) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500,)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((400,100))
screen.fill(pygame.Color(200,255,255))
pygame.display.init()
pygame.display.update()

def draw():
    pygame.draw.circle(screen, (0,0,0), (20,20), 25)
    pygame.display.update()

button1 = Button(buttonwin,text = 'Draw',  command=draw)
button1.pack(side=LEFT)
root.update()

while True:
    pygame.display.update()
    root.update()