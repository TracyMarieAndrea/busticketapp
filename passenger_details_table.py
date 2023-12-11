import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

class passenger_table():
    def __init__(self, window):
        passenger_table_window = tk.Tk()
        passenger_table_window.title('Passenger Details Table')
        width = passenger_table_window.winfo_screenwidth()
        height = passenger_table_window.winfo_screenheight()
        passenger_table_window.configure(bg="#ACCAD2")

        passenger_table_window.geometry("%dx%d" % (width, height))

        def refresh_table():
            # Clear existing rows in the table
            for item in tree.get_children():
                tree.delete(item)

            # Fetch all records from the database
            con = sqlite3.connect("bus_ticket_DB.db")
            c = con.cursor()
            c.execute("SELECT * FROM passenger_details")
            result = c.fetchall()

            for row in result:
                tree.insert("", "end", values=row)

            # vertical scrollbar
            vsb = ttk.Scrollbar(passenger_table_window, orient="vertical", command=tree.yview)
            vsb.pack(side="right", fill="y")
            tree.configure(yscrollcommand=vsb.set)

            # Pack the Treeview widget
            tree.pack(expand=True, fill="both")
        


        #Welcome Text
        welcome_label = tk.Label(passenger_table_window,text="PASSENGERS",font=('Roboto', 35,'bold'),fg='black',bg="#ACCAD2")
        welcome_label.pack(pady=15)

        #refresh button
        button_frame = Frame(passenger_table_window,bg="#ACCAD2")
        button_frame.pack()
        refresh_button = tk.Button(button_frame, text="Refresh", command=refresh_table)
        refresh_button.pack(side=LEFT, pady=5, padx=30)


        con = sqlite3.connect("bus_ticket_DB.db")
        c = con.cursor()
        c.execute("SELECT * FROM passenger_details")
        result = c.fetchall()
                
        columns = ("Passenger Name", "Address", "Contact No.", "Bus No.", "Bus Time", "Bus Destination", "Bus Seating", "Ticket ID")
        global tree
        tree = ttk.Treeview(passenger_table_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=tk.CENTER)

        for row in result:
            tree.insert("", "end", values=row)

        # vertical scrollbar
        vsb = ttk.Scrollbar(passenger_table_window, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=vsb.set)

        # Pack the Treeview widget
        tree.pack(expand=True, fill="both")


        passenger_table_window.mainloop()
