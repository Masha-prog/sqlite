import sqlite3

import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QStandardItem, QStandardItemModel


names = "ID, название сорта, степень обжарки, молотый/в зернах, описание вкуса, цена, объем упаковки".split(", ")


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connectDB("coffee.sqlite")

    def connectDB(self, dbname):
        con = sqlite3.connect(dbname)
        cur = con.cursor()
        table = list(cur.execute("""SELECT * FROM """))

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(names)
        for row in table:
            items = [QStandardItem(cell) for cell in row]
            self.model.appendRow(items)

        self.tableView.setModel(self.model)
        for i in range(7):
            self.tableView.resizeColumnToContents(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ev = MyWidget()
    ev.show()
    sys.exit(app.exec())







