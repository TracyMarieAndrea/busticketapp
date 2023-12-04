
#Import the required Libraries
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk

class dashboard(object):

    def __init__(self,window):
        window = tk.Tk()
        window.title('Welcome')

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        window.mainloop()