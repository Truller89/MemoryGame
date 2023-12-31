from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pickle

from UserInterfaces import *
from WorkFunctions import *
from gameLogicUIs import *

app = QApplication(sys.argv)
key = None
whoAmI = None

class Authorization(QtWidgets.QMainWindow, AuthorizationUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.EnterButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.PasswrodEnterField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginEnterField.setMaxLength(20)
        self.PasswrodEnterField.setMaxLength(20)
        self.ForgetPasswordLabelButton.adjustSize()
        self.RegisterButtonLabel.adjustSize()
        self.SaveMeGAlochka.adjustSize()

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

        with open("saved.bin", "rb") as file:
            data = pickle.load(file)
            if data[0]:
                self.LoginEnterField.setText(data[1])
                self.PasswrodEnterField.setText(data[2])
                self.SaveMeGAlochka.setChecked(data[0])

        self.EnterButton.clicked.connect(self.auth)
        self.RegisterButtonLabel.clicked.connect(self.regs)
        self.ForgetPasswordLabelButton.clicked.connect(self.change)
        self.close.clicked.connect(self.closing)

    def closing(self):
        app.exit()

    def auth(self):
        if login(self.LoginEnterField.text(), self.PasswrodEnterField.text(),  self.SaveMeGAlochka.isChecked()):
            print("Logined")
            global whoAmI
            whoAmI = self.LoginEnterField.text()
            global key
            key = self.PasswrodEnterField.text()
            if not self.SaveMeGAlochka.isChecked():
                self.LoginEnterField.clear()
                self.PasswrodEnterField.clear()
            global menu
            place = self.frameGeometry()
            place.setY(place.y()+30)
            menu.setGeometry(place)
            menu.show()
            self.hide()
        else:
            print("Unknown user")
            self.hide()
            self.LoginEnterField.clear()
            self.PasswrodEnterField.clear()
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Введен неверный логин и/или пароль.")
            error.buttonClicked.connect(lambda: self.show())
            error.exec_()


    def regs(self):
        self.LoginEnterField.clear()
        self.PasswrodEnterField.clear()
        self.reg = Register1()
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        self.reg.setGeometry(place)
        self.reg.show()
        self.hide()

    def change(self):
        self.LoginEnterField.clear()
        self.PasswrodEnterField.clear()
        self.changing = ForgetPassword()
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        self.changing.setGeometry(place)
        self.changing.show()
        self.hide()

auth = Authorization()

class MainMenu(QtWidgets.QMainWindow, MainMenuUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.ButtonStart.setStyleSheet('background: rgb(134, 194, 50);')
        self.ButtonSettings.setStyleSheet('background: rgb(134, 194, 50);')
        self.ButtonExit.setStyleSheet('background: rgb(134, 194, 50);')
        self.ButtonResults.setStyleSheet('background: rgb(134, 194, 50);')

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

        self.ButtonExit.clicked.connect(self.exiting)
        self.close.clicked.connect(self.closing)
        self.ButtonStart.clicked.connect(self.startGame)
        self.ButtonResults.clicked.connect(self.showResults)
        self.ButtonSettings.clicked.connect(self.changePassword)

    def changePassword(self):
        global whoAmI
        if whoAmI != "admin":
            self.changing = ChangePassword(whoAmI)
            place = self.frameGeometry()
            place.setY(place.y() + 30)
            self.changing.setGeometry(place)
            self.changing.show()
            self.hide()
        else:
            print("Not available to administrator")
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Невозможно сменить пароль администратора")
            error.exec_()


    def showResults(self):
        global whoAmI
        if whoAmI == "admin":
            result = allResults(self)
            place = self.frameGeometry()
            place.setY(place.y() + 30)
            result.setGeometry(place)
            self.hide()
            result.show()
        else:
            print("Avaible only for administrator")
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Доступно только администратору")
            error.exec_()

    def startGame(self):
        global whoAmI
        game = pregameSettings(self, app, whoAmI)
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        game.setGeometry(place)
        self.hide()
        game.show()

    def closing(self):
        app.exit()

    def exiting(self):
        global auth
        global key
        key = None
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        auth.setGeometry(place)
        self.hide()
        auth.show()
menu = MainMenu()

class Register1(QtWidgets.QMainWindow, Register1UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.NextButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordField.setMaxLength(20)
        self.LoginField.setMaxLength(20)
        self.NameField.setMaxLength(20)
        self.familyField.setMaxLength(20)
        self.GroupField.setMaxLength(20)

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

        self.NextButton.clicked.connect(self.regs)
        self.logo.clicked.connect(self.toMain)
        self.close.clicked.connect(self.closing)

    def closing(self):
        app.exit()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        auth.setGeometry(place)
        self.hide()
        auth.show()
        del self

    def regs(self):
        if self.NameField.text() != "" and self.familyField.text() != "" and self.GroupField.text() != "" and self.LoginField.text() and self.PasswordField.text() != "" :
            if checkRegister(self.LoginField.text()):
                if len(self.PasswordField.text()) < 8 or not isNumsLettersIn(self.PasswordField.text()):
                    self.hide()
                    error = QtWidgets.QMessageBox()
                    error.setWindowTitle("Пароль слишком простой")
                    error.setText("Пароль должен быть минимум 8 знаков, содержать минимум одну букву и цифру")
                    error.buttonClicked.connect(lambda: self.show())
                    error.exec_()
                else:
                    self.reg = Register2(self.NameField.text(), self.familyField.text(), self.GroupField.text(), self.LoginField.text(), self.PasswordField.text())
                    place = self.frameGeometry()
                    place.setY(place.y() + 30)
                    self.reg.setGeometry(place)
                    self.reg.show()
                    self.hide()
                    del self

            else:
                print("Login already exist")
                self.hide()
                error = QtWidgets.QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Данный логин уже занят")
                error.buttonClicked.connect(lambda: self.show())
                error.exec_()
        else:
            self.hide()
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не все поля заполнены")
            error.buttonClicked.connect(lambda: self.show())
            error.exec_()

class Register2(QtWidgets.QMainWindow, Register2UI):
    def __init__(self, name, surname, group, login, password):
        self.name = name
        self.surname = surname
        self.group = group
        self.login = login
        self.password = password
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.registerButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.MotherField.setMaxLength(20)
        self.CityField.setMaxLength(20)
        self.PetField.setMaxLength(20)

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

        self.registerButton.clicked.connect(self.regs)
        self.logo.clicked.connect(self.toMain)
        self.close.clicked.connect(self.closing)

    def closing(self):
        app.exit()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        auth.setGeometry(place)
        self.hide()
        auth.show()
        del self

    def regs(self):
        if self.MotherField.text() != "" and self.PetField.text() != "" and self.CityField.text() != "":
            global auth
            register(self.login, self.password, self.name, self.surname, self.group, self.MotherField.text(), self.PetField.text(), self.CityField.text())
            place = self.frameGeometry()
            place.setY(place.y() + 30)
            auth.setGeometry(place)
            auth.show()
            self.hide()
            del self
        else:
            self.hide()
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не все поля заполнены")
            error.buttonClicked.connect(lambda: self.show())
            error.exec_()

class ForgetPassword(QtWidgets.QMainWindow, ForgetPasswordUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.nextButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.LoginField.setMaxLength(20)

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

        self.nextButton.clicked.connect(self.answer)
        self.logo.clicked.connect(self.toMain)
        self.close.clicked.connect(self.closing)

    def closing(self):
        app.exit()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        auth.setGeometry(place)
        self.hide()
        auth.show()
        del self

    def answer(self):
        if self.LoginField.text() != "":
            if not checkRegister(self.LoginField.text()):
                self.answers = EnteringAnswers(self.LoginField.text())
                place = self.frameGeometry()
                place.setY(place.y() + 30)
                self.answers.setGeometry(place)
                self.answers.show()
                self.hide()
                del self
            else:
                self.hide()
                error = QtWidgets.QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Данного пользователя не существует")
                error.buttonClicked.connect(lambda: self.show())
                error.exec_()
        else:
            self.hide()
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Не вся поля заполнены")
            error.buttonClicked.connect(lambda: self.show())
            error.exec_()

class EnteringAnswers(QtWidgets.QMainWindow, EnteringAnswersUI):
    def __init__(self, login):
        super().__init__()
        self.login = login
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.finishButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.CityField.setMaxLength(20)
        self.MotherField.setMaxLength(20)
        self.PetField.setMaxLength(20)

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

        self.finishButton.clicked.connect(self.check)
        self.logo.clicked.connect(self.toMain)
        self.close.clicked.connect(self.closing)

    def closing(self):
        app.exit()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        auth.setGeometry(place)
        self.hide()
        auth.show()
        del self

    def check(self):
        if self.MotherField.text() != "" and self.PetField.text() != "" and self.CityField.text() != "" and isCorrectAnswers(self.login, self.MotherField.text(), self.CityField.text(), self.PetField.text()):
            self.changing = ChangePassword(self.login)
            place = self.frameGeometry()
            place.setY(place.y() + 30)
            self.changing.setGeometry(place)
            self.changing.show()
            self.hide()
            del self
        else:
            self.hide()
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Введенные данные не верны")
            error.buttonClicked.connect(lambda: self.show())
            error.exec_()

class ChangePassword(QtWidgets.QMainWindow, ChangePasswordUI):
    def __init__(self, login):
        super().__init__()
        self.login = login
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.finishButton.setStyleSheet('background: rgb(134, 194, 50);')
        self.PassField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassField.setMaxLength(20)

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

        self.finishButton.clicked.connect(self.change)
        self.logo.clicked.connect(self.toMain)
        self.close.clicked.connect(self.closing)

    def closing(self):
        app.exit()

    def toMain(self):
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        auth.setGeometry(place)
        self.hide()
        auth.show()
        del self

    def change(self):
        if len(self.PassField.text()) >= 8 and isNumsLettersIn(self.PassField.text()):
            changePassword(self.login, self.PassField.text())
            global auth
            place = self.frameGeometry()
            place.setY(place.y() + 30)
            auth.setGeometry(place)
            auth.show()
            self.hide()
            del self
        else:
            self.hide()
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пароль должен быть минимум 8 знаков, содержать минимум одну букву и цифру")
            error.buttonClicked.connect(lambda: self.show())
            error.exec_()

class allResults(QtWidgets.QMainWindow, allResultsUI):
    def __init__(self, login):
        super().__init__()
        self.login = login
        self.setupUi(self)
        self.setFixedSize(800,600)
        self.backButton.setStyleSheet('background: rgb(134, 194, 50);')

        self.AuthorizationFrame.move(175, 150)
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

        self.backButton.clicked.connect(lambda : self.toMain())
        self.logo.clicked.connect(self.toMain)
        self.close.clicked.connect(self.closing)

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Участник", "Группа", "Результат", "Режим", "Запоминал", "Элементы"])
        self.fillResult()

    def fillResult(self):
        with open('gameResults\\count.bin', 'rb') as f:
            count = f.read()
        intCount = int(str(count)[2:-1])
        self.tableWidget.setRowCount(intCount)
        global key
        for i in range(intCount):
            with open('gameResults\\game' + str(i) + ".bin", 'rb') as fobj:
                private_key = RSA.import_key(
                    open('private.bin').read(),
                    passphrase=key
                )

                enc_session_key, nonce, tag, ciphertext = [
                    fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
                ]

                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)

                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)

            currentResult = pickle.loads(data)
            with open('usersInfo\\' + str(currentResult.who) + ".bin", 'rb') as fobj:
                private_key = RSA.import_key(
                    open('private.bin').read(),
                    passphrase=key
                )

                enc_session_key, nonce, tag, ciphertext = [
                    fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
                ]

                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)

                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            currentUser = pickle.loads(data)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(currentUser.SurName + " " + currentUser.name[:1] + "."))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(currentUser.Group))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(currentResult.timer) + " cек"))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(currentResult.size))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(currentResult.delay) + " cек"))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(currentResult.figure))



    def closing(self):
        app.exit()

    def toMain(self):
        global menu
        place = self.frameGeometry()
        place.setY(place.y() + 30)
        menu.setGeometry(place)
        self.hide()
        menu.show()
        del self