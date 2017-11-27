from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import mainDesign


class ExamForm(QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.submitBtn.clicked.connect(self.submit)
        self.resetBtn.clicked.connect(self.reset)

    def submit(self):
        nameentry = self.nameEdit.text()
        subjectentry = self.subjectEdit.text()

        html = '''
        <div style="font-family:Calibri">
            <h1>Thank You!</h1>
            <img src="tick.png" style="float:right">
            <p style="font-size:16px">
                <b> ''' + nameentry + '''</b> Your submission was successful \n
                You have now been entered for the exam in <i>''' + subjectentry + '''</i>
            </p>
        <div>'''

        if nameentry == "" or subjectentry =="":
            self.nameLbl.setStyleSheet("color: red")
            self.nameEdit.setStyleSheet("background-color: red")
            self.subjectEdit.setStyleSheet("background-color: red")
            self.subjectLbl.setStyleSheet("color: red")
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.successText.setHtml(html)
            self.successText.setStyleSheet("background-color: #efefef")

    def reset(self):
        self.nameEdit.setText("")
        self.nameLbl.setStyleSheet("color: #000000")
        self.nameEdit.setStyleSheet("background-color: none")
        self.subjectEdit.setText("")
        self.subjectLbl.setStyleSheet("color: #000000")
        self.subjectEdit.setStyleSheet("background-color: none")


def main():
    app = QApplication(sys.argv)
    form = ExamForm()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()