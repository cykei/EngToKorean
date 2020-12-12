import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QCoreApplication
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        btn = QPushButton('Quit',self) #(버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("EngToKorean")
        self.setGeometry(300,300,700,250)
        self.show()

if __name__ == '__main__':
    #__nam__ = 현재 모듈의 이름이 저장되는 내장 변수수
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())