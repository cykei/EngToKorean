import sys
import time
import pyperclip

from PyQt5.QtWidgets import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.text_edit = QLineEdit(self)
        self.copy_button = QPushButton("copy", self)
        self.reset_button = QPushButton("reset", self)
        self.copy_button.clicked.connect(self.copyText)
        self.reset_button.clicked.connect(self.resetText)
        self.body_boxlayout()


    def initUI(self):
        ## 메뉴바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        aboutAction = QAction('About', self)

        helpmenu = menubar.addMenu('&Help')
        helpmenu.addAction(aboutAction)

        ## 상태바
        self.statusBar().showMessage('Ready')

        ## 전체 창
        self.setWindowTitle("EngToKorean")
        self.resize(700,250)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def body_boxlayout(self):

        hbox_input = QHBoxLayout()
        hbox_input.addWidget(QLabel('Text:'))
        hbox_input.addWidget(self.text_edit)

        hbox_button = QHBoxLayout()
        hbox_button.addStretch(1)
        hbox_button.addWidget(self.copy_button)
        hbox_button.addWidget(self.reset_button)
        hbox_button.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_input)
        vbox.addLayout(hbox_button)
        vbox.addStretch(2)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def copyText(self):
        lineText = self.text_edit.text()
        pyperclip.copy(lineText)
        self.text_edit.selectAll()

    def resetText(self):
        self.text_edit.clear()

if __name__ == '__main__':
    start = time.time()
    app = QApplication(sys.argv)
    ex = MyApp()
    print("time: ", time.time() - start)
    sys.exit(app.exec_())
