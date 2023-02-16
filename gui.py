from tkinter import *
from tkinter import ttk


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x500")
window.configure(bg = "#2c3333")
canvas = Canvas(
    window,
    bg = "#2c3333",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#E7F6F2",
                rowheight=25,
                fieldbackground="#E7F6F2")
my_tree = ttk.Treeview()
my_tree['columns'] = ("File Name", "Qualification")

my_tree.column("#0", width=30, minwidth=25)
my_tree.column("File Name", width=100, anchor=W)
my_tree.column("Qualification", anchor=CENTER, width=100)

# Headings
my_tree.heading("#0", text="#", anchor=CENTER)
my_tree.heading("File Name", text="File Name", anchor=CENTER)
my_tree.heading("Qualification", text="Qualification", anchor=CENTER)

my_tree.insert(parent='', index='end', iid=0, text="1", values=("Resume", "50%"))
my_tree.place(x=447, y=70, width=319, heigh=281)

# my_tree.pack()

img0 = PhotoImage(file = "img0.png")
btnOpen = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btnOpen.place(
    x = 34, y = 27,
    width = 190,
    height = 43)

lblFile = Label(
    font=("Archivo Black",15, "bold"),
    bg="#2c3333",
    fg="white",
    text="File Path:"
)

lblFile.place(
    x=240,
    y=30
)
imgSearch = PhotoImage(file = "imgSearch.png")
btnSearch = Button(
    image = imgSearch,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btnSearch.place(
    x = 129, y = 367,
    width = 190,
    height = 43)

imgClear = PhotoImage(file = "imgClear.png")
btnClear = Button(
    image = imgClear,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btnClear.place(
    x = 512, y = 367,
    width = 190,
    height = 43)

label1 = Label(
    window,
    text="Education\n\n\nExperience\n\n\nSkills\n\n\nLanguage",
    font="Times 14",
    bg="#2c3333",
    fg="white"
)

label1 = Label(window, text = "Education\n\n\nExperience\n\n\nSkills\n\n\nLanguage",font="Times 14", bg = "#2c3333", fg = "white", justify = "left")
label1.pack()

label1.place(
    x = 0, y = 100,
    width = 190,
    height = 220)

# Create text boxes
education = Entry(window, width=25, font = "Times 14", bg = "#E7F6F2")
education.place(x=170, y=105)
experience = Entry(window, width=25, font = "Times 14", bg = "#E7F6F2")
experience.place(x=170, y=170)
skills = Entry(window, width=25, font = "Times 14", bg = "#E7F6F2")
skills.place(x=170, y=230)
language = Entry(window, width=25, font = "Times 14", bg = "#E7F6F2")
language.place(x=170, y=295)

window.resizable(False, False)
window.mainloop()