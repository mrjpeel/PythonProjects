from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtCore import QUrl, Qt
import sys
import mainDesign

class GlobalMem: pass

class NumConvertor(QMainWindow, mainDesign.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.dec2bin.clicked.connect(lambda dec = self.number.text(): self.dec_2_bin(dec))
        self.bin2dec.clicked.connect(self.bin_2_dec)


    def dec_2_bin(self, dec):

        print(dec)
        def convertnum(self, dec):
            if dec > 1:
                self.convertnum(dec // 2)

            theAnswer = dec % 2
            print(theAnswer)
            self.answer.setText(theAnswer)

    def dec_2_bin(self):

        dec = self.number.text()
        num = self.convertNum(self, dec)
        self.answer.setText(num)

    def bin_2_dec(self):
        pass


def main():
    app = QApplication(sys.argv)
    appClass = NumConvertor()
    appClass.show()
    app.exec_()


if __name__ == '__main__':
    main()