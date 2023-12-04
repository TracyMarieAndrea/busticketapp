import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from dashboard import dashboard
import sqlite3


window = tk.Tk()
window.title('Welcome')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))


#Welcome Text
welcome_label = tk.Label(window,text="BUS MANAGEMENT",font=('Roboto', 35,'bold'),fg='black')
welcome_label.pack(pady=15)


con = sqlite3.connect("bus_ticket_DB.db")
c = con.cursor()
c.execute("SELECT * FROM bus_details")
result = c.fetchall()

columns = ("Bus Number", "Plate Number", "Driver Name", "Contact Number", "Capacity", "Destination")
tree = ttk.Treeview(window, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor=tk.CENTER)

for row in result:
    tree.insert("", "end", values=row)

# vertical scrollbar
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
vsb.pack(side="right", fill="y")
tree.configure(yscrollcommand=vsb.set)

# Pack the Treeview widget
tree.pack(expand=True, fill="both")

window.mainloop()