from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pickle, random, time

from WorkFunctions import *
from UserInterfaces import *


class basegame():
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

    def checkAnswers(self):
        if self.values == self.correct:
            work_time = (time.time() - self.start)
            result = results(self.menu, self.app, work_time, self.figure, self.size, self.delay, self.whoAmI)
            place = self.frameGeometry()
            place.setY(place.y() + 30)
            result.setGeometry(place)
            self.hide()
            result.show()
            del self
        else:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не всё расставлено верно.")
            error.exec_()

    def fillBoxesByValue(self):
        if self.figure == 0:
            for i in range(len(self.boxes)):
                if self.values[i] == 0:
                    self.boxes[i].setText("")
                    self.makeEmpty(self.boxes[i])
                else:
                    self.boxes[i].setText(str(self.values[i]))
                    self.makeFilled(self.boxes[i])
        else:
            for i in range(len(self.boxes)):
                if self.values[i] == 0:
                    self.boxes[i].setPixmap(QtGui.QPixmap("figures/" + str(self.values[i]) + '.png'))
                    self.makeEmpty(self.boxes[i])
                else:
                    self.boxes[i].setPixmap(QtGui.QPixmap("figures/" + str(self.values[i]) + '.png'))
                    self.makeFilled(self.boxes[i])

    def clickOnBox(self, number):
        if self.selected == None and self.values[number] != 0 and not self.isNowLearn:
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

    def showGame(self):
        for i in range(len(self.boxes)):
            self.boxes[i].show()
        self.ExitLabel.show()
        self.checkButton.show()

    def hideSide(self):
        self.checkButton.hide()
        for i in range(len(self.boxes) // 2, len(self.boxes)):
            self.boxes[i].hide()

    def showSide(self):
        self.checkButton.show()
        for i in range(len(self.boxes) // 2, len(self.boxes)):
            self.boxes[i].show()

    def startGame(self):
        self.showGame()
        self.startButton.hide()
        self.hideSide()
        self.generateShowCorrect()
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(self.delay * 1000, loop.quit)
        loop.exec()

        self.showSide()
        self.startPlaying()
        self.fillBoxesByValue()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        self.menu.setGeometry(place)
        self.hide()
        self.menu.show()
        del self
#todo settings
#todo надпись запоминай
class Game2(QMainWindow, Game2UI, basegame):
    def __init__(self, delay, figure, menu, appp, whoAmI):
        super().__init__()
        self.app = appp
        self.menu = menu
        self.setupUi(self)
        self.delay = delay
        self.whoAmI = whoAmI
        self.figure = figure
        self.size = 2
        self.isNowLearn = False
        self.setFixedSize(800, 600)
        self.boxes = [self.fieldLabel1, self.fieldLabel2, self.fieldLabel3, self.fieldLabel4, self.backLabel1,
                      self.backLabel2, self.backLabel3, self.backLabel4]

        self.startButton = ClickedLabel(self)
        self.startButton.resize(300, 300)
        self.pixmap = QtGui.QPixmap('start.png')
        self.startButton.setPixmap(self.pixmap)
        self.startButton.move(250, 150)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setAlignment(QtCore.Qt.AlignCenter)
        self.ExitLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitLabel.adjustSize()

        self.selected = None
        for i in range(len(self.boxes)):
            self.boxes[i].setAlignment(QtCore.Qt.AlignCenter)
            self.boxes[i].clicked.connect(
                lambda i=i: self.clickOnBox(i)
            )

        for i in range(len(self.boxes)):
            self.boxes[i].hide()
        self.checkButton.hide()

        self.startButton.clicked.connect(lambda: self.startGame())
        self.checkButton.clicked.connect(self.checkAnswers)
        self.ExitLabel.clicked.connect(self.toMain)

    def generateShowCorrect(self):
        answers = [1,2,3,4]
        random.shuffle(answers)
        self.correct = answers + [0,0,0,0]
        self.values = self.correct
        self.fillBoxesByValue()
        self.isNowLearn = True

    def startPlaying(self):
        self.values = [0,0,0,0,1,2,3,4]
        self.fillBoxesByValue()
        self.isNowLearn = False
        self.start = time.time()

class Game3(QMainWindow, Game3UI, basegame):
    def __init__(self, delay, figure, menu, appp, whoAmI):
        super().__init__()
        self.app = appp
        self.menu = menu
        self.setupUi(self)
        self.delay = delay
        self.whoAmI = whoAmI
        self.figure = figure
        self.size = 3
        self.isNowLearn = False
        self.setFixedSize(800, 600)
        self.boxes = [self.fieldLabel1, self.fieldLabel2, self.fieldLabel3, self.fieldLabel4, self.fieldLabel5, self.fieldLabel6, self.fieldLabel7, self.fieldLabel8, self.fieldLabel9,  self.backLabel1,
                      self.backLabel2, self.backLabel3, self.backLabel4,  self.backLabel5,
                      self.backLabel6, self.backLabel7, self.backLabel8, self.backLabel9]

        self.startButton = ClickedLabel(self)
        self.startButton.resize(300, 300)
        self.pixmap = QtGui.QPixmap('start.png')
        self.startButton.setPixmap(self.pixmap)
        self.startButton.move(250, 150)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setAlignment(QtCore.Qt.AlignCenter)
        self.ExitLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitLabel.adjustSize()

        self.selected = None
        for i in range(len(self.boxes)):
            self.boxes[i].setAlignment(QtCore.Qt.AlignCenter)
            self.boxes[i].clicked.connect(
                lambda i=i: self.clickOnBox(i)
            )

        for i in range(len(self.boxes)):
            self.boxes[i].hide()
        self.checkButton.hide()

        self.startButton.clicked.connect(lambda: self.startGame())
        self.checkButton.clicked.connect(self.checkAnswers)
        self.ExitLabel.clicked.connect(self.toMain)

    def generateShowCorrect(self):
        answers = [1,2,3,4,5,6,7,8,9]
        random.shuffle(answers)
        self.correct = answers + [0,0,0,0,0,0,0,0,0]
        self.values = self.correct
        self.fillBoxesByValue()
        self.isNowLearn = True

    def startPlaying(self):
        self.values = [0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9]
        self.fillBoxesByValue()
        self.isNowLearn = False
        self.start = time.time()

class Game4(QMainWindow, Game4UI, basegame):
    def __init__(self, delay, figure, menu, appp, whoAmI):
        super().__init__()
        self.app = appp
        self.menu = menu
        self.setupUi(self)
        self.delay = delay
        self.whoAmI = whoAmI
        self.isNowLearn = False
        self.figure = figure
        self.size = 4
        self.setFixedSize(800, 600)
        self.boxes = [self.fieldLabel1, self.fieldLabel2, self.fieldLabel3, self.fieldLabel4, self.fieldLabel5, self.fieldLabel6, self.fieldLabel7, self.fieldLabel8, self.fieldLabel9, self.fieldLabel10, self.fieldLabel11, self.fieldLabel12, self.fieldLabel13, self.fieldLabel14, self.fieldLabel15, self.fieldLabel16,  self.backLabel1,
                      self.backLabel2, self.backLabel3, self.backLabel4,  self.backLabel5,
                      self.backLabel6, self.backLabel7, self.backLabel8, self.backLabel9, self.backLabel10, self.backLabel11, self.backLabel12,  self.backLabel13,self.backLabel14, self.backLabel15,  self.backLabel16]

        self.startButton = ClickedLabel(self)
        self.startButton.resize(300, 300)
        self.pixmap = QtGui.QPixmap('start.png')
        self.startButton.setPixmap(self.pixmap)
        self.startButton.move(250, 150)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setAlignment(QtCore.Qt.AlignCenter)
        self.ExitLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitLabel.adjustSize()

        self.selected = None
        for i in range(len(self.boxes)):
            self.boxes[i].setAlignment(QtCore.Qt.AlignCenter)
            self.boxes[i].clicked.connect(
                lambda i=i: self.clickOnBox(i)
            )

        for i in range(len(self.boxes)):
            self.boxes[i].hide()
        self.checkButton.hide()

        self.startButton.clicked.connect(lambda: self.startGame())
        self.checkButton.clicked.connect(self.checkAnswers)
        self.ExitLabel.clicked.connect(self.toMain)

    def generateShowCorrect(self):
        answers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        random.shuffle(answers)
        self.correct = answers + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.values = self.correct
        self.fillBoxesByValue()
        self.isNowLearn = True

    def startPlaying(self):
        self.values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        self.fillBoxesByValue()
        self.isNowLearn = False
        self.start = time.time()

#todo иногда крашиться блять просто так, а иногда нет хуй пойми почему
class pregameSettings(QMainWindow, pregameSettingsUI):
    def __init__(self, menu, appp, whoAmI):
        super().__init__()
        self.setupUi(self)
        self.menu = menu
        self.whoAmI = whoAmI
        self.app = appp
        self.setFixedSize(800, 600)
        self.startButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.radioNumbers.setChecked(True)
        self.radioSeconds10.setChecked(True)
        self.radioSize3.setChecked(True)

        self.AuthorizationFrame.move(250, 150)
        self.logo = ClickedLabel(self)
        self.logo.resize(220, 147)
        self.pixmap = QtGui.QPixmap('image.png')
        self.logo.setPixmap(self.pixmap)
        self.logo.move(290, 10)
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close = ClickedLabel(self)
        self.close.resize(75, 75)
        self.pixmap = QtGui.QPixmap('exit.png')
        self.close.setPixmap(self.pixmap)
        self.close.move(725, 525)
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.startButton.clicked.connect(lambda: self.launch())
        self.close.clicked.connect(self.closing)
        self.logo.clicked.connect(self.toMain)

    def launch(self):
        if self.radioSeconds5.isChecked():
            delay = 5
        elif self.radioSeconds10.isChecked():
            delay = 10
        else:
            delay = 20
        if self.radioNumbers.isChecked():
            figure = 0
        else:
            figure = 1
        if self.radioSize2.isChecked():
            game = Game2(delay, figure, self.menu, self.app, self.whoAmI)
        elif self.radioSize3.isChecked():
            game = Game3(delay, figure, self.menu, self.app, self.whoAmI)
        else:
            game = Game4(delay, figure, self.menu, self.app, self.whoAmI)
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        game.setGeometry(place)
        game.show()
        self.hide()

    def closing(self):
        self.app.exit()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        self.menu.setGeometry(place)
        self.hide()
        self.menu.show()
        del self

class results(resultsUI, QMainWindow):
    def __init__(self, menu, appp, time, figure, size, delay, whoAmI):
        super().__init__()
        self.setupUi(self)
        self.figure = figure
        self.whoAmI = whoAmI
        self.setFixedSize(800, 600)
        self.returnButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.menu = menu
        self.delay = delay
        self.app = appp
        self.time = time
        self.size = size

        self.AuthorizationFrame.move(250, 150)
        self.logo = QLabel(self)
        self.logo.resize(220, 147)
        self.pixmap = QtGui.QPixmap('image.png')
        self.logo.setPixmap(self.pixmap)
        self.logo.move(290, 10)
        self.close = ClickedLabel(self)
        self.close.resize(75, 75)
        self.pixmap = QtGui.QPixmap('exit.png')
        self.close.setPixmap(self.pixmap)
        self.close.move(725, 525)
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeLabel.setText("Время: " + str(self.time)[:str(self.time).index(".") + 4] + " сек")

        self.returnButton.clicked.connect(lambda: self.back())
        self.close.clicked.connect(self.closing)
        print(self.whoAmI)
        saveResult(self.time, self.figure, self.size, self.whoAmI, self.delay)


    def back(self):

        place = self.frameGeometry()
        place.setY(place.y() + 30)
        self.menu.setGeometry(place)
        self.hide()
        self.menu.show()
        del self

    def closing(self):
        self.app.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Game4(None, None)
    Form.show()
    sys.exit(app.exec_())
