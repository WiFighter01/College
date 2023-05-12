from tkinter import *


class MyPaint:
    def __init__(self, root=Tk(), title='Paint', geometry='1280x720', brush_size=1, brush_color='black'):
        self.root = root
        self.title = title
        self.geometry = geometry
        self.brush_size = brush_size
        self.brush_color = brush_color
        self.draw_mode = 'brush'  # Режим рисования по умолчанию - кисть
        self.is_drawing = False  # Инициализация переменной состояния рисования
        self.root.resizable(0, 0)

        # Вызов виджетов
        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        # Создание канвы
        self.create_canvas()

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

        # Кнопки переключения режима рисования
        brush_mode_btn = Button(text='кисть', width=10, command=lambda: self.set_draw_mode('brush'))
        line_mode_btn = Button(text='линия', width=10, command=lambda: self.set_draw_mode('line'))

        # Создание выпадающего меню
        self.draw_menu = Menu(self.root, tearoff=0)
        self.draw_menu.add_command(label='прямоугольник', command=lambda: self.set_draw_mode('rectangle'))
        self.draw_menu.add_command(label='многоугольник', command=lambda: self.set_draw_mode('polygon'))

        # Размещаем кнопки в конве
        red_btn.grid(row=0, column=0, sticky=EW)
        black_btn.grid(row=1, column=0, sticky=EW)
        green_btn.grid(row=0, column=1, sticky=EW)
        yellow_btn.grid(row=1, column=1, sticky=EW)
        one_btn.grid(row=0, column=3, sticky=EW)
        five_btn.grid(row=0, column=4, sticky=EW)
        ten_btn.grid(row=1, column=3, sticky=EW)
        twenty_btn.grid(row=1, column=4, sticky=EW)
        white_btn.grid(row=0, column=6, sticky=EW)
        clear_all.grid(row=1, column=6, sticky=EW)
        brush_mode_btn.grid(row=3, column=0, sticky=EW)
        line_mode_btn.grid(row=3, column=1, sticky=EW)

    # Привязка действий к кнопкам
    def setup_bindings(self):
        self.w.bind('<B1-Motion>', self.paint)
        self.w.bind('<Button-1>', self.start_line)
        self.w.bind('<ButtonRelease-1>', self.end_line)
        self.w.bind('<Button-3>', self.show_menu)
        self.w.bind('<Button-1>', self.start_rectangle, '+')
        self.w.bind('<ButtonRelease-1>', self.end_rectangle, '+')

    # Создание канвы
    def create_canvas(self):
        width, height = map(int, self.geometry.split('x'))
        self.w = Canvas(self.root, width=width, height=height, bg='white')
        self.w.grid(row=4, column=0, columnspan=8, padx=5, pady=5, sticky=E + W + S + N)
        self.w.columnconfigure(6, weight=1)
        self.w.rowconfigure(4, weight=1)

    # Рисовальщик
    def paint(self, event):
        if self.draw_mode == 'brush':
            x1 = event.x - self.brush_size / 2
            x2 = event.x + self.brush_size / 2
            y1 = event.y - self.brush_size / 2
            y2 = event.y + self.brush_size / 2
            self.w.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    # Начало рисования линии
    def start_line(self, event):
        if self.draw_mode == 'line' and not self.is_drawing:
            self.start_x, self.start_y = event.x, event.y
            self.is_drawing = True

    # Окончание рисования линии
    def end_line(self, event):
        if self.draw_mode == 'line' and self.is_drawing:
            x1 = self.start_x
            y1 = self.start_y
            x2 = event.x
            y2 = event.y
            self.w.create_line(x1, y1, x2, y2, fill=self.brush_color, width=self.brush_size)
            self.is_drawing = False

    def start_rectangle(self, event):
        if self.draw_mode == 'rectangle' and not self.is_drawing:
            self.start_x, self.start_y = event.x, event.y
            self.is_drawing = True

    def end_rectangle(self, event):
        if self.draw_mode == 'rectangle' and self.is_drawing:
            x1 = self.start_x
            y1 = self.start_y
            x2 = event.x
            y2 = event.y
            self.w.create_rectangle(x1, y1, x2, y2, fill='', outline=self.brush_color, width=self.brush_size)
            self.is_drawing = False

    # Изменения режима рисования
    def set_draw_mode(self, mode):
        self.draw_mode = mode

    def show_menu(self, event):
        self.draw_menu.post(event.x_root, event.y_root)

    # Изменение размера кисти
    def brush_size_change(self, new_size):
        self.brush_size = new_size

    # Изменение цвета кисти
    def brush_color_change(self, new_color):
        self.brush_color = new_color


def main():
    app = MyPaint()
    app.root.mainloop()


if __name__ == '__main__':
    main()
