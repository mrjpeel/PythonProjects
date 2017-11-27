from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QUrl
import sys
import mainDesign

class WebViewer(QMainWindow, mainDesign.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_button)

    def push_button(self):
        print("Button pressed")
        newURL = self.lineEdit.text()
        print("the New URL will be", newURL)

        self.webView.setUrl(QUrl("http://" + newURL))


def main():
    app = QApplication(sys.argv)
    window = WebViewer()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
