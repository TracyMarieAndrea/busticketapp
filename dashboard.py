from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form
from bus_seating import bus_seating

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
        def proceed_bus_seating():
            show = bus_seating(window)

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
        
        labels = [
            ("CATICLAN", 'black', 12),
            ("KALIBO", 'black', 12),
            ("ANTIQUE", 'black', 12),
            ("CAPIZ", 'black', 12)
        ]

        for text, color, width in labels:
            label = tk.Label(frame, text=text, font=('Roboto', 25, 'bold'), fg=color, width=width)
            label.pack(side=LEFT, padx=10, pady=10)

        caticlan_bottomframe = Frame(window)
        caticlan_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        caticlan_seatnum = ["A1", "A2", "A3", "A4"]

        for caticlan_seat in caticlan_seatnum:
            caticlan_bus_button = Button(caticlan_bottomframe, text=caticlan_seat, fg="red", width=35, height=3, command=proceed_bus_seating)
            caticlan_bus_button.pack(padx=10, pady=10)

        kalibo_bottomframe = Frame(window)
        kalibo_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        kalibo_seatnum = ["B1", "B2", "B3", "B4"]

        for kalibo_seat in kalibo_seatnum:
            kalibo_bus_button = Button(kalibo_bottomframe, text=kalibo_seat, fg="red", width=35, height=3, command=proceed_bus_seating)
            kalibo_bus_button.pack(padx=10, pady=10)

        antique_bottomframe = Frame(window)
        antique_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        antique_seatnum = ["C1", "C2", "C3", "C4"]

        for antique_seat in antique_seatnum:
            antique_bus_button = Button(antique_bottomframe, text=antique_seat, fg="red", width=35, height=3, command=proceed_bus_seating)
            antique_bus_button.pack(padx=10, pady=10)

        capiz_bottomframe = Frame(window)
        capiz_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        capiz_seatnum = ["C1", "C2", "C3", "C4"]

        for capiz_seat in capiz_seatnum:
            capiz_bus_button = Button(capiz_bottomframe, text=capiz_seat, fg="red", width=35, height=3, command=proceed_bus_seating)
            capiz_bus_button.pack(padx=10, pady=10)

        window.mainloop()