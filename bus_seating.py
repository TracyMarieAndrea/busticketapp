from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form
from passenger_details_form import passenger
import sqlite3

class bus_seating(object):

    def __init__(self,window, location, time,busno):
        window = tk.Tk()
        window.title('Bus Seating')

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        
        def proceed_bus_management():
            show = bus_management(window)
        def proceed_bus_details_form():
            show = bus_details_form(window)
        def proceed_passenger_form(s,l,t,b):
            show = passenger(window,s,l,t,b)

        frame = Frame(window)
        frame.pack()

        location_label = tk.Label(window,text=location,font=('Roboto', 35,'bold'),fg='black')
        location_label.pack()
        time_label = tk.Label(window,text=time,font=('Roboto', 25,'bold'),fg='black')
        time_label.pack()
        busno_label = tk.Label(window,text=busno,font=('Roboto', 25,'bold'),fg='black')
        busno_label.pack()


        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum_A = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_A in seatnum_A:
            
            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_A))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"
            
            if(button_color == "green"):
                A_button = Button(bottomframe, bg=button_color, fg="white", text=seat_A, width=5,command=lambda s=seat_A: proceed_passenger_form(s, location, time,busno))
            else:
                A_button = Button(bottomframe, bg=button_color, fg="white", text=seat_A, width=5)
            A_button.pack( side = LEFT, padx=10, pady=10)



        con.close()
        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum_B = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_B in seatnum_B:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_B))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"

            if(button_color == "green"):
                B_button = Button(bottomframe, bg=button_color, fg="white", text=seat_B, width=5,command=lambda s=seat_B: proceed_passenger_form(s, location, time,busno))
            else:
                B_button = Button(bottomframe, bg=button_color, fg="white", text=seat_B, width=5)
            B_button.pack( side = LEFT, padx=10, pady=10)  
        con.close()


        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum_C = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_C in seatnum_C:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_C))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"

            if(button_color == "green"):
                C_button = Button(bottomframe, bg=button_color, fg="white", text=seat_C, width=5,command=lambda s=seat_C: proceed_passenger_form(s, location, time,busno))
            else:
                C_button = Button(bottomframe, bg=button_color, fg="white", text=seat_C, width=5)
            C_button.pack( side = LEFT, padx=10, pady=10)  
        con.close()


        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum_D = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_D in seatnum_D:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_D))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"

            if(button_color == "green"):
                D_button = Button(bottomframe, bg=button_color, fg="white", text=seat_D, width=5,command=lambda s=seat_D: proceed_passenger_form(s, location, time,busno))
            else:
                D_button = Button(bottomframe, bg=button_color, fg="white", text=seat_D, width=5)
            D_button.pack( side = LEFT, padx=10, pady=10)  
        con.close()

        window.mainloop()