from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox, QLabel)      # QLabel 추가
from PyQt5.QtGui import QIcon, QFont        # QFont 추가
from PyQt5 import QtCore


class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.lbl1 = QLabel('v2.3.0', self)      # 버전 정보 표시를 위한 lbl1 위젯 생성
        self.lbl1.setFont(QFont('Consolas', 10))        # 폰트 설정 추가, Consolas, 사이즈 10
        self.btn1=QPushButton('Calc',self)
        self.btn2=QPushButton('Clear',self)
        
        self.le1=QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus(True)
        self.le1.selectAll()
        
        self.le2=QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        
        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/', '^', '%'])     # % 연산자 추가
        
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl1)       # 버전 정보 표시를 위한 lbl1 위젯 생성
        # hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
        
    def setDisplay(self, text):     # 함수명 변경
        self.te1.appendPlainText(text)
        
    def clearMessage(self):
        self.te1.clear()