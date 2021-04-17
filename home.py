def createNew(base, new):
    base.destroy()
    new()

def home():
    home = Tk()
    home.geometry("1024x786")
    home.resizable(0,0)
    home.title("MovieZone - Movie Ticket Booking")


    #-------------------Navbar----------------------#
    #----------------------------------------------#
    bgColor = "#F1BB47"
    navbar = LabelFrame(home, height=4, width=1024, bg=bgColor, fg='white', padx=50, pady=10)
    navbar.place(x=0, y=0)
    navbar.pack()

    brandName = Label(navbar, text="Movie-Zone", font=('Cambria', 20) , bg=bgColor)
    brandName.grid(row=0, column=0)

    space = Label(navbar, width=59, bg=bgColor).grid(row=0, column=1) 
    button1 = Button(navbar, text="Home", padx=5, bg=bgColor)
    button1.grid(row=0, column=2)

    button2 = Button(navbar, text="Movie", padx=5, bg=bgColor, command= lambda: createNew(home, movie))
    button2.grid(row=0, column=3)

    button3 = Button(navbar, text="My Bookings", padx=5, bg=bgColor)
    button3.grid(row=0, column=4)

    button4 = Button(navbar, text="Contact Us", padx=5, bg=bgColor)
    button4.grid(row=0, column=5)

    button5 = Button(navbar, text="Log In", padx=18, bg="#F1D9A7")
    button5.grid(row=0, column=6)


    #--------------Banner-----------------------------#
    #-------------------------------------------------#
    bgColor1 = "#4C929E"
    banner = LabelFrame(home, height=400, width=1024, bg=bgColor1, padx=70, pady=20)
    banner.place(x=0, y=62)
    
    welcome = Label(banner, text="Movie Ticket Booking",font=('Cambria', 34, 'bold'), bg=bgColor1, fg="#F1D9A7")
    welcome.place(x=50, y=60)
    
    taglineText = "Enjoy all Bollywood and Hollywood homes\nBook your homes tickets now, offers avaliable..!!"
    tagline = Label(banner, text=taglineText, font=('Arial', 12, 'italic'), bg=bgColor1, pady=10, fg="#DEE2FF")
    tagline.place(x=80, y=130)
    
    signUpB = Button(banner, text="Sign Up for Free", bg="#F1D9A7", fg="#000066", height=2, padx=5, font=('Cambria'), 
                     command= lambda: createNew(home, signUp))
    signUpB.place(x=70, y=250)
    
    label = Label(banner, text="OR", font=('Arial', 14, 'bold'), bg=bgColor1, pady=10, fg="#DEE2FF")
    label.place(x=250, y=252)
    
    logInB = Button(banner, text="Log In", bg="#F1D9A7", fg="#000066", height=2, padx=10, font=('Cambria'), 
                   command= lambda: createNew(home, logIn))
    logInB.place(x=340, y=250)
    
    image = Image.open('ESD/Homepage/home.png')
    image = image.resize((320, 270), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image)
    main = Label(banner, height=270, width=320, padx=5, pady=5, image=test, bg="#DEE2FF")
    main.image = test
    main.place(x=550, y=50)
    
    
    
    #---------------------------New Banner---------------------------------------#
    #----------------------------------------------------------------------------#
    bgColor2 = "#C4DACF"; fgColor2 = "#63585E"
    banner2 = LabelFrame(home, height=720, width=1024, bg="#C4DACF", padx=70, pady=20)
    banner2.place(x=0, y=440)
    
    def placemovie2(path, w, h, xcoordinate, ycoordinate, name):
        image = Image.open(path)
        image = image.resize((w-5, h-5), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image)
        main = Label(banner2, height=h, width=w, padx=5, pady=5, image=test, bg="#DEE2FF")
        main.image = test
        main.place(x=xcoordinate, y=ycoordinate)
        button = Button(banner2, width=24, height=2, text=name, bg="#DEE2FF")
        button.place(x=xcoordinate, y=ycoordinate+h+2)
    
    section2 = Label(banner2, text="Exclusive Offers on Blockbuster Hit", bg=bgColor2, fg=fgColor2, font=('Cambria',14, 'italic'))
    section2.place(x=40, y=20)

    placemovie2("ESD/Homepage/sooryavanshi.jpg", 172, 140, 40, 70, "Sooryavanshi")
    placemovie2("ESD/Homepage/black-widow.jpg", 172, 140, 340, 70, "Black Widow")
    placemovie2("ESD/Homepage/saina.jpg", 172, 140, 640, 70, "Sania")
    
    home.mainloop()
    
home()
