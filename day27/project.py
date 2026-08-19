# build a converter from miles to kilometer
from tkinter import *
import math

window = Tk()
window.minsize(width=600, height=300)
window.title("Mile to Km Converter")
window.config(padx=150, pady=75)
    

my_entry = Entry(width=5)
my_entry.grid(row=0, column=2)

miles_label = Label(text="Miles", font=("Helvetica", 12))
miles_label.grid(row=0, column=3)

my_label = Label(text="is equal to", font=("Helvetica", 12))
my_label.grid(row=1, column=1)
my_label.config(pady=10)

result = Label(text=0, font=("Helvetica", 10,"bold" ))
result.grid(row=1, column=2)

label_two = Label(text="Km", font=("Helvetica", 12))
label_two.grid(row=1, column=3)

def calculate_btn():
    entry_text = float(my_entry.get())
    km = entry_text * 1.60934
    result.config(text=math.floor(km))

button = Button(text="Calculate", font=("Helvetica", 10, "bold"), command=calculate_btn)
button.grid(row=2, column=2)

window.mainloop()