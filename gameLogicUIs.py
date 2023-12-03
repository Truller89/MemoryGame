from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pickle, random, time

from UserInterfaces import *
from WorkFunctions import *

class Game2(QMainWindow, Game2UI):
    def __init__(self, delay):
        super().__init__()
        self.setupUi(self)
        self.delay = delay
        self.setFixedSize(800, 600)
        self.boxes = [self.fieldLabel1, self.fieldLabel2, self.fieldLabel3, self.fieldLabel4, self.backLabel1, self.backLabel2, self.backLabel3, self.backLabel4]

        self.startButton = ClickedLabel(self)
        self.startButton.resize(300, 300)
        self.pixmap = QtGui.QPixmap('start.png')
        self.startButton.setPixmap(self.pixmap)
        self.startButton.move(250, 150)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.selected = None
        for i in range(len(self.boxes)):
            self.boxes[i].setAlignment(QtCore.Qt.AlignCenter)
            self.boxes[i].clicked.connect(
                    lambda i=i: self.clickOnBox(i)
                )

        for i in range(len(self.boxes)):
            self.boxes[i].hide()
        self.TimeLabel.hide()
        self.checkButton.hide()

        self.startButton.clicked.connect(self.startGame)
        self.checkButton.clicked.connect(self.checkAnswers)

    def showGame(self):
        for i in range(len(self.boxes)):
            self.boxes[i].show()
        self.TimeLabel.show()
        self.checkButton.show()

    def startGame(self):
        self.showGame()
        self.startButton.hide()
        self.generateShowCorrect()
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(self.delay * 1000, loop.quit)
        loop.exec()
        self.startPlaying()
        self.fillBoxesByValue()

    def generateShowCorrect(self):
        answers = [1,2,3,4]
        random.shuffle(answers)
        self.correct = answers + [0,0,0,0]
        self.values = self.correct
        self.fillBoxesByValue()


    def startPlaying(self):
        self.values = [0, 0, 0, 0, 1, 2, 3, 4]
        self.fillBoxesByValue()

    def checkAnswers(self):
        if self.values == self.correct:
            print("ok")
        else:
            print("Nope")

    def fillBoxesByValue(self):
        for i in range(len(self.boxes)):
            if self.values[i] == 0:
                self.boxes[i].setText("")
                self.makeEmpty(self.boxes[i])
            else:
                self.boxes[i].setText(str(self.values[i]))
                self.makeFilled(self.boxes[i])

    def clickOnBox(self, number):
        if self.selected == None and self.values[number] != 0:
            self.selected = number
            self.makeSelected(self.boxes[number])
        elif self.selected == number:
            self.selected = None
            self.makeFilled(self.boxes[number])
        elif self.selected != None:
            buffer = self.values[number]
            self.values[number] = self.values[self.selected]
            self.values[self.selected] = buffer
            self.selected = None
            self.fillBoxesByValue()

    #def generateAnswers(self):

    def makeEmpty(self, box):
        box.setStyleSheet("transition: background-color 0.5s;\n"
"  margin-bottom: 10px;\n"
"  padding: 5px;\n"
"\n"
"  text-align: center;\n"
"  border: 4px ridge #71A429;\n"
"  border-radius: 10px;\n"
"  cursor: move;\n"
"  background-color: #86c232;\n"
"\n"
"  transition: background-color 0.5s;")
    def makeFilled(self, box):
        box.setStyleSheet("transition: background-color 0.5s;\n"
"font: 42pt \"Tw Cen MT Condensed Extra Bold\" ;\n"
"color: #ffF;\n"
"  margin-bottom: 10px;\n"
"  padding: 5px;\n"
"\n"
"  text-align: center;\n"
"  border: 5px groove #A6ED44;\n"
"  border-radius: 10px;\n"
"  cursor: move;\n"
"  background-color: #A6ED44;\n"
"\n"
"  transition: background-color 0.5s;")
    def makeSelected(self, box):
        box.setStyleSheet("transition: background-color 0.5s;\n"
"font: 42pt \"Tw Cen MT Condensed Extra Bold\" ;\n"
"color: #ffF;\n"
"\n"
"  margin-bottom: 10px;\n"
"  padding: 5px;\n"
"\n"
"  text-align: center;\n"
"  border: 5px double #fff;\n"
"  border-radius: 10px;\n"
"  cursor: move;\n"
"  background-color: #A6ED44;\n"
"\n"
"  transition: background-color 0.5s;")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Game2()
    Form.show()
    sys.exit(app.exec_())
