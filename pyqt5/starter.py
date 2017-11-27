import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.Qt import QLabel


class OurGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI App')
        self.addMenuStatus()
        self.positionalWidgetLayout()


    def positionalWidgetLayout(self):
        label_1 = QLabel('Label ONE', self)

        print(self.menuBar().size())
        mBarHeight = self.menuBar().height()
        print(mBarHeight)
        label_1.move(10, mBarHeight)

        label_2 = QLabel('Label TWO', self)
        label_2.move(10, mBarHeight * 2)

    def addMenuStatus(self):
        self.statusBar().showMessage('Status Bar Text')
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        new_action = QAction('New', self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('New File')

        file_menu.addSeparator()

        exit_action = QAction('Exit', self)    # create Exit Action
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.resize(400,300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = OurGUI()
    gui.show()
    sys.exit(app.exec_())