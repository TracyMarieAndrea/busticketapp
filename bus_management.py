import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
from bus_details_form import bus_details_form

class bus_management(object):

    def __init__(self, window):
        bus_management_window = tk.Tk()
        bus_management_window.title('Bus Management')
        width = bus_management_window.winfo_screenwidth()
        height = bus_management_window.winfo_screenheight()

        bus_management_window.geometry("%dx%d" % (width, height))


        #Functions
        def proceed_bus_management():
            show = bus_management(bus_management_window)
        def proceed_bus_details_form():
            show = bus_details_form(bus_management_window)


        #Welcome Text
        welcome_label = tk.Label(bus_management_window,text="BUS MANAGEMENT",font=('Roboto', 35,'bold'),fg='black')
        welcome_label.pack(pady=15)

       
        
        def addbus():
            show = bus_details_form(bus_management_window)

        # Buttons in one row
        button_frame = Frame(bus_management_window)
        button_frame.pack()

        add_button = tk.Button(button_frame, text="Add", command=addbus)
        add_button.pack(side=LEFT, pady=5, padx=30)

        edit_button = tk.Button(button_frame, text="Edit", command=addbus)
        edit_button.pack(side=LEFT, pady=5, padx=30)

        delete_button = tk.Button(button_frame, text="Delete", command=addbus)
        delete_button.pack(side=LEFT, pady=5, padx=30)

        con = sqlite3.connect("bus_ticket_DB.db")
        c = con.cursor()
        c.execute("SELECT * FROM bus_details")
        result = c.fetchall()

        columns = ("Bus Number", "Plate Number", "Driver Name", "Contact Number", "Capacity", "Destination")
        tree = ttk.Treeview(bus_management_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=tk.CENTER)

        for row in result:
            tree.insert("", "end", values=row)

        # vertical scrollbar
        vsb = ttk.Scrollbar(bus_management_window, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=vsb.set)

        # Pack the Treeview widget
        tree.pack(expand=True, fill="both")

        bus_management_window.mainloop()