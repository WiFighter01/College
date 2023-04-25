from tkinter import *

def move(event):
    global canvas
    global line
    canvas.move(line, 0, 100)


root = Tk()
root.title('paint')
root.geometry('300x300')

canvas = Canvas(bg='white', width=250, height=250)
canvas.pack(anchor=CENTER, expand=1)
line = canvas.create_line(10, 10, 200, 50)
canvas.bind('<ButtonPress>', move)


root.mainloop()
