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
        MainWindow.resize(408, 176)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.formPage = QtWidgets.QWidget()
        self.formPage.setObjectName("formPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.formPage)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nameLbl = QtWidgets.QLabel(self.formPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLbl.sizePolicy().hasHeightForWidth())
        self.nameLbl.setSizePolicy(sizePolicy)
        self.nameLbl.setMinimumSize(QtCore.QSize(100, 35))
        self.nameLbl.setMaximumSize(QtCore.QSize(100, 35))
        self.nameLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLbl.setObjectName("nameLbl")
        self.horizontalLayout_3.addWidget(self.nameLbl)
        self.nameEdit = QtWidgets.QLineEdit(self.formPage)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_3.addWidget(self.nameEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subjectLbl = QtWidgets.QLabel(self.formPage)
        self.subjectLbl.setMinimumSize(QtCore.QSize(100, 35))
        self.subjectLbl.setMaximumSize(QtCore.QSize(100, 35))
        self.subjectLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.subjectLbl.setObjectName("subjectLbl")
        self.horizontalLayout_2.addWidget(self.subjectLbl)
        self.subjectEdit = QtWidgets.QLineEdit(self.formPage)
        self.subjectEdit.setObjectName("subjectEdit")
        self.horizontalLayout_2.addWidget(self.subjectEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.submitBtn = QtWidgets.QPushButton(self.formPage)
        self.submitBtn.setObjectName("submitBtn")
        self.horizontalLayout.addWidget(self.submitBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.resetBtn = QtWidgets.QPushButton(self.formPage)
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout.addWidget(self.resetBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.formPage)
        self.successPage = QtWidgets.QWidget()
        self.successPage.setObjectName("successPage")
        self.successText = QtWidgets.QTextBrowser(self.successPage)
        self.successText.setGeometry(QtCore.QRect(0, 10, 341, 121))
        self.successText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.successText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.successText.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.successText.setObjectName("successText")
        self.stackedWidget.addWidget(self.successPage)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLbl.setText(_translate("MainWindow", "Name"))
        self.subjectLbl.setText(_translate("MainWindow", "Subject"))
        self.submitBtn.setText(_translate("MainWindow", "Submit"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.successText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Your submission was successful</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

