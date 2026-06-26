from tkinter import *
from tkinter import filedialog


def soundImporter():
    filename = filedialog.askopenfilename(initialdir= "./assets/sounds",title="Select File",filetypes=(("wav files","*.wav"), ("mp3 files","*.mp3"), ("m4a files","*.m4a"))) 
    print(filename)