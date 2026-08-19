import tkinter


def clicked_btn():
    entry_text = input.get()
    my_label.config(text=entry_text)


window = tkinter.Tk()
window.title("GUI PROGRAM")
window.minsize(width=500, height=300)
# changing padding in the whole of the window
window.config(padx=100, pady=200)


my_label = tkinter.Label(text="I'm a Label", font=("Helvetica", 12, "bold"))
# my_label.pack()
# for precise use place instead of pack side...
# my_label.place(x=100, y=200)
# note you cant use grid with pack at the same time
my_label.grid(row=0, column=0)

# text input
input = tkinter.Entry(width=30)
# input.pack()
input.grid(row=1, column=1)

# challenge,, whenever one cliks the btn to show the label as what was written on the
# text input

btn = tkinter.Button(text="new btn")
btn.grid(row=0, column=2)

button = tkinter.Button(text="Click me", command=clicked_btn)
# button.pack()
button.grid(row=2, column=3)


window.mainloop()
