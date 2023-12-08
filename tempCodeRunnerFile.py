import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from dashboard import dashboard
import sqlite3


window = tk.Tk()
window.title('Welcome')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))


def proceed_dashboard():
    show = dashboard(window)

#Login Function