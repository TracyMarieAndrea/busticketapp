from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
from bus_management import bus_management
from bus_details_form import bus_details_form
from passenger_details_form import passenger

class bus_seating(object):

    def __init__(self,window):

        window = tk.Tk()
        window.title('Bus Seating')

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        
        def proceed_bus_management():
            show = bus_management(window)
        def proceed_bus_details_form():
            show = bus_details_form(window)
        def proceed_passenger_form():
            show = passenger(window)

        

        frame = Frame(window)
        frame.pack()


        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]

        for seat in seatnum:
            redbutton = Button(bottomframe, text=seat, width=5,command=proceed_passenger_form)
            redbutton.pack( side = LEFT, padx=10, pady=10)

        bottomframe = Frame(window)
        bottomframe.pack()

        seatnum = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]

        for seat in seatnum:
            redbutton = Button(bottomframe, text=seat, width=5,command=proceed_passenger_form)
            redbutton.pack( side = LEFT, padx=10, pady=10)  
        

        window.mainloop()