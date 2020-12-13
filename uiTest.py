import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QAction, qApp

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ## 메뉴바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) # mac os 에서도 동일하게 나온다.

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        filemenu = menubar.addMenu('&File') # Alt + F 가 File 메뉴의 단축키가 된다.
        filemenu.addAction(exitAction)

        aboutAction = QAction('About', self)

        helpmenu = menubar.addMenu('&Help')
        helpmenu.addAction(aboutAction)

        ## 상태바
        self.statusBar().showMessage('Ready')

        ## 버튼
        btn = QPushButton('Quit',self) #(버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(qApp.quit)

        ## 전체 창
        self.setWindowTitle("EngToKorean")
        self.setGeometry(300,300,700,250)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())