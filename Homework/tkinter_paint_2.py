from tkinter import *
from tkinter import ttk

brush_size = 1
brush_color = 'black'


def paint(event):
    global brush_size
    global brush_color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)


def brush_size_change(new_size):
    global brush_size
    brush_size = new_size


def brush_color_change(new_color):
    global brush_color
    brush_color = new_color


root = Tk()
root.title('Paint')
root.geometry('1280x720')
root.resizable(0, 0)

w = Canvas(root, width=1280, height=720, bg='white')
w.bind('<B1-Motion>', paint)
w.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky=E + W + S + N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

red_btn = Button(text='красный', width=10, command=lambda: brush_color_change('red'))
black_btn = Button(text='черный', width=10, command=lambda: brush_color_change('black'))
green_btn = Button(text='зеленый', width=10, command=lambda: brush_color_change('green'))
yellow_btn = Button(text='желтый', width=10, command=lambda: brush_color_change('yellow'))
white_btn = Button(text='ластик', width=10, command=lambda: brush_color_change('white'))
clear_all = Button(text='очистить', width=10, command=lambda: w.delete('all'))

five_btn = ttk.Button(text='5', width=10, command=lambda: brush_size_change(5))

red_btn.grid(row=0, column=0)
black_btn.grid(row=0, column=1)
green_btn.grid(row=0, column=2)
yellow_btn.grid(row=0, column=3)
white_btn.grid(row=0, column=4)
clear_all.grid(row=0, column=5)
five_btn.grid(row=0, column=6)

root.mainloop()
