from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form

class bus_seating(object):

    def __init__(self,window):

        window = tk.Tk()
        window.title('Welcome')

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        
        def proceed_bus_management():
            show = bus_management(window)
        def proceed_bus_details_form():
            show = bus_details_form(window)

        menubar = Menu(window)
        window.config(menu=menubar)

        # create a menu
        bus_menu = Menu(menubar, tearoff=False)
        report_menu = Menu(menubar)

        # add a menu item to the menu
        bus_menu.add_command(
            label='Bus Management',
            command=proceed_bus_management
        )
        bus_menu.add_command(
            label='Bus Input',
            command=proceed_bus_details_form
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="Bus",
            menu=bus_menu
        )
        menubar.add_cascade(
            label="Report"
        )

        frame = Frame(window)
        frame.pack()


        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]

        for seat in seatnum:
            redbutton = Button(bottomframe, text=seat, width=5)
            redbutton.pack( side = LEFT, padx=10, pady=10)

        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]

        for seat in seatnum:
            redbutton = Button(bottomframe, text=seat, width=5)
            redbutton.pack( side = LEFT, padx=10, pady=10)  
        

        window.mainloop()