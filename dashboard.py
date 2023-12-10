from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form
from bus_seating import bus_seating
import sqlite3

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
        def proceed_bus_seating(location,time,busno):
            #confirmation = messagebox.askyesno("Confirmation", f"Selected Location: {location}\nTime: {time}\nProceed to Bus Seating?")
            show = bus_seating(dashboard_window, location, time,busno)
            
        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()  
           

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

        
        c.execute("SELECT * FROM bus_details WHERE destination = 'Caticlan'")
        results_caticlan = c.fetchall()

        if results_caticlan:
            for result in results_caticlan:
                caticlan_bus_button = Button(caticlan_bottomframe, text=result[1] + " - " +result[6], fg="red", width=35, height=3, command=lambda busno=result[1], bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                caticlan_bus_button.pack(padx=10, pady=10)
        

        kalibo_bottomframe = Frame(dashboard_window)
        kalibo_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        c.execute("SELECT * FROM bus_details WHERE destination = 'Kalibo'")
        results_kalibo = c.fetchall()

        if results_kalibo:
            for result in results_kalibo:
                kalibo_bus_button = Button(kalibo_bottomframe, text=result[1] + " - " +result[6], fg="red", width=35, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                kalibo_bus_button.pack(padx=10, pady=10)

        antique_bottomframe = Frame(dashboard_window)
        antique_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)


        c.execute("SELECT * FROM bus_details WHERE destination = 'Antique'")
        results_antique = c.fetchall()

        if results_antique:
            for result in results_antique:
                antique_bus_button = Button(antique_bottomframe, text=result[1] + " - " +result[6], fg="red", width=35, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                antique_bus_button.pack(padx=10, pady=10)

        capiz_bottomframe = Frame(dashboard_window)
        capiz_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        c.execute("SELECT * FROM bus_details WHERE destination = 'Capiz'")
        results_capiz = c.fetchall()

        if results_capiz:
            for result in results_capiz:
                capiz_bus_button = Button(capiz_bottomframe, text=result[1] + " - " +result[6], fg="red", width=35, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                capiz_bus_button.pack(padx=10, pady=10)


        con.close()
        window.mainloop()