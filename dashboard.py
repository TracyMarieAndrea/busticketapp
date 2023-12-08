from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form
from bus_seating import bus_seating

class dashboard(object):

    def __init__(self,window):

        dashboard_window = tk.Tk()
        dashboard_window.title('Dashboard')

        width = dashboard_window.winfo_screenwidth()
        height = dashboard_window.winfo_screenheight()

        dashboard_window.geometry("%dx%d" % (width, height))

        

        
        def proceed_bus_management():
            show = bus_management(dashboard_window)
        def proceed_bus_details_form():
            show = bus_details_form(dashboard_window)
        def proceed_bus_seating(location,time):
            #confirmation = messagebox.askyesno("Confirmation", f"Selected Location: {location}\nTime: {time}\nProceed to Bus Seating?")
            show = bus_seating(dashboard_window, location, time)
            
            
           

        menubar = Menu(dashboard_window)
        dashboard_window.config(menu=menubar)

        # create a menu
        bus_menu = Menu(menubar, tearoff=False)
        report_menu = Menu(menubar)

        # add a menu item to the menu
        bus_menu.add_command(
            label='Bus Management',
            command=proceed_bus_management
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="Bus",
            menu=bus_menu
        )
        menubar.add_cascade(
            label="Report"
        )

        frame = Frame(dashboard_window)
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

        caticlan_bottomframe = Frame(dashboard_window)
        caticlan_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        caticlan_seatnum = ["6:00AM", "10:00AM", "2:00PM", "6:00PM"]

        for caticlan_seat in caticlan_seatnum:
            caticlan_bus_button = Button(caticlan_bottomframe, text=caticlan_seat, fg="red", width=35, height=3, command=lambda bustime=caticlan_seat: proceed_bus_seating("Caticlan",bustime))
            caticlan_bus_button.pack(padx=10, pady=10)

        kalibo_bottomframe = Frame(dashboard_window)
        kalibo_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        kalibo_seatnum = ["5:00AM", "10:30AM", "1:00PM", "4:00PM"]

        for kalibo_seat in kalibo_seatnum:
            kalibo_bus_button = Button(kalibo_bottomframe, text=kalibo_seat, fg="red", width=35, height=3, command=lambda bustime=caticlan_seat: proceed_bus_seating("Kalibo",bustime))
            kalibo_bus_button.pack(padx=10, pady=10)

        antique_bottomframe = Frame(dashboard_window)
        antique_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        antique_seatnum = ["5:30AM", "9:00AM", "12:00PM", "4:00PM"]

        for antique_seat in antique_seatnum:
            antique_bus_button = Button(antique_bottomframe, text=antique_seat, fg="red", width=35, height=3, command=lambda bustime=caticlan_seat: proceed_bus_seating("Antique",bustime))
            antique_bus_button.pack(padx=10, pady=10)

        capiz_bottomframe = Frame(dashboard_window)
        capiz_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        capiz_seatnum = ["7:30AM", "12:00PM", "2:30PM", "6:00PM"]

        for capiz_seat in capiz_seatnum:
            capiz_bus_button = Button(capiz_bottomframe, text=capiz_seat, fg="red", width=35, height=3, command=lambda bustime=caticlan_seat: proceed_bus_seating("Capiz",bustime))
            capiz_bus_button.pack(padx=10, pady=10)

        window.mainloop()