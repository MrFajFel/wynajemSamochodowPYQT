import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
