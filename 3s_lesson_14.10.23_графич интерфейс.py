# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Первая программа на PyQt')
window.resize(1280, 720)
label = QtWidgets.QLabel('<center>Привет, мир!</center>')
label2 = QtWidgets.QLabel('<center>Пока, мир!</center>')
btnQuit = QtWidgets.QPushButton('&Закрыть окно')
btn_space = QtWidgets.QPushButton('&Космос')
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(label2)
vbox.addWidget(btnQuit)
vbox.addWidget(btn_space)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
btn_space.clicked.connect(app.activeWindow)
window.show()
sys.exit(app.exec_())
# Ошибка программы, надо разобраться!