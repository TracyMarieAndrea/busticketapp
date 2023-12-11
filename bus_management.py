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

        def edit_record():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a record to edit.")
                return

            values = tree.item(selected_item)['values']

            # Create a new window for editing
            edit_window = Toplevel(bus_management_window)
            edit_window.title('Edit Bus Record')
            width = bus_management_window.winfo_screenwidth() // 2
            height = edit_window.winfo_screenheight() // 2
            edit_window.geometry("%dx%d" % (width, height))
            edit_window.configure(bg="#ACCAD2")

            edit_frame = Frame(edit_window, bg="#ACCAD2")
            edit_frame.pack(expand=True)

            entry_widgets = []
            for col, value in zip(columns, values):
                label = Label(edit_frame, text=f"{col}:", font=('Roboto', 12, 'bold'), bg="#ACCAD2")
                label.grid(row=len(entry_widgets), column=0, padx=5, pady=5, sticky='e')

                entry = Entry(edit_frame)
                entry.insert(0, value)
                entry.grid(row=len(entry_widgets), column=1, padx=5, pady=5, sticky='w')

                entry_widgets.append(entry)

            # Function to save changes
            def save_changes():
                new_values = [entry.get() for entry in entry_widgets]
                tree.item(selected_item, values=new_values)
                
                conn = sqlite3.connect('bus_ticket_DB.db')
                c = conn.cursor()

                try:
                    c.execute("UPDATE bus_details SET bus_num=?, plate_num=?, driver_name=?, contact_num=?, capacity=?, destination=?, schedule=? WHERE plate_num=?", (new_values[0], new_values[1], new_values[2], new_values[3], new_values[4], new_values[5], new_values[6], values[1]))
                    conn.commit()

                except Exception as e:
                    conn.rollback()
                    messagebox.showerror(edit_window, "Error", f"Error updating record: {str(e)}")

                finally:
                    conn.close()

                edit_window.destroy()

            # Save button
            save_button = Button(edit_frame, font=('Roboto', 12, 'bold'), text="U P D A T E", command=save_changes)
            save_button.grid(row=len(entry_widgets), columnspan=2, pady=10)

        
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
            add_window = Toplevel(bus_management_window)
            add_window.title('Add Bus Record')
            width = bus_management_window.winfo_screenwidth() // 2
            height = add_window.winfo_screenheight() // 2
            add_window.geometry("%dx%d" % (width, height))
            add_window.configure(bg="#ACCAD2")

            add_frame = Frame(add_window, bg="#ACCAD2")
            add_frame.pack(expand=True)

            entry_widgets = []

            def save_changes():
                new_values = [entry.get() for entry in entry_widgets]
                tree.insert("", "end", values=new_values)

                conn = sqlite3.connect('bus_ticket_DB.db')
                c = conn.cursor()

                try:
                    c.execute("INSERT INTO bus_details VALUES (?, ?, ?, ?, ?, ?, ?)", tuple(new_values))
                    conn.commit()

                except Exception as e:
                    conn.rollback()
                    messagebox.showerror(add_window, "Error", f"Error adding record: {str(e)}")

                finally:
                    conn.close()

                add_window.destroy()

            columns = ("Bus Number", "Plate Number", "Driver Name", "Contact Number", "Capacity", "Destination", "Schedule")

            for col in columns:                
                label = Label(add_frame, text=f"{col}:", font=('Roboto', 12, 'bold'), bg="#ACCAD2")
                label.grid(row=len(entry_widgets), column=0, padx=5, pady=5, sticky='e')

                entry = Entry(add_frame)
                entry.grid(row=len(entry_widgets), column=1, padx=5, pady=5, sticky='w')

                entry_widgets.append(entry)

            # Save button
            save_button = Button(add_frame, font=('Roboto', 12, 'bold'), text="A D D", command=save_changes)
            save_button.grid(row=len(entry_widgets), columnspan=2, pady=10)



        # Buttons in one row
        button_frame = Frame(bus_management_window,bg="#ACCAD2")
        button_frame.pack()

        add_button = tk.Button(button_frame, text="Add", command=addbus)
        add_button.pack(side=LEFT, pady=5, padx=30)

        edit_button = tk.Button(button_frame, text="Edit", command=edit_record)
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