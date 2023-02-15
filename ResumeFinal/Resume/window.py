from tkinter import *


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

img0 = PhotoImage(file = f"img0.png")
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

imgSearch = PhotoImage(file = f"imgSearch.png")
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

imgClear = PhotoImage(file = f"imgClear.png")
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

window.resizable(False, False)
window.mainloop()
