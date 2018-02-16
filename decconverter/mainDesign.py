# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(303, 191)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 284, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ideal Sans Medium")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.number = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ideal Sans Medium")
        font.setPointSize(14)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.verticalLayout.addWidget(self.number)
        self.answer = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer.setFont(font)
        self.answer.setTextFormat(QtCore.Qt.PlainText)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")
        self.verticalLayout.addWidget(self.answer)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dec2bin = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ideal Sans Medium")
        font.setPointSize(14)
        self.dec2bin.setFont(font)
        self.dec2bin.setObjectName("dec2bin")
        self.verticalLayout_2.addWidget(self.dec2bin)
        self.bin2dec = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ideal Sans Medium")
        font.setPointSize(14)
        self.bin2dec.setFont(font)
        self.bin2dec.setObjectName("bin2dec")
        self.verticalLayout_2.addWidget(self.bin2dec)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Number Converter"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ideal Sans Medium\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please enter a number in the box below that you wish to be converted.  Then press the button that corresponds to the convertion you wish to make.</p></body></html>"))
        self.answer.setText(_translate("MainWindow", "Answer"))
        self.dec2bin.setText(_translate("MainWindow", "Dec 2 Bin"))
        self.bin2dec.setText(_translate("MainWindow", "Bin 2 Dec"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

