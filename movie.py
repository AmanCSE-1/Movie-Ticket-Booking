from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

import sqlite3
import json
import smtplib


username = None
email = None
   
def movie():
    movie = Tk()
    movie.geometry("1024x786")
    movie.resizable(0,0)
    movie.title("MovieZone - Movie Ticket Booking")

    global username
    global email
    #-------------------Navbar----------------------#
    #----------------------------------------------#
    bgColor = "#F1BB47"
    navbar = LabelFrame(movie, height=4, width=1024, bg=bgColor, fg='white', padx=50, pady=10)
    navbar.place(x=0, y=0)
    navbar.pack()

    brandName = Label(navbar, text="Movie-Zone", font=('cambria', 20) , bg=bgColor)
    brandName.grid(row=0, column=0)

    space = Label(navbar, width=59, bg=bgColor).grid(row=0, column=1) 
    button1 = Button(navbar, text="Home", padx=5, bg=bgColor, command=lambda: createNew(movie, home))
    button1.grid(row=0, column=2)

    button2 = Button(navbar, text="Movies", padx=5, bg=bgColor)
    button2.grid(row=0, column=3)

    button3 = Button(navbar, text="My Bookings", padx=5, bg=bgColor)
    button3.grid(row=0, column=4)

    button4 = Button(navbar, text="Contact Us", padx=5, bg=bgColor)
    button4.grid(row=0, column=5)

    button5 = Button(navbar, text="Log Out", padx=18, bg="Red")
    button5.grid(row=0, column=6)


    #--------------Banner-----------------------------#
    #-------------------------------------------------#
    bgColor1 = "#4C929E"
    banner = LabelFrame(movie, height=720, width=1024, bg=bgColor1, padx=70, pady=20)
    banner.place(x=0, y=62)
    
    welcome = Label(banner, text="Welcome " + str(username),font=('Cambria', 22, 'bold'), bg=bgColor1, fg="#F1D9A7")
    welcome.place(x=330, y=20)
    
    taglineText = "Enjoy all Bollywood and Hollywood Movies\nBook your movies tickets now, offers avaliable..!!"
    tagline = Label(banner, text=taglineText, font=('Arial', 12, 'italic'), bg=bgColor1, pady=10, fg="#F1D9A7")
    tagline.place(x=270, y=60)
    
    
    def bookWindow(path, name):
        bookWindow = Toplevel(movie)
        bookWindow.title("Booking Window")
        bookWindow.geometry("400x580")
        bookWindow.resizable(0,0)
        
        bgColor3="#F1BB47"; fgColor3="#000066"
        banner = LabelFrame(bookWindow, height=580, width=400, bg=bgColor3)
        banner.place(x=0, y=0)
        image = Image.open(path)
        image = image.resize((350, 200), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image)
        main = Label(bookWindow, height=200, width=350, padx=5, pady=5, image=test, bg="#DEE2FF")
        main.image = test
        main.place(x=20, y=20)
        
        with open("ESD/movieDetails.json") as jsonData:
            details = json.load(jsonData)
            
        Label(bookWindow, text=name, font=('Cambria', 18, 'bold'), bg=bgColor3, fg=fgColor3).place(x=150, y=225)
        Label(bookWindow, text="Cast : "+ details[name]["Cast"], font=('Comic', 12), bg=bgColor3, fg=fgColor3).place(x=60, y=260)
        Label(bookWindow, text="Genre : "+ details[name]["Genre"], font=('Comic', 12), bg=bgColor3, fg=fgColor3).place(x=60, y=285)
        
        Label(bookWindow, text="Bookings", font=('Arial', 14), bg=bgColor3, fg=fgColor3).place(x=150, y=340)
        city = StringVar()
        city.set("Select any City")
        cityC = OptionMenu(bookWindow, city, "INOX, Kandivali", "Woodland, Virar", "INOX, Andheri") 
        cityC.place(x=50, y=370)
    
        Label(bookWindow, text="Rs. 300 per ticket", font=('Arial', 12),bg=bgColor3, fg=fgColor3).place(x=220, y=370)
        
        time = StringVar()
        time.set("Select the time")
        timeC = OptionMenu(bookWindow, time, "10:00 AM", "6:00 PM", "9:00 PM")
        timeC.place(x=220, y=410)
        
        date = StringVar()
        date.set("Select the date")
        dateC = OptionMenu(bookWindow, date, "18 April", "19 April", "21 April")
        dateC.place(x=50, y=410)
        
        labelN = Label(bookWindow, text="Enter your Number of Tickets:").place(x=53, y=450)
        seat = Entry(bookWindow)
        seat.place(x=220, y=450)
        
        bookB = Button(bookWindow, width=20, height=2, text="Confirm Booking", bg="#FE5F55", fg="#EEF5DB", 
                       font=('Cambria', 12, 'bold'), 
                       command=lambda:book(city, time, date, seat, name, bookWindow))
        bookB.place(x=100, y=500)
    
    def placeMovie(path, w, h, xcoordinate, ycoordinate, name):
        image = Image.open(path)
        image = image.resize((w-5, h-5), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image)
        main = Label(banner, height=h, width=w, padx=5, pady=5, image=test, bg="#DEE2FF")
        main.image = test
        main.place(x=xcoordinate, y=ycoordinate)
        button = Button(banner, width=24, height=2, text=name, bg="#DEE2FF", command=lambda:bookWindow(path, name))
        button.place(x=xcoordinate, y=ycoordinate+h+2)
    
    section1 = Label(banner, text="In Theatres", bg=bgColor1, fg="#DEE2FF", font=('Cambria',14, 'italic'))
    section1.place(x=40, y=165)

    placeMovie("ESD/Homepage/Roohi.jpg", 172, 140, 40, 200, "Roohi")
    placeMovie("ESD/Homepage/Aranya tamil.jpg", 172, 140, 340, 200, "Aranya")
    placeMovie("ESD/Homepage/godzilla vs kong.jpg", 172, 140, 640, 200, "Godzilla vs Kong")
    
    section2 = Label(banner, text="Upcoming Movies", bg=bgColor1, fg="#DEE2FF", font=('Cambria',14, 'italic'))
    section2.place(x=40, y=445)

    placeMovie("ESD/Homepage/sooryavanshi.jpg", 172, 140, 40, 480, "Sooryavanshi")
    placeMovie("ESD/Homepage/black-widow.jpg", 172, 140, 340, 480, "Black Widow")
    placeMovie("ESD/Homepage/saina.jpg", 172, 140, 640, 480, "Saina")
    
    movie.mainloop()
       
