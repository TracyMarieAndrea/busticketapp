import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
 
class passenger(object):

    def __init__(self, window):
        window = tk.Tk()
        window.title('Welcome')
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        def save_passenger_details():
            con = sqlite3.connect('bus_ticket_DB.db')
            c = con.cursor()
            c.execute("INSERT INTO passenger_details VALUES (:n, :ad, :cno)",
                {
                    'n':passenger_name_entry.get(),
                    'ad':address_entry.get(),
                    'cno':contact_no_entry.get()
                }
            )
            con.commit()
            con.close()
            # Entry.delete(0, END)


        #Welcome Text
        welcome_label = tk.Label(window,text="PASSENGER DETAILS",font=('Roboto', 35,'bold'),fg='black')
        welcome_label.pack(pady=15)

        #Bus No. Text
        passenger_name_label = tk.Label(window,text="Name",font=('Roboto', 12,),fg='black')
        passenger_name_label.pack(pady=10)
        # bus_no_label.place(rely=0.35,relx=0.60)

        #Bus No. Entry
        passenger_name_entry = tk.Entry(window)
        passenger_name_entry.pack(pady=5)
        # bus_no_entry.place(rely=0.40,relx=0.60,width=230,height=30)

        #Plate Number Text
        address_label = tk.Label(window,text="Address",font=('Roboto', 12,),fg='black')
        address_label.pack(pady=10)
        # password_label.place(rely=0.50,relx=0.60)

        #Plate Number Entry
        address_entry = tk.Entry(window)
        address_entry.pack(pady=5)
        # password_entry.place(rely=0.55,relx=0.60,width=230,height=30)

        #Driver Name Text
        contact_no_label = tk.Label(window,text="Contact Number",font=('Roboto', 12,),fg='black')
        contact_no_label.pack(pady=10)

        #Driver Name Entry
        contact_no_entry = tk.Entry(window)
        contact_no_entry.pack(pady=5)


        #Save and Ticket Button
        save_btn = tk.Button(window,text="T I C K E T",background="#52ACA1",border=0, command=save_passenger_details)
        save_btn.pack(pady=10)
        # save_btn.place(rely=0,relx=0,height=25,width=230)



        window.mainloop()