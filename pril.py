import sys, random, threading  # sys нужен для передачи argv в QApplication
from ui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
f ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя0123456789!@#$%^&*()_+-=`~№;:?<>/.,{}[] "
df = len(f)#длинна переменной f
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()
def sg():
    k = ui.lineEdit.text()
    try:
        file = open("sp.txt", "w")
        rt = ""
        for i in range(int(k)):
            rt += f[random.randint(0, df - 1)]
        file.write(rt)
        file.close()
        if ui.checkBox_2.checkState():
            file = open(QFileDialog.getSaveFileName()[0],"w")
            file.write(rt)
            file.close()
        msg = QMessageBox()
        msg.setWindowTitle("Успех")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        if ui.checkBox_2.checkState():
            msg.setText(
                "Ключевая последовательность успешно сгенерирована и её копия сохранена в заданном вами файле, в указанной директории.")
        else:
            msg.setText("Ключевая последовательность успешно сгенерирована. Она записана в файле sp.txt. \n Файл находится в дериктории, в которой установлена эта программа.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    except ValueError:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!!!")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setText("Введите в верхнее поле ввода положительное число. Это длинна ключевой последовательности!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
def sig(id):#ччтобы в потоке вызвать сигнал, который вызовет уведомление, а основной поток продолжит работу
    ui.mysignal1.emit(int(id))
def sh():#шифрование
    text = ui.textEdit.toPlainText()
    rt = ""
    if ui.checkBox.checkState():
        for i in range(len(text)):
            rt += f[random.randint(0, df - 1)]
        fi = open("sp.txt", "w")
        fi.write(rt)
        fi.close()
        if ui.checkBox_2.checkState():
            fil = QFileDialog.getSaveFileName()[0]
            if fil != "":
                fi = open(fil, "w")
                fi.write(rt)
                fi.close()
                #ui.mysignal1.emit(1)
                threading.Thread(target=sig, args=("1"), daemon=True).start()
            else:
                threading.Thread(target=sig, args=("2"), daemon=True).start()
        else:
            threading.Thread(target=sig, args=("2"), daemon=True).start()
    try:
        file = open("sp.txt", "r")
        rt = file.read()
    except:
        ui.mysignal.emit(1)
        return 0
    if len(text) > len(rt):
        ui.mysignal.emit(2)
        return 0
    sh = ""
    for i in range(len(text)):
        n = f.index(text[i]) + f.index(rt[i])
        if n > df - 1:
            n -= df
        sh += f[n]
    ui.textEdit_2.setPlainText(sh)
def dsh():#расшифровка
    sh = ui.textEdit.toPlainText()
    rt = ""
    rsh = ""
    try:
        file = open("sp.txt", "r")
        rt = file.read()
    except:
        ui.mysignal.emit(1)
        return 0
    if len(sh) > len(rt):
        ui.mysignal.emit(2)
        return 0
    for i in range(len(sh)):
        n = f.index(sh[i]) - f.index(rt[i])
        if n < 0:
            n += df
        rsh += f[n]
    ui.textEdit_2.setPlainText(rsh)
def vop():
    msg = QMessageBox()
    msg.setWindowTitle("Объяснение")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText(
        "OBK(Одноразовый Блокнот шифр, который использовал КГБ) решил назвать так программу, потому что алгоритм шифрования(Один Блокнот), на котором она основана, описан в книге Брюса Шнайера 'Прикладная Криптография', автор рассказал о том, что его использовали многие спецслужбы включая КГБ.Мне он понравился, и я реализовал его на python.\nЧтобы зашифровать текст нужно сгенерировать ключевую последовательность, её длина должна быть меньше либо равна длине оригинального текста! Для этого нужно в вверхнюю линию ввода ввести длинну ключевой последовательности и нажать на кнопку 'Сгенерировать ключевую последовательность'. Можно также сгенерировать ключевую последовательность при шифровании текста, это будет описано ниже. Ключевую последовательность можно 'сохранить' и загрузить. Чтобы 'сохранить' файл с ключевой последовательностью нажмите на кнопку 'скопировать ключевую последовательность' и выберите директорию и имя файла, в который запишется ключевая последовательность из файла sp.txt. В файл sp.txt, ключевая последовательность записывается сразу после генерации шифра, этот файл находится в директории, в которой установлена эта программа. Чтобы загрузить ключевую последовательность нажмите на кнопку 'загрузить ключевую последовательность' и выбирите файл, в которой она записана.\nЧтобы зашифровать текст введите его в поле 'Входные данные' и нажмите на кнопку 'зашифровать' зашифрованный текст появится в поле 'Выходные данные'. Перед шифрованием текста сгенерируйте или загрузите ключевую последовательность, или проделайте нижеописанные действия! Можно обойтись без загрузки и генерации ключевой последовательности, для этого нужно перед нажатием на кнопку 'зашифровать' включить 'Сгенерировать ключевую последовательность по длинне оригинального текста', для генерации ключевой последовательности по длине введённого вами текста, также можно включить 'Сделать копию файла с ключевой последовательностью', чтобы сразу сохранить копию файла с ключевой последовательностью, в выбранной вами директории.\n Для расшифровки текста нужно ввести шифротекст в поле 'Входные данные' и нажать кнопку 'расшифровать'. Только перед этим вы должны загрузить ключевую последовательность.")
    #msg.setIcon(QMessageBox.Information)
    msg.exec_()
def load_rt():
    try:
        fil = QFileDialog.getOpenFileName()[0]
        if fil == "":
            return 0
        file = open(fil, "r")
        rt = file.read()
        f = open("sp.txt", "w")
        f.write(rt)
        ui.mysignal1.emit(3)
    except:
        ui.mysignal1.emit(3)
def save_rt():
    try:
        file = open("sp.txt", "r")
        rt = file.read()
        file.close()
        file = open(QFileDialog.getSaveFileName()[0], "w")
        file.write(rt)
        ui.mysignal1.emit(4)
    except FileNotFoundError:
        ui.mysignal1.emit(1)
ui.pushButton_2.clicked.connect(dsh)
ui.pushButton_3.clicked.connect(sg)
ui.pushButton.clicked.connect(sh)
ui.pushButton_4.clicked.connect(vop)
ui.pushButton_5.clicked.connect(load_rt)
ui.pushButton_6.clicked.connect(save_rt)
sys.exit(app.exec_())