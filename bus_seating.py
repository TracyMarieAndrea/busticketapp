from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form
from passenger_details_form import passenger
import sqlite3

class bus_seating(object):

    def __init__(self,window, location, time):
        window = tk.Tk()
        window.title('Bus Seating')

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        
        def proceed_bus_management():
            show = bus_management(window)
        def proceed_bus_details_form():
            show = bus_details_form(window)
        def proceed_passenger_form(s,l,t):
            show = passenger(window,s,l,t)

        frame = Frame(window)
        frame.pack()

        location_label = tk.Label(window,text=location,font=('Roboto', 35,'bold'),fg='black')
        location_label.pack()
        location_label = tk.Label(window,text=time,font=('Roboto', 25,'bold'),fg='black')
        location_label.pack()


        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat in seatnum:
            
            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat))
            result = c.fetchone()

            button_color = "green" if result is None else "red"
            
            if(button_color == "green"):
                redbutton = Button(bottomframe, fg=button_color, text=seat, width=5,command=lambda s=seat: proceed_passenger_form(s, location, time))
            else:
                redbutton = Button(bottomframe, fg=button_color, text=seat, width=5)
            redbutton.pack( side = LEFT, padx=10, pady=10)



        con.close()
        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat in seatnum:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat))
            result = c.fetchone()

            button_color = "green" if result is None else "red"

            if(button_color == "green"):
                redbutton = Button(bottomframe, fg=button_color, text=seat, width=5,command=lambda s=seat: proceed_passenger_form(s, location, time))
            else:
                redbutton = Button(bottomframe, fg=button_color, text=seat, width=5)
            redbutton.pack( side = LEFT, padx=10, pady=10)  
        con.close()

        window.mainloop()