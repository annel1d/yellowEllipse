import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.draw_ellipse)

    def draw_ellipse(self):
        self.update()

    def paintEvent(self, event):
        QMainWindow.paintEvent(self, event)
        k = 0
        painter = QPainter(self)
        pen = QPen(Qt.black, 1)
        painter.setPen(pen)
        painter.setBrush(Qt.yellow)
        while k < 3:
            a = randint(1, 200)
            painter.drawEllipse(randint(0, 800), randint(0, 500), a, a)
            k += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
