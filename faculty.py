from tkinter import *
import main


def faculty_main():
    window = Tk()
    window.title('Faculty')
    photo = PhotoImage(file="icon.png")
    window.iconphoto(False, photo)
    window["bg"] = "#1C2833"
    window.geometry("500x350+{}+{}".format(window.winfo_screenwidth() // 2 - 375, window.winfo_screenheight() // 2 - 250))
    window.focus_force()

    mydb = main.connect()
    # select query
    cursor = mydb.cursor()
    i = 0
    for FACULTY in cursor:
        for j in range(len(FACULTY)):
            e = Entry(window, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, FACULTY[j])
        i = i + 1
    window.mainloop()

