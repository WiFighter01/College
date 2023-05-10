from tkinter import *


class MyPaint:
    def __init__(self, root=Tk(), title='Paint', geometry='1280x720', brush_size=1, brush_color='black'):
        self.root = root
        self.title = title
        self.geometry = geometry
        self.brush_size = brush_size
        self.brush_color = brush_color
        self.root.resizable(0, 0)

        self.create_widgets()

    def create_widgets(self):
        # Создание канвы
        self.w = Canvas(self.root, width=self.geometry.split('x')[0], height=self.geometry.split('x')[1], bg='white')
        self.w.bind('<B1-Motion>', self.paint)
        self.w.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky=E + W + S + N)
        self.w.columnconfigure(6, weight=1)
        self.w.rowconfigure(2, weight=1)

        # Кнопки изменения цвета кисти
        red_btn = Button(text='красный', width=10, command=lambda: self.brush_color_change('red'))
        black_btn = Button(text='черный', width=10, command=lambda: self.brush_color_change('black'))
        green_btn = Button(text='зеленый', width=10, command=lambda: self.brush_color_change('green'))
        yellow_btn = Button(text='желтый', width=10, command=lambda: self.brush_color_change('yellow'))
        # Ластик
        white_btn = Button(text='ластик', width=10, command=lambda: self.brush_color_change('white'))
        # Очистка экрана
        clear_all = Button(text='очистить', width=10, command=lambda: self.w.delete('all'))

        # Кнопки изменения размера кисти
        one_btn = Button(text='1', width=10, command=lambda: self.brush_size_change(1))
        five_btn = Button(text='5', width=10, command=lambda: self.brush_size_change(5))
        ten_btn = Button(text='10', width=10, command=lambda: self.brush_size_change(10))
        twenty_btn = Button(text='20', width=10, command=lambda: self.brush_size_change(20))

        # Размещаем кнопки в конве
        red_btn.grid(row=0, column=0)
        black_btn.grid(row=1, column=0)
        green_btn.grid(row=0, column=1)
        yellow_btn.grid(row=1, column=1)
        one_btn.grid(row=0, column=3)
        five_btn.grid(row=0, column=4)
        ten_btn.grid(row=1, column=3)
        twenty_btn.grid(row=1, column=4)
        white_btn.grid(row=0, column=6)
        clear_all.grid(row=1, column=6)

    # Рисовальщик
    def paint(self, event):
        x1 = event.x - self.brush_size
        x2 = event.x + self.brush_size
        y1 = event.y - self.brush_size
        y2 = event.y + self.brush_size
        self.w.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    # Изменение размера кисти
    def brush_size_change(self, new_size):
        self.brush_size = new_size

    # Изменение цвета кисти
    def brush_color_change(self, new_color):
        self.brush_color = new_color


def main():
    paint = MyPaint()
    paint.root.mainloop()


if __name__ == '__main__':
    main()
