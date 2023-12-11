import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

class ticket_table():
    def __init__(self, window):
        ticket_window = tk.Tk()
        ticket_window.title('Ticket Table')
        width = ticket_window.winfo_screenwidth()
        height = ticket_window.winfo_screenheight()
        ticket_window.configure(bg="#ACCAD2")

        ticket_window.geometry("%dx%d" % (width, height))

        def refresh_table():
            # Clear existing rows in the table
            for item in tree.get_children():
                tree.delete(item)

            # Fetch all records from the database
            con = sqlite3.connect("bus_ticket_DB.db")
            c = con.cursor()
            c.execute("SELECT * FROM ticket_table")
            result = c.fetchall()

            for row in result:
                tree.insert("", "end", values=row)

            # vertical scrollbar
            vsb = ttk.Scrollbar(ticket_window, orient="vertical", command=tree.yview)
            vsb.pack(side="right", fill="y")
            tree.configure(yscrollcommand=vsb.set)

            # Pack the Treeview widget
            tree.pack(expand=True, fill="both")
        


        #Welcome Text
        welcome_label = tk.Label(ticket_window,text="TICKETS",font=('Roboto', 35,'bold'),fg='black',bg="#ACCAD2")
        welcome_label.pack(pady=15)

        #refresh button
        button_frame = Frame(ticket_window,bg="#ACCAD2")
        button_frame.pack()
        refresh_button = tk.Button(button_frame, text="Refresh", command=refresh_table)
        refresh_button.pack(side=LEFT, pady=5, padx=30)


        con = sqlite3.connect("bus_ticket_DB.db")
        c = con.cursor()
        c.execute("SELECT * FROM ticket_table")
        result = c.fetchall()
                
        columns = ("Bus ID", "Bus Time", "Bus Destination", "Bus Seating", "Passenger Name", "Bus No.")
        global tree
        tree = ttk.Treeview(ticket_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=tk.CENTER)

        for row in result:
            tree.insert("", "end", values=row)

        # vertical scrollbar
        vsb = ttk.Scrollbar(ticket_window, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=vsb.set)

        # Pack the Treeview widget
        tree.pack(expand=True, fill="both")


        ticket_window.mainloop()
