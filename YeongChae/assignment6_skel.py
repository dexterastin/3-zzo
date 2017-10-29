import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.keyname = 'Name'
        self.name = ""
        self.score = ""
        self.age = ""
        self.amount = ""
        self.readScoreDB()
       	self.showScoreDB()
        
        
    def initUI(self):

        name = QLabel('Name:') 
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        nameEdit = QLineEdit(self)
        nameEdit.textChanged.connect(self.setName)
        ageEdit = QLineEdit(self)
        ageEdit.textChanged.connect(self.setAge)
        scoreEdit = QLineEdit(self)
        scoreEdit.textChanged.connect(self.setScore)
        amountEdit = QLineEdit(self)
        amountEdit.textChanged.connect(self.setAmount)
        self.resultEdit = QTextEdit(self)

        combo = QComboBox(self)
        combo.addItem('Name')
        combo.addItem('Age')
        combo.addItem('Score')
        combo.activated[str].connect(self.keydetector)

        add = QPushButton("Add",self)
        add.clicked.connect(self.operateAdd)
        dele = QPushButton("Del",self)
        dele.clicked.connect(self.operateDele)
        find = QPushButton("Find",self)
        find.clicked.connect(self.operateFind)
        inc = QPushButton("Inc",self)
        inc.clicked.connect(self.operateInc)
        show = QPushButton("Show",self)
        show.clicked.connect(self.showScoreDB)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(name, 0, 0)
        grid.addWidget(nameEdit, 0, 1)

        grid.addWidget(age, 0, 2)
        grid.addWidget(ageEdit, 0, 3)

        grid.addWidget(score, 0, 4)
        grid.addWidget(scoreEdit, 0, 5)

        grid.addWidget(amount, 1, 2)
        grid.addWidget(amountEdit, 1, 3)
	
        grid.addWidget(key, 1, 4)
        grid.addWidget(combo, 1, 5)

        grid.addWidget(add, 2, 1)
        grid.addWidget(dele, 2, 2)
        grid.addWidget(find, 2, 3)
        grid.addWidget(inc, 2, 4)
        grid.addWidget(show, 2, 5)

        grid.addWidget(result, 3, 0)
        grid.addWidget(self.resultEdit, 4, 0, 7, 7)
        
        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()


    def closeEvent(self, event):
        self.writeScoreDB()

    def keydetector(self, text):
        self.keyname = text

    def setAge(self, text):
        self.age = text

    def setName(self,text):
        self.name = text

    def setScore(self,text):
        self.score = text

    def setAmount(self,text):
        self.amount = text

    def operateAdd(self):
        name = self.name
        age = self.age
        score = self.score
        record = {'Name': name, 'Age' : age, 'Score': score}
        self.scoredb += [record]
        self.showScoreDB()

    def operateDele(self):
        idx = 0
        name = self.name
        while idx < len(self.scoredb):
            if self.scoredb[idx]['Name'] == name:
                self.scoredb.remove(self.scoredb[idx])
            else:
                idx += 1
        self.showScoreDB()

    def operateFind(self):
        string = ''
        name = self.name
        for d in self.scoredb:
            if d['Name'] == name:
                string += 'Name :  '+d['Name']+",  "+"Age :  "+str(d["Age"])+',  '+"Score :  "+str(d["Score"])
                string += '\n'
        self.resultEdit.setText(string)

    def operateInc(self):
        name = self.name
        amount = self.amount
        idx = 0
        while idx < len(self.scoredb):
            if self.scoredb[idx]['Name'] == name:
                self.scoredb[idx]['Score'] += int(amount)
                idx +=1
            else:
                idx +=1
        self.showScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        print(self.scoredb)
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        string = ''       
        for p in sorted(self.scoredb, key=lambda person : person[self.keyname]):
            for attr in sorted(p):
                string += attr +  " = " + str(p[attr]) + "        "
            string += "\n"
        self.resultEdit.setText(string)
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





