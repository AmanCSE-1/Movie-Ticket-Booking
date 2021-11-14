# Importing the Libraries
from tkinter import *
import tkinter.messagebox
import sqlite3


# Importing other modules
import home
import login



def signUp():
    signUp = Tk()
    signUp.geometry("1024x786")
    signUp.resizable(0,0)
    signUp.title("MovieZone - Movie Ticket Booking")
    
    bgColor1 = "#C7EFCF"; bgColor3= "#FE5F55"
    fgColor1 = "#EEF5DB"
    banner = LabelFrame(signUp, width=1024, height=785, bg=bgColor1, padx=70, pady=20)
    banner.place(x=0, y=0)
    
    box1 = LabelFrame(signUp, width=500, height=80, bg=bgColor3)
    box1.place(x=300, y=100)
    
    label1 = Label(box1, text="SIGN UP", font=('Cambria', 26, 'bold'), fg=fgColor1, bg=bgColor3)
    label1.place(x=180, y=20)
    
    box2 = LabelFrame(signUp, width=500, height=480, bg=fgColor1)
    box2.place(x=300, y=180)
    
    Label(box2, text="Username", font=('comic', 12), fg=bgColor3).place(x=70, y=30)
    entry1 = Entry(box2, width=40, bd=3)
    entry1.place(x=70, y=55)
    
    Label(box2, text="Password", font=('comic', 12), fg=bgColor3).place(x=70, y=120)
    entry2 = Entry(box2, width=40, bd=3)
    entry2.place(x=70, y=145)
    
    Label(box2, text="Email", font=('comic', 12), fg=bgColor3).place(x=70, y=210)
    entry3 = Entry(box2, width=40, bd=3)
    entry3.place(x=70, y=235)
    
    Label(box2, text="Age", font=('comic', 12), fg=bgColor3).place(x=70,y=290)
    entry4 = Entry(box2, width=10, bd=3)
    entry4.place(x=70, y=315)
    
    def insert(entry1, entry2, entry3, entry4):
        username = entry1.get()
        password = entry2.get()
        email = entry3.get()
        age = entry4.get()

        if username=="":
            messagebox.showerror("Movie-Zone", "Username cannot be blank")
        elif password=="":
            messagebox.showerror("Movie-Zone", "Password cannot be blank")
        elif email=="":
            messagebox.showerror("Movie-Zone", "Email cannot be blank")
        elif age=="":
            messagebox.showerror("Movie-Zone", "Age cannot be blank")
        else:
            connection = sqlite3.connect('assets/movieTicket.db')
            cur = connection.cursor()
            cur.execute('''INSERT into user (username, password, email, age)
                            VALUES (?, ?, ?, ?)''', (username, password, email, age))
            cur.close()
            connection.commit()
            connection.close()
            createNew(signUp, login.logIn)
            
            
    signUpB = Button(box2, text="Create Account", width=15, bg=bgColor3, fg=fgColor1, font=('cambria', 14), 
                     command=lambda: insert(entry1, entry2, entry3, entry4))
    signUpB.place(x=160, y=380)
    
    signUp.mainloop()
  
  
