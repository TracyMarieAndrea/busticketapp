import tkinter as tk
import sqlite3

window = tk.Tk()

window.title("DATABASE")

con = sqlite3.connect("bus_ticket_DB.db")

c = con.cursor()

#Passenger Details table
c.execute("""CREATE TABLE passenger_details (
    passenger_name text NOT NULL,
    address text NOT NULL,
    contact_num int NOT NULL,
    Bus_ID text NOT NULL,
    Bus_Num text NOT NULL,
    Bus_Time text NOT NULL,
    Bus_Destination text NOT NULL,
    Ticket_Date text NOT NULL,
    Bus_Seating text NOT NULL
    )
    """)
#Ticketing table
c.execute("""CREATE TABLE ticket_table (
    Bus_ID text NOT NULL,
    Bus_Num text NOT NULL,
    Bus_Time text NOT NULL,
    Bus_Destination text NOT NULL,
    A1 text,
    A2 text,
    A3 text,
    A4 text,
    A5 text,
    A6 text,
    A7 text,
    A8 text,
    A9 text,
    A10 text,
    B1 text,
    B2 text,
    B3 text,
    B4 text,
    B5 text,
    B6 text,
    B7 text,
    B8 text,
    B9 text,
    B10 text
    )
    """)

# #Admin Details Table
c.execute("""CREATE TABLE admin_credentials (
    uname text NOT NULL,
    pword text NOT NULL
    )
    """)

# Insert data into admin_credentials table
admin_insert = [
    ('angelica', 'princess'),
    ('tracy', 'superman')
]

for data in admin_insert:
    c.execute("INSERT INTO admin_credentials VALUES (?, ?)", data)


#Bus Details Table
c.execute("""CREATE TABLE bus_details (
    bus_num text NOT NULL,
    plate_num text NOT NULL,
    driver_name int NOT NULL,
    contact_num int NOT NULL,
    capacity int NOT NULL,
    destination text NOT NULL
    )
    """)






con.commit()
con.close()

window.mainloop()