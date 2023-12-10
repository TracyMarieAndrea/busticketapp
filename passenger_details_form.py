import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
from datetime import datetime

 
class passenger(object):

    def __init__(self, window, s, l, t,b):
        passenger_window = tk.Tk()
        passenger_window.title('Add Passenger')
        width = passenger_window.winfo_screenwidth()
        height = passenger_window.winfo_screenheight()

        passenger_window.geometry("%dx%d" % (width, height))

        from dashboard import dashboard
        def go_back():
            passenger_window.destroy()  # Close the current window
            dashboard(window) 

        def save_passenger_details():
            con = sqlite3.connect('bus_ticket_DB.db')
            c = con.cursor()

            current_date = datetime.now().strftime('%Y%m%d')

            c.execute("SELECT MAX(CAST(SUBSTR(Ticket_ID, 9) AS INTEGER)) FROM passenger_details")
            max_id = c.fetchone()[0]

            if max_id is None:
                max_id = 0

            max_id += 1

            ticket_id = f'{current_date}{max_id:04d}'


    #Ticket_Date text NOT NULL,
    
            try:
                # Insert into passenger_details table
                c.execute("INSERT INTO passenger_details (passenger_name, address, contact_num,Bus_Num,Bus_Time,Bus_Destination,Bus_Seating,Ticket_ID) VALUES (:n, :ad, :cno, :bn, :bt, :bl, :bs,:ti)",
                        {
                            'n': passenger_name_entry.get(),
                            'ad': address_entry.get(),
                            'cno': contact_no_entry.get(),
                            'bn':b,
                            'bt':t,
                            'bl':l,
                            'bs':s,
                            'ti':ticket_id

                        })
                con.commit()

                # Insert into ticket_table table
                c.execute("INSERT INTO ticket_table (Bus_ID,Bus_Time, Bus_Destination, Bus_Seating, Passenger_Name,Bus_Num) VALUES (:bi,:bt, :bd, :bs, :pn,:bn)",
                        {
                            'bi':ticket_id,
                            'bt': t,
                            'bd': l,
                            'bs': s,
                            'bn' :b,
                            'pn': passenger_name_entry.get()
                            
                        })
                con.commit()

                messagebox.showinfo(title="Saved", message="Data Saved!")
                go_back()

            except Exception as e:
                messagebox.showerror(title="Error", message=f"Error saving data: {e}")

            finally:
                con.close()


        #Welcome Text
        welcome_label = tk.Label(passenger_window,text="PASSENGER DETAILS",font=('Roboto', 35,'bold'),fg='black')
        welcome_label.pack(pady=15)

        bus_location = tk.Label(passenger_window,text=l,font=('Roboto', 12,),fg='black')
        bus_location.pack(pady=10)

        bus_time = tk.Label(passenger_window,text=t,font=('Roboto', 12,),fg='black')
        bus_time.pack(pady=10)

        bus_seat = tk.Label(passenger_window,text=s,font=('Roboto', 12,),fg='black')
        bus_seat.pack(pady=10)

        bus_no = tk.Label(passenger_window,text=b,font=('Roboto', 12,),fg='black')
        bus_no.pack(pady=10)

        #Bus No. Text
        passenger_name_label = tk.Label(passenger_window,text="Name",font=('Roboto', 12,),fg='black')
        passenger_name_label.pack(pady=10)
        # bus_no_label.place(rely=0.35,relx=0.60)

        #Bus No. Entry
        passenger_name_entry = tk.Entry(passenger_window)
        passenger_name_entry.pack(pady=5)
        # bus_no_entry.place(rely=0.40,relx=0.60,width=230,height=30)

        #Plate Number Text
        address_label = tk.Label(passenger_window,text="Address",font=('Roboto', 12,),fg='black')
        address_label.pack(pady=10)
        # password_label.place(rely=0.50,relx=0.60)

        #Plate Number Entry
        address_entry = tk.Entry(passenger_window)
        address_entry.pack(pady=5)
        # password_entry.place(rely=0.55,relx=0.60,width=230,height=30)

        #Driver Name Text
        contact_no_label = tk.Label(passenger_window,text="Contact Number",font=('Roboto', 12,),fg='black')
        contact_no_label.pack(pady=10)

        #Driver Name Entry
        contact_no_entry = tk.Entry(passenger_window)
        contact_no_entry.pack(pady=5)


        #Save and Ticket Button
        save_btn = tk.Button(passenger_window,text="T I C K E T",background="#52ACA1",border=0, command=save_passenger_details)
        save_btn.pack(pady=10)
        # save_btn.place(rely=0,relx=0,height=25,width=230)



        passenger_window.mainloop()