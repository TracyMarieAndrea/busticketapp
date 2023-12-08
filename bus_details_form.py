import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

class bus_details_form(object):
    def __init__(self, window):
        window = tk.Tk()
        window.title('Add Bus')
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        window.geometry("%dx%d" % (width, height))

        def save_bus_details():
            con = sqlite3.connect('bus_ticket_DB.db')
            c = con.cursor()
            c.execute("INSERT INTO bus_details VALUES (:bn, :pn, :dn, :cn, :cp, :d)",
                {
                    'bn':bus_num_entry.get(),
                    'pn':plate_num_entry.get(),
                    'dn':driver_name_entry.get(),
                    'cn':contact_num_entry.get(),
                    'cp':capacity_entry.get(),
                    'd':destination_entry.get()
                }
            )
            con.commit()
            con.close()


        #Welcome Text
        welcome_label = tk.Label(window,text="INPUT BUS DETAILS",font=('Roboto', 35,'bold'),fg='black')
        welcome_label.pack(pady=15)

        #Bus No. Text
        bus_num_label = tk.Label(window,text="Bus Number",font=('Roboto', 12,),fg='black')
        bus_num_label.pack(pady=10)
        # bus_no_label.place(rely=0.35,relx=0.60)

        #Bus No. Entry
        bus_num_entry = tk.Entry(window)
        bus_num_entry.pack(pady=5)
        # bus_no_entry.place(rely=0.40,relx=0.60,width=230,height=30)

        #Plate Number Text
        plate_num_label = tk.Label(window,text="Plate Number",font=('Roboto', 12,),fg='black')
        plate_num_label.pack(pady=10)
        # password_label.place(rely=0.50,relx=0.60)

        #Plate Number Entry
        plate_num_entry = tk.Entry(window)
        plate_num_entry.pack(pady=5)
        # password_entry.place(rely=0.55,relx=0.60,width=230,height=30)

        #Driver Name Text
        driver_name_label = tk.Label(window,text="Driver Name",font=('Roboto', 12,),fg='black')
        driver_name_label.pack(pady=10)

        #Driver Name Entry
        driver_name_entry = tk.Entry(window)
        driver_name_entry.pack(pady=5)

        #Contact Number Text
        contact_num_label = tk.Label(window,text="Contact Number",font=('Roboto', 12,),fg='black')
        contact_num_label.pack(pady=10)

        #Contact Number Entry
        contact_num_entry = tk.Entry(window)
        contact_num_entry.pack(pady=5)

        #Capacity Text
        capacity_label = tk.Label(window,text="Capacity",font=('Roboto', 12,),fg='black')
        capacity_label.pack(pady=10)
        # password_label.place(rely=0.50,relx=0.60)

        #Capacity Entry
        capacity_entry = tk.Entry(window)
        capacity_entry.pack(pady=5)


        #Destination Text
        destination_label = tk.Label(window,text="Destination",font=('Roboto', 12,),fg='black')
        destination_label.pack(pady=10)

        #Destination Entry
        destination_entry = tk.Entry(window)
        destination_entry.pack(pady=5)

        #Save Button
        save_btn = tk.Button(window, text="S A V E",background="#52ACA1",border=0, command=save_bus_details)
        save_btn.pack(pady=10)
        # save_btn.place(rely=0,relx=0,height=25,width=230)



        window.mainloop()