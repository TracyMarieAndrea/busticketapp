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
        bus_management_window.configure(bg="#ACCAD2")

        bus_management_window.geometry("%dx%d" % (width, height))


        #Functions
        def proceed_bus_management():
            show = bus_management(bus_management_window)
        def proceed_bus_details_form():
            show = bus_details_form(bus_management_window)
        def delete_record():
        # Check if a row is selected in the Treeview
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning(bus_management_window,"Warning", "Please select a record to delete.")
                return

            # Get the values of the selected row
            values = tree.item(selected_item)['values']

            # Delete the selected row from the Treeview
            tree.delete(selected_item)

            # Create a database or connect to one that exists
            conn = sqlite3.connect('bus_ticket_DB.db')

            # Create a cursor instance
            c = conn.cursor()

            try:
                # Delete From Database using values from the selected row
                c.execute("DELETE FROM bus_details WHERE plate_num=?", (values[1],))
                
                # Commit changes
                conn.commit()

                # Add a little message box for fun
                messagebox.showinfo(bus_management_window,"Deleted!", "Bus Record Has Been Deleted!")

            except Exception as e:
                # If an error occurs, rollback the changes and show an error message
                conn.rollback()
                messagebox.showerror(bus_management_window,"Error", f"Error deleting record: {str(e)}")

            finally:
                # Close our connection
                conn.close()

       
        def refresh_table():
            # Clear existing rows in the table
            for item in tree.get_children():
                tree.delete(item)

            # Fetch all records from the database
            con = sqlite3.connect("bus_ticket_DB.db")
            c = con.cursor()
            c.execute("SELECT * FROM bus_details")
            result = c.fetchall()

            for row in result:
                tree.insert("", "end", values=row)

         
            # Pack the Treeview widget
            tree.pack(expand=True, fill="both")
        


        #Welcome Text
        welcome_label = tk.Label(bus_management_window,text="BUS MANAGEMENT",font=('Roboto', 35,'bold'),fg='black',bg="#ACCAD2")
        welcome_label.pack(pady=15)

       
        
        def addbus():
            show = bus_details_form(bus_management_window)

        # Buttons in one row
        button_frame = Frame(bus_management_window,bg="#ACCAD2")
        button_frame.pack()

        add_button = tk.Button(button_frame, text="Add", command=addbus)
        add_button.pack(side=LEFT, pady=5, padx=30)

        edit_button = tk.Button(button_frame, text="Edit", command=addbus)
        edit_button.pack(side=LEFT, pady=5, padx=30)

        delete_button = tk.Button(button_frame, text="Delete", command=delete_record)
        delete_button.pack(side=LEFT, pady=5, padx=30)

        refresh_button = tk.Button(button_frame, text="Refresh", command=refresh_table)
        refresh_button.pack(side=LEFT, pady=5, padx=30)

        con = sqlite3.connect("bus_ticket_DB.db")
        c = con.cursor()
        c.execute("SELECT * FROM bus_details")
        result = c.fetchall()
        
        columns = ("Bus Number", "Plate Number", "Driver Name", "Contact Number", "Capacity", "Destination", "Schedule")
        global tree
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