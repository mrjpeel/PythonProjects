from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys
import mainDesign
import convert


class Converter(QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.filePicker)
        self.pushButton_2.clicked.connect(self.confirm)

    def filePicker(self):
        fileName = QFileDialog().getOpenFileName()

        print('The selected file is', fileName[0])
        self.lineEdit.setText(fileName[0])

    def confirm(self):
        newFileName = self.lineEdit_2.text()
        print('newfilename', newFileName)
        print('Confirm')


def main():
    app = QApplication(sys.argv)
    gui = Converter()
    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()
