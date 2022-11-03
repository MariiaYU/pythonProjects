from tkinter import *

window = Tk()


def calculate():
    km = float(input.get())
    mile = km * 1.609
    am_km["text"] = f"{mile}"


window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=2, row=1)

miles = Label(text="Miles")
miles.grid(column=3, row=1)
km = Label(text="Km")
km.grid(column=3, row=2)
is_eq_to = Label(text="is equal to")
is_eq_to.grid(column=1, row=2)
am_km = Label(text="0")
am_km.grid(column=2, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)


window.mainloop()