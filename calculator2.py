import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout

# from PyQt4 import QtGui

app = QApplication(sys.argv)
widget = QWidget()
label = QLabel("", widget)
btnAdd = QPushButton("+", widget)
btnSub = QPushButton("-", widget)
btnDiv = QPushButton("/", widget)
btnMul = QPushButton("*", widget)
btnClear = QPushButton("Clear", widget)
txtArea1 = QLineEdit("", widget)
txtArea2 = QLineEdit("", widget)

def init():
    widget.resize(300, 300)
    widget.move(300, 300)
    widget.setWindowTitle('Calculator')
    widget.show()

    txtArea1.move(20, 10)
    txtArea1.show()
    txtArea2.move(20, 50)
    txtArea2.show()

    label.setText("")
    label.move(20, 100)
    label.show()

    btnAdd.setToolTip('+')
    btnAdd.move(20, 120)
    btnAdd.clicked.connect(addition)
    btnAdd.show()

    btnSub.setToolTip('-')
    btnSub.move(110, 120)
    btnSub.clicked.connect(subtraction)
    btnSub.show()

    btnDiv.setToolTip('/')
    btnDiv.move(20, 150)
    btnDiv.clicked.connect(division)
    btnDiv.show()

    btnMul.setToolTip('*')
    btnMul.move(110, 150)
    btnMul.clicked.connect(multiplication)
    btnMul.show()

    btnClear.setToolTip('Clear')
    btnClear.move(200, 150)
    btnClear.clicked.connect(clear)
    btnClear.show()

def addition():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText('Answer: '+str(num1 + num2))

def subtraction():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText('Answer: '+str(num1 - num2))

def multiplication():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText('Answer: '+str(num1 * num2))

def division():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    if num2==0:
        label.setText("division by zero")
    else:
        label.setText('Answer: ' + str(num1 / num2))

def clear():
    txtArea1.setText("{}".format(""))
    txtArea2.setText("{}".format(""))

if __name__ == "__main__":
    init()

app.exec_()