import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QAction, qApp, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon
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
        self.resize(700,250)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry() #창의 위치와 크기정보를 가져온다.
        cp = QDesktopWidget().availableGeometry().center() #센터위치 파악
        qr.moveCenter(cp) #창의 프레임을 센터 위치로 이동
        self.move(qr.topLeft()) # 현재 창 전부를 프레임이 있는 곳으로 이동

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())