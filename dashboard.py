from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form

class dashboard(object):

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
        red_label = tk.Label(frame, text="CALIBO", font=('Roboto', 25, 'bold'), fg='black', width=20)
        red_label.pack(side=LEFT, padx=10, pady=10)
        green_label = tk.Label(frame, text="CALIBO", font=('Roboto', 25, 'bold'), fg='black')
        green_label.pack(side=LEFT, padx=10, pady=10)
        blue_label = tk.Label(frame, text="CALIBO", font=('Roboto', 25, 'bold'), fg='black', width=20)
        blue_label.pack(side=LEFT, padx=10, pady=10)
        black_label = tk.Label(frame, text="CALIBO", font=('Roboto', 25, 'bold'), fg='black')
        black_label.pack(side=LEFT, padx=10, pady=10)


        bottomframe = Frame(window)
        bottomframe.pack()

        redbutton = Button(bottomframe, text="Red", fg="red", width=40, height=3)
        redbutton.pack( side = LEFT, padx=10, pady=10)

        greenbutton = Button(bottomframe, text="Brown", fg="brown", width=40, height=3)
        greenbutton.pack( side = LEFT, padx=10, pady=10)

        bluebutton = Button(bottomframe, text="Blue", fg="blue", width=40, height=3)
        bluebutton.pack( side = LEFT, padx=10, pady=10)

        blackbutton = Button(bottomframe, text="Black", fg="black", width=40, height=3)
        blackbutton.pack( side = LEFT, padx=10, pady=10)

        bottomframe = Frame(window)
        bottomframe.pack()

        redbutton = Button(bottomframe, text="Red", fg="red", width=40, height=3)
        redbutton.pack( side = LEFT, padx=10, pady=10)

        greenbutton = Button(bottomframe, text="Brown", fg="brown", width=40, height=3)
        greenbutton.pack( side = LEFT, padx=10, pady=10)

        bluebutton = Button(bottomframe, text="Blue", fg="blue", width=40, height=3)
        bluebutton.pack( side = LEFT, padx=10, pady=10)

        blackbutton = Button(bottomframe, text="Black", fg="black", width=40, height=3)
        blackbutton.pack( side = LEFT, padx=10, pady=10)

        bottomframe = Frame(window)
        bottomframe.pack()

        redbutton = Button(bottomframe, text="Red", fg="red", width=40, height=3)
        redbutton.pack( side = LEFT, padx=10, pady=10)

        greenbutton = Button(bottomframe, text="Brown", fg="brown", width=40, height=3)
        greenbutton.pack( side = LEFT, padx=10, pady=10)

        bluebutton = Button(bottomframe, text="Blue", fg="blue", width=40, height=3)
        bluebutton.pack( side = LEFT, padx=10, pady=10)

        blackbutton = Button(bottomframe, text="Black", fg="black", width=40, height=3)
        blackbutton.pack( side = LEFT, padx=10, pady=10)

        bottomframe = Frame(window)
        bottomframe.pack()

        redbutton = Button(bottomframe, text="Red", fg="red", width=40, height=3)
        redbutton.pack( side = LEFT, padx=10, pady=10)

        greenbutton = Button(bottomframe, text="Brown", fg="brown", width=40, height=3)
        greenbutton.pack( side = LEFT, padx=10, pady=10)

        bluebutton = Button(bottomframe, text="Blue", fg="blue", width=40, height=3)
        bluebutton.pack( side = LEFT, padx=10, pady=10)

        blackbutton = Button(bottomframe, text="Black", fg="black", width=40, height=3)
        blackbutton.pack( side = LEFT, padx=10, pady=10)

        window.mainloop()