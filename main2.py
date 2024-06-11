import tkinter as tk
from tkinter import filedialog
import pygame
import sqlite3
from mutagen.easyid3 import EasyID3
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize Tkinter
root = tk.Tk()
root.title("Basic Music Player")

# Function to load a music file
def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        song_title.set(os.path.basename(file_path))
        pygame.mixer.music.load(file_path)

# Function to play music
def play_music():
    pygame.mixer.music.play()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# UI Elements
song_title = tk.StringVar()
title_label = tk.Label(root, textvariable=song_title)
title_label.pack()

load_button = tk.Button(root, text="Load", command=load_music)
load_button.pack()

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack()

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack()

# Run the application
root.mainloop()
