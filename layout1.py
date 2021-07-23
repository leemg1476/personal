import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import process

class MainWiondw(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 512
        self.height = 512

        self.store = set()
        self.start_pos_x = QDesktopWidget().availableGeometry().width()
        self.HOT_KEYS = {
            'show_red': set([Qt.Key_Alt, Qt.Key_1])}



        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.width, self.height)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QLabel(self.centralwidget)
        pixmap = QPixmap(r"C:\Users\LeeMyeonggyu\PycharmProjects\personal\image\blue.png")
        self.left = (self.width - pixmap.width()) // 2
        self.top = (self.height - pixmap.height()) // 2
        self.label.setGeometry(QRect(self.left,self.top,pixmap.width(),pixmap.height()))
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap(r"C:\Users\LeeMyeonggyu\PycharmProjects\personal\image\blue.png"))  # image path

        self.move(int(self.start_pos_x)-int(pixmap.width())-int(self.left),0-int(self.top))
        print(0-int(pixmap.height())-int(self.top))


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # Change mouse icon

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # Change window position
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def show_red(self):
        self.label.setPixmap(QPixmap(r"C:\Users\LeeMyeonggyu\PycharmProjects\personal\image\red.png"))

    def keyPressEvent(self, e):
        self.store.add(e.key())

        for action, trigger in self.HOT_KEYS.items():
            CHECK = all([True if triggerKey in self.store else False for triggerKey in trigger])

            if CHECK:
                if action == "show_red":
                    self.show_red()

    def keyReleaseEvent(self, e):
        if e.key() in self.store:
            self.store.remove(e.key())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWiondw()
    w.show()

    sys.exit(app.exec_())

