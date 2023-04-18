from tkinter import *


def finish():
    w.destroy()
    print('close application')


clicks = 0


def click_button():
    global clicks
    clicks += 1
    if clicks < 10:
        but['text'] = f'Click {clicks}'
    else:
        but['state'] = ['disabled'] # блокировка кнопки


w = Tk()
w.title('Tkinter Application')
# w.iconbitmap(default='handshake.png') не работает
icon = PhotoImage(file='handshake.png')  # Добавление иконки в верхний левый угол
w.iconphoto(False, icon)
w.geometry('300x700')
frame1 = Frame()
frame2 = Frame()

lab_hello = Label(master=frame1, text='Hello, Tkinter!',
                  foreground='#FFFFFF', background='#000000',  # цвета можно задать как текстом так и в 16-й системе
                  width=20, height=20)                         # c индексом #
lab_hello.pack()
label2 = Label(master=frame2, text='I am in frame2')
label2.pack()
but = Button(master=frame2, text='Press!', width=30, height=10,
             bg='blue', fg='green', command=click_button)
but.pack()
but['text'] = 'Click'

entry = Entry(master=frame2, fg='red', bg='yellow', width=50)
entry.pack()

frame1.pack()
frame2.pack()

w.protocol('WM_DELETE_WINDOW', finish)
# w.attributes('-fullscreen', True) #открытие окна на весь экран
w.mainloop()
