from tkinter import *
from tkinter import filedialog
from PIL import Image
import os


class MyPaint:
    def __init__(self, root=Tk(), title='Paint', geometry='1280x720', brush_size=1, brush_color='black'):
        self.root = root
        self.title = title
        self.geometry = geometry
        self.brush_size = brush_size
        self.brush_color = brush_color
        self.draw_mode = 'brush'  # Режим рисования по умолчанию - кисть
        self.is_drawing = False  # Инициализация переменной состояния рисования
        self.root.resizable(False, False)

        # Вызов виджетов
        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        # Создание канвы
        self.create_canvas()

        # Заголовки меню
        label1 = Label(text='Работа с файлом', foreground='white', justify=LEFT, bg='#909090', width=10)
        label2 = Label(text='Инструменты', foreground='white', justify=LEFT, bg='#909090', width=10)
        label3 = Label(text='Примитивы (можно также вызвать правой кнопкой мыши)', foreground='white', justify=LEFT,
                       bg='#909090', width=10)

        # Кнопки изменения цвета кисти
        red_btn = Button(text='цвет: красный', width=10, command=lambda: self.brush_color_change('red'))
        black_btn = Button(text='цвет: черный', width=10, command=lambda: self.brush_color_change('black'))
        green_btn = Button(text='цвет: зеленый', width=10, command=lambda: self.brush_color_change('green'))
        yellow_btn = Button(text='цвет: желтый', width=10, command=lambda: self.brush_color_change('yellow'))
        # Ластик
        white_btn = Button(text='инструмент: ластик', width=10,
                           command=lambda: [self.brush_color_change('white'), self.set_draw_mode('brush')])
        # Очистка экрана
        clear_all = Button(text='очистить экран', width=10, command=lambda: self.w.delete('all'))

        # Кнопки изменения размера кисти
        one_btn = Button(text='размер: 1', width=10, command=lambda: self.brush_size_change(1))
        five_btn = Button(text='размер: 5', width=10, command=lambda: self.brush_size_change(5))
        ten_btn = Button(text='размер: 10', width=10, command=lambda: self.brush_size_change(10))
        twenty_btn = Button(text='размер: 20', width=10, command=lambda: self.brush_size_change(20))

        # Кнопки переключения режима рисования
        brush_mode_btn = Button(text='инструмент: кисть', width=10, command=lambda: self.set_draw_mode('brush'))
        line_mode_btn = Button(text='линия', width=10, command=lambda: self.set_draw_mode('line'))
        rectangle_btn = Button(text='прямоугольник', width=10, command=lambda: self.set_draw_mode('rectangle'))
        oval_btn = Button(text='овал', width=10, command=lambda: self.set_draw_mode('oval'))
        triangle_btn = Button(text='треугольник', width=10, command=lambda: self.set_draw_mode('triangle'))

        # Кнопка сохранения изображения
        save_img_btn = Button(text='сохранить', width=10, command=lambda: self.save_image())

        # Создание выпадающего меню
        self.draw_menu = Menu(self.root, tearoff=0)
        self.draw_menu.add_command(label='прямоугольник', command=lambda: self.set_draw_mode('rectangle'))
        self.draw_menu.add_command(label='овал', command=lambda: self.set_draw_mode('oval'))
        self.draw_menu.add_command(label='треугольник', command=lambda: self.set_draw_mode('triangle'))

        # Размещаем лейблы в конве
        label1.grid(row=0, columnspan=7, sticky=EW)
        label2.grid(row=2, columnspan=7, sticky=EW)
        label3.grid(row=5, columnspan=7, sticky=EW)
        # Размещаем кнопки в конве
        red_btn.grid(row=3, column=2, sticky=EW)
        black_btn.grid(row=4, column=2, sticky=EW)
        green_btn.grid(row=3, column=3, sticky=EW)
        yellow_btn.grid(row=4, column=3, sticky=EW)
        one_btn.grid(row=3, column=5, sticky=EW)
        five_btn.grid(row=3, column=6, sticky=EW)
        ten_btn.grid(row=4, column=5, sticky=EW)
        twenty_btn.grid(row=4, column=6, sticky=EW)
        white_btn.grid(row=4, column=0, sticky=EW)
        clear_all.grid(row=1, column=1, sticky=EW)
        brush_mode_btn.grid(row=3, column=0, sticky=EW)
        line_mode_btn.grid(row=6, column=0, sticky=EW)
        rectangle_btn.grid(row=6, column=1, sticky=EW)
        oval_btn.grid(row=6, column=2, sticky=EW)
        triangle_btn.grid(row=6, column=3, sticky=EW)
        save_img_btn.grid(row=1, column=0, sticky=EW)

    # Привязка действий к кнопкам
    def setup_bindings(self):
        self.w.bind('<B1-Motion>', self.paint)
        self.w.bind('<Button-1>', self.start_line)
        self.w.bind('<ButtonRelease-1>', self.end_line)
        self.w.bind('<Button-3>', self.show_menu)
        self.w.bind('<Button-1>', self.start_rectangle, '+')
        self.w.bind('<ButtonRelease-1>', self.end_rectangle, '+')
        self.w.bind('<Button-1>', self.start_oval, '+')
        self.w.bind('<ButtonRelease-1>', self.end_oval, '+')
        self.w.bind('<Button-1>', self.start_triangle, '+')
        self.w.bind('<ButtonRelease-1>', self.end_triangle, '+')

    # Создание канвы
    def create_canvas(self):
        width, height = map(int, self.geometry.split('x'))
        self.w = Canvas(self.root, width=width, height=height, bg='white')
        self.w.grid(row=7, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
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

    # Начало рисования прямоугольника
    def start_rectangle(self, event):
        if self.draw_mode == 'rectangle' and not self.is_drawing:
            self.start_x, self.start_y = event.x, event.y
            self.is_drawing = True

    # Окончание рисования прямоугольника
    def end_rectangle(self, event):
        if self.draw_mode == 'rectangle' and self.is_drawing:
            x1 = self.start_x
            y1 = self.start_y
            x2 = event.x
            y2 = event.y
            self.w.create_rectangle(x1, y1, x2, y2, fill='', outline=self.brush_color, width=self.brush_size)
            self.is_drawing = False

    # Начало рисования овала
    def start_oval(self, event):
        if self.draw_mode == 'oval' and not self.is_drawing:
            self.start_x, self.start_y = event.x, event.y
            self.is_drawing = True

    # Окончание рисования овала
    def end_oval(self, event):
        if self.draw_mode == 'oval' and self.is_drawing:
            x1 = self.start_x
            y1 = self.start_y
            x2 = event.x
            y2 = event.y
            self.w.create_oval(x1, y1, x2, y2, fill='', outline=self.brush_color, width=self.brush_size)
            self.is_drawing = False

    # Начало рисования треугольника
    def start_triangle(self, event):
        if self.draw_mode == 'triangle' and not self.is_drawing:
            self.start_x, self.start_y = event.x, event.y
            self.is_drawing = True

    # Окончание рисования треугольника
    def end_triangle(self, event):
        if self.draw_mode == 'triangle' and self.is_drawing:
            x1 = self.start_x
            y1 = event.y
            x2 = (self.start_x + event.x) / 2
            y2 = self.start_y
            x3 = event.x
            y3 = event.y
            self.w.create_polygon(x1, y1, x2, y2, x3, y3, fill='', outline=self.brush_color, width=self.brush_size)
            self.is_drawing = False

    def save_image(self):
        file_path = filedialog.asksaveasfile(defaultextension='.png', filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg')])
        if file_path:
            ps_file = f'{file_path.name}.ps'  # Сохранение изображения в формате ps
            self.w.postscript(file=ps_file, colormode='color')

            # Преобразование файла PostScript в формат изображения
            image = Image.open(ps_file)
            image.save(f'{file_path.name}')

            # Закрытие файла PostScript и его удаление
            image.close()
            file_path.close()
            os.remove(ps_file)

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
