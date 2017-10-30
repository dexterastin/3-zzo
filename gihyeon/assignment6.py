import sys

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QPushButton, QTextEdit,
                             QComboBox)

from database import Database


class ScoreDB(QWidget):
    def __init__(self, db):
        super().__init__()

        self.inputComponents = {
            'name': QLineEdit(),
            'age': QLineEdit(),
            'score': QLineEdit(),
            'amount': QLineEdit(),
            'key': QComboBox()
        }

        self.inputComponents['key'].addItem('name')
        self.inputComponents['key'].addItem('score')
        self.inputComponents['key'].addItem('age')

        self.resultComponent = [
            QLabel("result"), QTextEdit()
        ]

        self.db = db

        self.initUI()

    def initUI(self):
        layouts = [QHBoxLayout(), QHBoxLayout(), QVBoxLayout()]

        for layout in layouts:
            layout.addStretch(1)

        # input Box Layout

        for key in self.inputComponents:
            layouts[0].addWidget(QLabel(key + " :"))
            layouts[0].addWidget(self.inputComponents[key])

        # button Group Layout
        btnComponents = [
            QPushButton("Add", self),
            QPushButton("Del", self),
            QPushButton("Find", self),
            QPushButton("Inc", self),
            QPushButton("Show", self)
        ]

        for component in btnComponents:
            component.clicked.connect(self.btnClicked)
            layouts[1].addWidget(component)

        # result Box Layout

        for component in self.resultComponent:
            layouts[2].addWidget(component)

        # vertical Layout
        verticalLayout = QVBoxLayout()
        verticalLayout.addStretch(1)

        for layout in layouts:
            verticalLayout.addLayout(layout)

        self.setLayout(verticalLayout)

        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Assignment6')
        self.show()
        pass

    def btnClicked(self):
        sender = self.sender()
        try:
            stringFormat = {
                'add': "{0} {1} {2} {3}".format('add', self.inputComponents['age'].text(),
                                                self.inputComponents['name'].text(),
                                                self.inputComponents['score'].text()),
                'del': "{0} {1}".format('del', self.inputComponents['name'].text()),
                'find': "{0} {1}".format('find', self.inputComponents['name'].text()),
                'inc': "{0} {1} {2}".format('inc', self.inputComponents['name'].text(),
                                            self.inputComponents['amount'].text()),
                'show': "{0}".format('show')
            }
            user_input = "{0} {1}".format(stringFormat[sender.text().lower()],
                                          self.inputComponents['key'].currentText())
            print(user_input)

            k = db.run(user_input)
            print(k)
            self.resultComponent[1].setFontWeight(100)
            self.resultComponent[1].append("Command => {0}".format(user_input))
            self.resultComponent[1].setFontWeight(1)
            for row in k:
                result = ""
                for info in row:
                    result += "{0}={1}\t\t".format(str(info), str(row[info]))
                self.resultComponent[1].append(result)

            self.resultComponent[1].append('\n')
            pass
        except Exception as e:
            self.resultComponent[1].append(e.__str__())
        pass

    def closeEvent(self, event):
        db.quit_db()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = Database("20171648-양기현-assignment3.dat")
    ex = ScoreDB(db)
    sys.exit(app.exec_())
