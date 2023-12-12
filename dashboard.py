from tkinter import *
from tkinter import messagebox
import tkinter as tk
from bus_management import bus_management
from bus_details_form import bus_details_form
from bus_seating import bus_seating
import sqlite3
from passenger_details_table import passenger_table
from ticket_table import ticket_table
from tkinter import ttk
from PIL import Image, ImageTk

class dashboard(object):

    def __init__(self,window):

        dashboard_window = tk.Toplevel()
        dashboard_window.title('Dashboard')


        width = dashboard_window.winfo_screenwidth()
        height = dashboard_window.winfo_screenheight()

        dashboard_window.geometry("%dx%d" % (width, height))  

        
        def proceed_bus_management():
            show = bus_management(dashboard_window)
        def proceed_bus_details_form():
            show = bus_details_form(dashboard_window)
        def proceed_bus_seating(location,time,busno):
            #confirmation = messagebox.askyesno("Confirmation", f"Selected Location: {location}\nTime: {time}\nProceed to Bus Seating?")
            show = bus_seating(dashboard_window, location, time,busno)
        def proceed_passenger_table():
            show = passenger_table(dashboard_window)
        def proceed_ticket_table():
            show = ticket_table(dashboard_window)
        def logout():
            dashboard_window.destroy()
        def refresh():
            for widget in dashboard_window.winfo_children():
                if isinstance(widget,Frame):
                    widget.destroy()
            con = sqlite3.connect('bus_ticket_DB.db')
            c = con.cursor()  

            menubar = Menu(dashboard_window)
            dashboard_window.config(menu=menubar)

            # create a menu
            bus_menu = Menu(menubar, tearoff=False)
            passenger_menu = Menu(menubar, tearoff=False)
            ticket_menu = Menu(menubar, tearoff=False)

            # add a menu item to the menu
            bus_menu.add_command(
                label='Bus Management',
                command=proceed_bus_management
            )
            passenger_menu.add_command(
                label='Passenger Table',
                command=proceed_passenger_table
            )
            ticket_menu.add_command(
                label='Ticket Table',
                command=proceed_ticket_table
            )

            # add the File menu to the menubar
            menubar.add_cascade(
                label="Bus",
                menu=bus_menu
            )
            menubar.add_cascade(
                label="Passenger",
                menu=passenger_menu
            )
            menubar.add_cascade(
                label="Ticket",
                menu=ticket_menu
            )

            logo_frame = Frame(dashboard_window)
            logo_frame.pack()
            
            img = Image.open("Busbly.png")
            resized_image = img.resize((300, 100))
            self.new_image = ImageTk.PhotoImage(resized_image)

            # Create a label to display the image
            image_label = tk.Label(logo_frame, image=self.new_image) 
            image_label.pack(side="left")

            location_frame = Frame(dashboard_window)
            location_frame.pack()
            
            labels = [
                ("CATICLAN", 'black', 12),
                ("KALIBO", 'black', 12),
                ("ANTIQUE", 'black', 12),
                ("CAPIZ", 'black', 12)
            ]

            for text, color, width in labels:
                label = tk.Label(location_frame, text=text, font=('Roboto', 25, 'bold'), fg=color, width=width)
                label.pack(side=LEFT, padx=50, pady=10)

            refresh_bottomframe = Frame(dashboard_window)
            refresh_bottomframe.pack()

            refresh_btn = tk.Button(refresh_bottomframe,text='Refresh',command=refresh)
            refresh_btn.pack(side = LEFT, padx=10, pady=10)

            logout_btn = tk.Button(refresh_bottomframe,text='Logout',command=logout)
            logout_btn.pack(side = LEFT, padx=10, pady=10)

            

            caticlan_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
            caticlan_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

            c.execute("SELECT * FROM bus_details WHERE destination = 'Caticlan'")
            results_caticlan = c.fetchall()

            if results_caticlan:
                for result in results_caticlan:
                    caticlan_bus_button = Button(caticlan_bottomframe,font=('Roboto', 12), text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1], bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                    caticlan_bus_button.pack(padx=10, pady=10)
            

            kalibo_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
            kalibo_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

            c.execute("SELECT * FROM bus_details WHERE destination = 'Kalibo'")
            results_kalibo = c.fetchall()

            if results_kalibo:
                for result in results_kalibo:
                    kalibo_bus_button = Button(kalibo_bottomframe,font=('Roboto', 12),  text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                    kalibo_bus_button.pack(padx=10, pady=10)

            antique_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
            antique_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)


            c.execute("SELECT * FROM bus_details WHERE destination = 'Antique'")
            results_antique = c.fetchall()

            if results_antique:
                for result in results_antique:
                    antique_bus_button = Button(antique_bottomframe,font=('Roboto', 12),  text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                    antique_bus_button.pack(padx=10, pady=10)


            capiz_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
            capiz_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

            c.execute("SELECT * FROM bus_details WHERE destination = 'Capiz'")
            results_capiz = c.fetchall()

            if results_capiz:
                for result in results_capiz:
                    capiz_bus_button = Button(capiz_bottomframe,font=('Roboto', 12),  text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                    capiz_bus_button.pack(padx=10, pady=10)
        

            con.close()
            dashboard_window.update()
                
      
        
            
        con = sqlite3.connect('bus_ticket_DB.db')
        c = con.cursor()  



        menubar = Menu(dashboard_window)
        dashboard_window.config(menu=menubar)

        # create a menu
        bus_menu = Menu(menubar, tearoff=False)
        passenger_menu = Menu(menubar, tearoff=False)
        ticket_menu = Menu(menubar, tearoff=False)

        # add a menu item to the menu
        bus_menu.add_command(
            label='Bus Management',
            command=proceed_bus_management
        )
        passenger_menu.add_command(
            label='Passenger Table',
            command=proceed_passenger_table
        )
        ticket_menu.add_command(
            label='Ticket Table',
            command=proceed_ticket_table
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="Bus",
            menu=bus_menu
        )
        menubar.add_cascade(
            label="Passenger",
            menu=passenger_menu
        )
        menubar.add_cascade(
            label="Ticket",
            menu=ticket_menu
        )

        logo_frame = Frame(dashboard_window)
        logo_frame.pack()
            
        img = Image.open("Busbly.png")
        resized_image = img.resize((300, 100))
        self.new_image = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(logo_frame, image=self.new_image) 
        image_label.pack()


        location_frame = Frame(dashboard_window)
        location_frame.pack()
        
        labels = [
            ("CATICLAN", 'black', 12),
            ("KALIBO", 'black', 12),
            ("ANTIQUE", 'black', 12),
            ("CAPIZ", 'black', 12)
        ]

        for text, color, width in labels:
            label = tk.Label(location_frame, text=text, font=('Roboto', 25, 'bold'), fg=color, width=width)
            label.pack(side=LEFT, padx=50, pady=10)

        refresh_bottomframe = Frame(dashboard_window)
        refresh_bottomframe.pack()

        refresh_btn = tk.Button(refresh_bottomframe,text='Refresh',command=refresh)
        refresh_btn.pack(side = LEFT, padx=10, pady=10)

        logout_btn = tk.Button(refresh_bottomframe,text='Logout',command=logout)
        logout_btn.pack(side = LEFT, padx=10, pady=10)

        
        caticlan_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
        caticlan_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)
        
        frameScrollbar = Scrollbar(caticlan_bottomframe,orient="vertical")
        frameScrollbar.pack(side="right",fill='y')

        c.execute("SELECT * FROM bus_details WHERE destination = 'Caticlan'")
        results_caticlan = c.fetchall()

        if results_caticlan:
            for result in results_caticlan:
                caticlan_bus_button = Button(caticlan_bottomframe,font=('Roboto', 12), text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1], bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                caticlan_bus_button.pack(padx=10, pady=10)
        

        kalibo_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
        kalibo_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        c.execute("SELECT * FROM bus_details WHERE destination = 'Kalibo'")
        results_kalibo = c.fetchall()

        if results_kalibo:
            for result in results_kalibo:
                kalibo_bus_button = Button(kalibo_bottomframe,font=('Roboto', 12),  text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                kalibo_bus_button.pack(padx=10, pady=10)

        antique_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
        antique_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)


        c.execute("SELECT * FROM bus_details WHERE destination = 'Antique'")
        results_antique = c.fetchall()

        if results_antique:
            for result in results_antique:
                antique_bus_button = Button(antique_bottomframe,font=('Roboto', 12),  text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                antique_bus_button.pack(padx=10, pady=10)


        capiz_bottomframe = Frame(dashboard_window, bg="#ACCAD2")
        capiz_bottomframe.pack(expand=True, fill='both', padx=10, pady=10, side=LEFT)

        c.execute("SELECT * FROM bus_details WHERE destination = 'Capiz'")
        results_capiz = c.fetchall()

        if results_capiz:
            for result in results_capiz:
                capiz_bus_button = Button(capiz_bottomframe,font=('Roboto', 12),  text=result[1] + " - " +result[6], bg="#F5CB83", width=30, height=3, command=lambda busno=result[1],bustime=result[6], busname=result[5]: proceed_bus_seating(busname,bustime,busno))
                capiz_bus_button.pack(padx=10, pady=10)
    

        con.close()
        dashboard_window.mainloop()