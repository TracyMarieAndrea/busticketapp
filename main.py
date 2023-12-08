import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from dashboard import dashboard
import sqlite3


#test git Nik

window = tk.Tk()
window.title('Welcome')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))


def proceed_dashboard():
    show = dashboard(window)

#Login Function
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    con = sqlite3.connect("bus_ticket_DB.db")
    c = con.cursor()

    c.execute("SELECT * FROM admin_credentials WHERE uname=? AND pword=?", (entered_username, entered_password))
    result = c.fetchone()
    
    if result:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        proceed_dashboard()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

#Welcome Text
welcome_label = tk.Label(window,text="LOGIN",font=('Roboto', 35,'bold'),fg='black')
welcome_label.pack(pady=10)
welcome_label.place(rely=0.15,relx=0.60)

#Caption Text
caption_label = tk.Label(window,text="Please login your username and password.",font=('Roboto', 10,),fg='black')
caption_label.pack(pady=10)
caption_label.place(rely=0.25,relx=0.60)

#Username Text
username_label = tk.Label(window,text="USERNAME",font=('Roboto', 15,),fg='black')
username_label.pack(pady=10)
username_label.place(rely=0.35,relx=0.60)

#Username Entry
username_entry = tk.Entry(window)
username_entry.pack(pady=10)
username_entry.place(rely=0.40,relx=0.60,width=230,height=30)

#Password Text
password_label = tk.Label(window,text="PASSWORD",font=('Roboto', 15,),fg='black')
password_label.pack(pady=10)
password_label.place(rely=0.50,relx=0.60)

#Password Entry
password_entry = tk.Entry(window)
password_entry.pack(pady=10)
password_entry.place(rely=0.55,relx=0.60,width=230,height=30)

#Login Button
login_btn = tk.Button(text="LOGIN",background="#52ACA1",border=0,command=login)
login_btn.pack(pady=10)
login_btn.place(rely=0.70,relx=0.60,height=25,width=230)

#Create a canvas
canvas= Canvas(window, width= 600, height= 600)
canvas.pack()
canvas.place(rely=0.15,relx=0.10)

#Load an image in the script
img= (Image.open("ticket.png"))

#Resize the Image using resize method
resized_image= img.resize((400,500))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
img = canvas.create_image(10,10, anchor=NW, image=new_image)

window.mainloop()