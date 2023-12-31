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
        window = tk.Toplevel()
        window.title('Bus Seating')

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.configure(bg="#ACCAD2")
        window.geometry("%dx%d" % (width, height))

        
        def proceed_bus_management():
            show = bus_management(window)
        def proceed_bus_details_form():
            show = bus_details_form(window)
        def proceed_passenger_form(s,l,t,b):
            show = passenger(window,s,l,t,b)

        frame = Frame(window,bg="#ACCAD2")
        frame.pack()
        
        none_label = tk.Label(window,text="",font=('Roboto', 25,'bold'),fg='black',bg="#ACCAD2")
        none_label.pack()

        #bus_label_location = tk.Label(destination_frame,text="Destination: ",font=('Roboto', 12, 'bold'),fg='black')
        #bus_label_location.pack(side=tk.LEFT, pady=3)
        #location_label = tk.Label(window,text=location,font=('Roboto', 35,'bold'),fg='black',bg="#ACCAD2")
        #location_label.pack()

        destination_frame = Frame(window,bg="#ACCAD2")
        destination_frame.pack()

        bus_label_location = tk.Label(destination_frame,text="Destination: ",font=('Roboto', 20, 'bold'),fg='black',bg="#ACCAD2")
        bus_label_location.pack(side=tk.LEFT, pady=3)
        bus_location = tk.Label(destination_frame,text=location,font=('Roboto', 20,),fg='black',bg="#ACCAD2")
        bus_location.pack(side=tk.LEFT, pady=10)




        #time_label = tk.Label(window,text=time,font=('Roboto', 25,'bold'),fg='black',bg="#ACCAD2")
        #time_label.pack()

        time_frame = Frame(window,bg="#ACCAD2")
        time_frame.pack()

        bus_label_time = tk.Label(time_frame,text="Time: ",font=('Roboto', 20,'bold'),fg='black',bg="#ACCAD2")
        bus_label_time.pack(side=tk.LEFT, pady=3)
        bus_time = tk.Label(time_frame,text=time,font=('Roboto', 20,),fg='black',bg="#ACCAD2")
        bus_time.pack(side=tk.LEFT, pady=10)


        #busno_label = tk.Label(window,text=busno,font=('Roboto', 25,'bold'),fg='black',bg="#ACCAD2")
        #busno_label.pack()

        plateNo_frame = Frame(window,bg="#ACCAD2")
        plateNo_frame.pack()

        bus_label_no = tk.Label(plateNo_frame,text="Plate No.: ",font=('Roboto', 20,'bold'),fg='black',bg="#ACCAD2")
        bus_label_no.pack(side=tk.LEFT, pady=3)
        bus_no = tk.Label(plateNo_frame,text=busno,font=('Roboto', 20,),fg='black',bg="#ACCAD2")
        bus_no.pack(pady=10)

        bottomframe = Frame(window,bg="#ACCAD2")
        bottomframe.pack()

        seatnum_A = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_A in seatnum_A:
            
            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_A))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"
            
            if(button_color == "#49A64C"):
                A_button = Button(bottomframe, bg=button_color, fg="white", text=seat_A, width=5,command=lambda s=seat_A: proceed_passenger_form(s, location, time,busno))
            else:
                A_button = Button(bottomframe, bg=button_color, fg="white", text=seat_A, width=5)
            A_button.pack( side = LEFT, padx=10, pady=10)



        con.close()
        bottomframe = Frame(window,bg="#ACCAD2")
        bottomframe.pack()

        seatnum_B = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_B in seatnum_B:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_B))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"

            if(button_color == "#49A64C"):
                B_button = Button(bottomframe, bg=button_color, fg="white", text=seat_B, width=5,command=lambda s=seat_B: proceed_passenger_form(s, location, time,busno))
            else:
                B_button = Button(bottomframe, bg=button_color, fg="white", text=seat_B, width=5)
            B_button.pack( side = LEFT, padx=10, pady=10)  
        con.close()


        bottomframe = Frame(window,bg="#ACCAD2")
        bottomframe.pack()

        seatnum_C = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_C in seatnum_C:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_C))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"

            if(button_color == "#49A64C"):
                C_button = Button(bottomframe, bg=button_color, fg="white", text=seat_C, width=5,command=lambda s=seat_C: proceed_passenger_form(s, location, time,busno))
            else:
                C_button = Button(bottomframe, bg=button_color, fg="white", text=seat_C, width=5)
            C_button.pack( side = LEFT, padx=10, pady=10)  
        con.close()


        bottomframe = Frame(window,bg="#ACCAD2")
        bottomframe.pack()

        seatnum_D = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]


        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()

        for seat_D in seatnum_D:

            c.execute("SELECT Bus_Seating FROM ticket_table WHERE Bus_Destination = ? AND Bus_Time = ? AND Bus_Seating = ?",
                      (location, time, seat_D))
            result = c.fetchone()

            button_color = "#49A64C" if result is None else "#DD0A0A"

            if(button_color == "#49A64C" ):
                D_button = Button(bottomframe, bg=button_color, fg="white", text=seat_D, width=5,command=lambda s=seat_D: proceed_passenger_form(s, location, time,busno))
            else:
                D_button = Button(bottomframe, bg=button_color, fg="white", text=seat_D, width=5)
            D_button.pack( side = LEFT, padx=10, pady=10)  
        con.close()

        img = Image.open("bus.png")
        resized_image = img.resize((600, 250))
        self.new_image = ImageTk.PhotoImage(resized_image)

        # Create a label to display the image
        image_label = tk.Label(window, image=self.new_image) 
        image_label.pack()

        
        window.mainloop()