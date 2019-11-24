import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.values=[]
        self.setWindowTitle("Калькулятор")
        self.setWindowTitle('form')
        self.resize(300, 300)
        self.move(300, 300)
        self.input = QLabel('')
        self.label1 = QLineEdit()
        self.label2 = QLabel('Ответ')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button0 = QPushButton('0')
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_split = QPushButton('/')
        self.button_answer= QPushButton('=')
        self.button_clear = QPushButton('C')



        self.button1.clicked.connect(self.press)
        self.button2.clicked.connect(self.press)
        self.button3.clicked.connect(self.press)
        self.button4.clicked.connect(self.press)
        self.button5.clicked.connect(self.press)
        self.button6.clicked.connect(self.press)
        self.button7.clicked.connect(self.press)
        self.button8.clicked.connect(self.press)
        self.button9.clicked.connect(self.press)
        self.button0.clicked.connect(self.press)
        self.button_plus.clicked.connect(self.press)
        self.button_minus.clicked.connect(self.press)
        self.button_multiply.clicked.connect(self.press)
        self.button_split.clicked.connect(self.press)
        self.button_answer.clicked.connect(self.answer)
        self.button_clear.clicked.connect(self.clear)

        self.layout = QGridLayout()

        self.layout.addWidget(self.label1,0,1)
        self.layout.addWidget(self.label2,1,1)
        self.layout.addWidget(self.button_plus,2,0)
        self.layout.addWidget(self.button_minus,3,0)
        self.layout.addWidget(self.button_multiply,4,0)
        self.layout.addWidget(self.button_split,5,0)
        self.layout.addWidget(self.button_answer,5,1)
        self.layout.addWidget(self.button_clear,5,3)
        self.layout.addWidget(self.button1,2,1)
        self.layout.addWidget(self.button2,2,2)
        self.layout.addWidget(self.button3,2,3)
        self.layout.addWidget(self.button4,3,1)
        self.layout.addWidget(self.button5,3,2)
        self.layout.addWidget(self.button6,3,3)
        self.layout.addWidget(self.button7,4,1)
        self.layout.addWidget(self.button8,4,2)
        self.layout.addWidget(self.button9,4,3)
        self.layout.addWidget(self.button0,5,2)
        self.setLayout(self.layout)

    def press(self):
        click = self.sender()
        self.values.append(click.text())
        self.res = ''.join(self.values)
        self.label1.setText('{}'.format(self.res))

    def clear(self):
        self.values=[]
        self.res=''
        self.label1.setText('')
        self.label2.setText('')

    def answer(self):
        if not self.res.find('+')==-1:
            k=self.res.split('+')
            num=[int(elem) for elem in k]
            self.values= []
            self.label2.setText('Answer: {}'.format(num[0]+num[1]))
            self.label1.setText('')
        elif not self.res.find('-') == -1:
            k = self.res.split('-')
            num = [int(elem) for elem in k]
            self.values = []
            self.label2.setText('Answer: {}'.format(num[0] - num[1]))
            self.label1.setText('')
        elif not self.res.find('*') == -1:
            k = self.res.split('*')
            num = [int(elem) for elem in k]
            self.values = []
            self.label2.setText('Answer: {}'.format(num[0] * num[1]))
            self.label1.setText('')
        elif not self.res.find('/') == -1:
            k = self.res.split('/')
            num = [int(elem) for elem in k]
            if num[1]==0:
                self.values = []
                self.label2.setText('Division by zero')
            else:
                self.values = []
                self.label2.setText('Answer {}'.format(num[0] /num[1]))
                self.label1.setText('')




if __name__ == '__main__':
    app = QApplication()

    form = Form()
    form.show()

    sys.exit(app.exec_())