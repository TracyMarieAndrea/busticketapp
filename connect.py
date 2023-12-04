import tkinter as tk
import sqlite3

window = tk.Tk()

window.title("DATABASE")

con = sqlite3.connect("bus_ticket_DB.db")

c = con.cursor()

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

#Passenger Details table
c.execute("""CREATE TABLE passenger_details (
    passenger_name text NOT NULL,
    address text NOT NULL,
    contact_num int NOT NULL
    )
    """)

con.commit()
con.close()

window.mainloop()