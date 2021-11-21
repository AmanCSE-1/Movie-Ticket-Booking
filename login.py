## Importing the Libraries
from tkinter import *
import tkinter.messagebox
import sqlite3


# Importing other modules
import home
import movie



def logIn():
    logIn = Tk()
    logIn.geometry("1024x786")
    logIn.resizable(0,0)
    logIn.title("MovieZone - Movie Ticket Booking")
    #logIn.iconbitmap('path')
    global username
    
    bgColor1 = "#C7EFCF"; bgColor3= "#FE5F55"
    fgColor1 = "#EEF5DB"
    banner = LabelFrame(logIn, width=1024, height=785, bg=bgColor1, padx=70, pady=20)
    banner.place(x=0, y=0)
    
    box1 = LabelFrame(logIn, width=400, height=80, bg=bgColor3)
    box1.place(x=300, y=150)
    
    label1 = Label(box1, text="LOG IN", font=('Cambria', 26, 'bold'), fg=fgColor1, bg=bgColor3)
    label1.place(x=150, y=20)
    
    box2 = LabelFrame(logIn, width=400, height=400, bg=fgColor1)
    box2.place(x=300, y=230)
    
    Label(box2, text="Username", font=('comic', 12), fg=bgColor3).place(x=30, y=30)
    entry1 = Entry(box2, width=40, bd=3)
    entry1.place(x=32, y=63)
    
    Label(box2, text="Password", font=('comic', 12), fg=bgColor3).place(x=30, y=120)
    entry2 = Entry(box2, width=40, bd=3)
    entry2.place(x=32, y=153)
    
    
    
    #---------------------------------------------------------------#
    #-----------------Validate the user details---------------------#
    
    def validate(entry1, entry2):
        global username
        global email
        
        # Fetch the user input for username and password
        username = entry1.get()
        password = entry2.get()

        # If the field is left blank, prompt an error message
        if username=="" and password=="":
            messagebox.showerror("Movie-Zone", "Please enter Username and Password")
            
        else:
            try:
                # Connecting with the database
                connection = sqlite3.connect('assets/movieTicket.db')
                cur = connection.cursor()

                # Execute SQL statement to select entries with same username and password
                cur.execute('SELECT username, email FROM user WHERE username=? AND password=?', (username, password))
                row = cur.fetchone()
                email = row[1]
                
                # If the account credentials does not exist in the database
                if row is None:
                    tkinter.messagebox.showerror("Movie-Zone", "Incorrect Credentials")
                # Else, if the credentials are valid, redirect to movie boooking interface
                else:
                    home.createNew(logIn, movie.movie)

                # Close the connection, commit the chnages in database and close it.
                cur.close()
                connection.commit()
                connection.close()
            except:
                tkinter.messagebox.showerror("Movie-Zone", "Incorrect Credentials")
        #--------------End of Validate--------------------------------#
            
            
    LoginB = Button(box2, text="Log In", width=15, bg=bgColor3, fg=fgColor1, font=('cambria', 14), 
                    command=lambda: validate(entry1, entry2))
    LoginB.place(x=120, y=230)
    
    logIn.mainloop()
