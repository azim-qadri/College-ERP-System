import time
import webbrowser
import mysql.connector
import tkinter
from tkinter import *

page = 'admin'


window = Tk()
window.title('ERP System')
photo = PhotoImage(file="icon.png")
window.iconphoto(False, photo)
window["bg"] = "#1C2833"
window.geometry("500x350+{}+{}".format(window.winfo_screenwidth() // 2 - 375, window.winfo_screenheight() // 2 - 250))


# functions

def connect():
    mydb = mysql.connector.connect(
        host="bah6qv28fznfoj3pyusx-mysql.services.clever-cloud.com",
        user="uyvrtgzasma2lvv0",
        password="uCQPecJt0uEjrCC9lblw",
        database="bah6qv28fznfoj3pyusx"
    )
    return mydb


def faculty_main():
    login_screen.destroy()
    win = Tk()
    win.title('Faculty')
    photo = PhotoImage(file="icon.png")
    win.iconphoto(False, photo)
    win["bg"] = "#1C2833"
    win.geometry("500x350+{}+{}".format(win.winfo_screenwidth() // 2 - 375, win.winfo_screenheight() // 2 - 250))
    win.focus_force()

    mydb = connect()
    # select query
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM FACULTY limit 1")
    for FACULTY in cursor:
        for j in range(len(FACULTY)):
            if j == 1:
                continue
            e = Entry(win, width=10, fg='blue')
            e.grid(row=j, column=1)
            e.insert(END, FACULTY[j])
    win.mainloop()


def login():
    # getting form data
    uname = username.get()
    pwd = password.get()
    # open database
    mydb = connect()
    # select query
    cursor = mydb.cursor()
    # applying empty validation
    if uname == '' or pwd == '':
        message.set("fill the empty field!!!")
    elif page == 'admin':

        cursor.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"' % (uname, pwd))
        # fetch data
        if cursor.fetchone():
            message.set("Login success")
            time.sleep(1)
            webbrowser.open('Link to your database')  # url to your database
            login_screen.destroy()
        else:
            message.set("Wrong username or password!!!")
    elif page == 'faculty':
        cursor.execute('SELECT * from FACULTY where FACULTY_UID="%s" and PASSWORD="%s"' % (uname, pwd))
        # fetch data
        if cursor.fetchone():
            message.set("Login success")
            time.sleep(1)
            faculty_main()
        else:
            message.set("Wrong username or password!!!")
    else:
        cursor.execute('SELECT * from STUDENT where STUDENT_UID="%s" and PASSWORD="%s"' % (uname, pwd))
        # fetch data
        if cursor.fetchone():
            message.set("Login success")
        else:
            message.set("Wrong username or password!!!")


# defining loginform function
def loginform():
    global page
    global login_screen
    login_screen = Tk()
    # Setting icon of screen
    photo = PhotoImage(file="icon.png")
    if page == 'admin':
        login_screen.title('ADMIN Login')
    elif page == 'faculty':
        login_screen.title('FACULTY Login')
    else:
        login_screen.title('STUDENT Login')
    login_screen.iconphoto(False, photo)
    login_screen["bg"] = "#1C2833"
    # setting height and width of screen
    login_screen.geometry("500x350+{}+{}".format(login_screen.winfo_screenwidth() // 2 - 375, login_screen.winfo_screenheight() // 2 - 250))
    login_screen.focus_force()
    # declaring variable
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Login From", bg="#0E6655", fg="white", font=("Arial", 12, "bold")).pack(ipady=10)
    # Username Label
    Label(login_screen, text="Username/UID * ", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=40, y=60,)
    # Username textbox
    Entry(login_screen, textvariable=username, bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=185, y=62)
    # Password Label
    Label(login_screen, text="Password * ", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=40, y=100)
    # Password textbox
    Entry(login_screen, textvariable=password, show="*", bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(
        x=185, y=102)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message, bg="#1C2833", fg="white", font=("Arial", 12, "bold")).place(x=185,
                                                                                                                   y=130)
    # Login button
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655", fg="white",
           font=("Arial", 12, "bold")).place(x=185, y=170)
    login_screen.mainloop()


def admin_page():
    global page
    window.destroy()
    page = 'admin'
    loginform()


def faculty_page():
    global page
    window.destroy()
    page = 'faculty'
    loginform()


def student_page():
    global page
    window.destroy()
    page = 'student'
    loginform()


# widgets
main_label = tkinter.Label(window, text="Welcome to ERP!", bg="#1C2833", fg="white", font=("Arial", 12, "bold"))
main_label.grid(column=0, row=0, padx=120, pady=20)
sub_label = tkinter.Label(window, text="Choose from the following to login", bg="#1C2833", fg="white", font=("Arial", 12, "bold"))
sub_label.grid(column=0, row=1, padx=120, pady=20)
admin_btn = Button(window, text="Admin", command=admin_page, bg="#0E6655", fg="white", font=("Arial", 12, "bold"))
admin_btn.grid(column=0, row=2, pady=5, ipadx=35)
faculty_btn = Button(window, text="Faculty", command=faculty_page, bg="#0E6655", fg="white", font=("Arial", 12, "bold"))
faculty_btn.grid(column=0, row=3, pady=5, ipadx=35)
student_btn = Button(window, text="Student", command=student_page, bg="#0E6655", fg="white", font=("Arial", 12, "bold"))
student_btn.grid(column=0, row=4, pady=5, ipadx=35)
window.mainloop()
