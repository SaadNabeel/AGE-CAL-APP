from tkinter import *
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        dob = datetime(year, month, day)
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter a valid date!")

root = Tk()
root.title("Age Calculator App")
root.geometry("400x300")
root.config(bg="#d0efff")

frame = Frame(root, bg="#d0efff")
frame.pack(pady=20)

title_label = Label(frame, text="Age Calculator", bg="#3895D3", fg="white", font=("Arial", 16), width=20)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

day_label = Label(frame, text="Day:", bg="#3895D3", fg="white", width=10)
day_label.grid(row=1, column=0, pady=5)
day_entry = Entry(frame, width=5)
day_entry.grid(row=1, column=1)

month_label = Label(frame, text="Month:", bg="#3895D3", fg="white", width=10)
month_label.grid(row=2, column=0, pady=5)
month_entry = Entry(frame, width=5)
month_entry.grid(row=2, column=1)

year_label = Label(frame, text="Year:", bg="#3895D3", fg="white", width=10)
year_label.grid(row=3, column=0, pady=5)
year_entry = Entry(frame, width=5)
year_entry.grid(row=3, column=1)

calculate_button = Button(frame, text="Calculate Age", bg="red", fg="white", command=calculate_age)
calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

result_label = Label(root, text="", bg="#d0efff", fg="black", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