def book(entry1, entry2, entry3, entry4, name, frame):
    global username
    global email
    
    city = entry1.get()
    time = entry2.get()
    date = entry3.get()
    seat = entry4.get()
    
    if (seat)=="":
        tkinter.messagebox.showerror("Movie-Mania", "Enter Correct Seat Number")
        return
    if city=="Select any City":
        tkinter.messagebox.showerror("Movie-Mania", "Select a city")
        return
    if date=="Select the date":
        tkinter.messagebox.showerror("Movie-Mania", "Select a date")
        return
    if time=="Select the time":
        tkinter.messagebox.showerror("Movie-Mania", "Select a time")
        return
    
    try:
        connection = sqlite3.connect('ESD/Homepage/movieTicket.db')
        cur = connection.cursor()
        cur.execute('''INSERT into booking (username, city, time, date, seat)
                        VALUES (?, ?, ?, ?, ?)''', (username, city, time, date, str(seat)))
        cur.close()
        connection.commit()
        connection.close()
        
    except:
        print("DB Error")
        
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("project.python2424@gmail.com", "Python24@TRUE")
    
    msg = "Hi  " + str(username) +"\nYour Movie Ticket Booking has been successfully completed..!!!"
    msg += "\n\nThese are your booking details:\nMovie-Name :-   "+ name
    msg += "\nCity :-  " + city
    msg += "\nDate :-  " + date + "\t\tTime :-   "+time
    msg += "\nSeat Allotment :-   " + "A5"
    msg += "\n\nEnjoy your show...!!!"
    server.sendmail("project.python2424@gmail.com", email, msg)
    server.quit()
    
    tkinter.messagebox.showinfo("Movie-Zone", "Booking Successfull")
    frame.destroy()
