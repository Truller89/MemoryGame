from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.Qt import pyqtSignal
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()

class AuthorizationUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 261))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(80, 10, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.LoginLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.LoginLabel.setGeometry(QtCore.QRect(10, 60, 71, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.LoginLabel.setPalette(palette)
        self.LoginLabel.setObjectName("LoginLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.PasswordLabel.setGeometry(QtCore.QRect(10, 90, 91, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.PasswordLabel.setPalette(palette)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.SaveMeGAlochka = QtWidgets.QRadioButton(self.AuthorizationFrame)
        self.SaveMeGAlochka.setGeometry(QtCore.QRect(20, 130, 181, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.SaveMeGAlochka.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.SaveMeGAlochka.setFont(font)
        self.SaveMeGAlochka.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveMeGAlochka.setObjectName("SaveMeGAlochka")
        self.EnterButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.EnterButton.setGeometry(QtCore.QRect(90, 160, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        self.EnterButton.setPalette(palette)
        self.EnterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EnterButton.setObjectName("EnterButton")
        self.RegisterButtonLabel = ClickedLabel(self.AuthorizationFrame)
        self.RegisterButtonLabel.setGeometry(QtCore.QRect(20, 190, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.RegisterButtonLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        font.setUnderline(True)
        self.RegisterButtonLabel.setFont(font)
        self.RegisterButtonLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RegisterButtonLabel.setObjectName("RegisterButtonLabel")
        self.ForgetPasswordLabelButton = ClickedLabel(self.AuthorizationFrame)
        self.ForgetPasswordLabelButton.setGeometry(QtCore.QRect(20, 220, 101, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.ForgetPasswordLabelButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        font.setUnderline(True)
        self.ForgetPasswordLabelButton.setFont(font)
        self.ForgetPasswordLabelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ForgetPasswordLabelButton.setObjectName("ForgetPasswordLabelButton")
        self.LoginEnterField = QtWidgets.QLineEdit(self.AuthorizationFrame)
        self.LoginEnterField.setGeometry(QtCore.QRect(100, 60, 151, 24))
        self.LoginEnterField.setAutoFillBackground(False)
        self.LoginEnterField.setObjectName("LoginEnterField")
        self.PasswrodEnterField = QtWidgets.QLineEdit(self.AuthorizationFrame)
        self.PasswrodEnterField.setGeometry(QtCore.QRect(100, 100, 151, 24))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        self.PasswrodEnterField.setPalette(palette)
        self.PasswrodEnterField.setObjectName("PasswrodEnterField")
        self.AuthrroizationLabel.raise_()
        self.LoginLabel.raise_()
        self.PasswordLabel.raise_()
        self.SaveMeGAlochka.raise_()
        self.RegisterButtonLabel.raise_()
        self.ForgetPasswordLabelButton.raise_()
        self.LoginEnterField.raise_()
        self.PasswrodEnterField.raise_()
        self.EnterButton.raise_()
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Авторизация"))
        self.LoginLabel.setText(_translate("Widget", "Логин"))
        self.PasswordLabel.setText(_translate("Widget", "Пароль"))
        self.SaveMeGAlochka.setText(_translate("Widget", "Запомнить меня?"))
        self.EnterButton.setText(_translate("Widget", "Войти"))
        self.RegisterButtonLabel.setText(_translate("Widget", "У меня нет аккаунта."))
        self.ForgetPasswordLabelButton.setText(_translate("Widget", "Забыли пароль?"))

class MainMenuUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 401))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 0, 301, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.AuthrroizationLabel.setFont(font)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.AuthorizationFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonStart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonStart.setObjectName("ButtonStart")
        self.verticalLayout.addWidget(self.ButtonStart)
        self.ButtonResults = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonResults.setObjectName("ButtonResults")
        self.verticalLayout.addWidget(self.ButtonResults)
        self.ButtonSettings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonSettings.setObjectName("ButtonSettings")
        self.verticalLayout.addWidget(self.ButtonSettings)
        self.ButtonExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonExit.setObjectName("ButtonExit")
        self.verticalLayout.addWidget(self.ButtonExit)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Главное меню"))
        self.ButtonStart.setText(_translate("Widget", "Игра памяти"))
        self.ButtonResults.setText(_translate("Widget", "Результаты"))
        self.ButtonSettings.setText(_translate("Widget", "Сменить пароль"))
        self.ButtonExit.setText(_translate("Widget", "Выйти из аккаунта"))

class Register1UI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 401))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 0, 301, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.AuthrroizationLabel.setFont(font)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.formLayoutWidget = QtWidgets.QWidget(self.AuthorizationFrame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 60, 301, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelFamily = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(253, 253, 253))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.labelFamily.setPalette(palette)
        self.labelFamily.setObjectName("labelFamily")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelFamily)
        self.familyField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.familyField.setObjectName("familyField")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.familyField)
        self.labelName = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.labelName.setPalette(palette)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.NameField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NameField.setObjectName("NameField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NameField)
        self.labelGroup = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.labelGroup.setPalette(palette)
        self.labelGroup.setObjectName("labelGroup")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelGroup)
        self.GroupField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.GroupField.setObjectName("GroupField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.GroupField)
        self.labelLogin = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.labelLogin.setPalette(palette)
        self.labelLogin.setObjectName("labelLogin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelLogin)
        self.LoginField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LoginField.setObjectName("LoginField")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LoginField)
        self.labelPassword = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.labelPassword.setPalette(palette)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.PasswordField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.PasswordField.setObjectName("PasswordField")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.PasswordField)
        self.NextButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.NextButton.setGeometry(QtCore.QRect(50, 340, 193, 40))
        self.NextButton.setObjectName("NextButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Регистрация"))
        self.labelFamily.setText(_translate("Widget", "Фамилия"))
        self.labelName.setText(_translate("Widget", "Имя"))
        self.labelGroup.setText(_translate("Widget", "Группа"))
        self.labelLogin.setText(_translate("Widget", "Логин"))
        self.labelPassword.setText(_translate("Widget", "Пароль"))
        self.NextButton.setText(_translate("Widget", "Далее"))

class Register2UI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 10, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.AuthorizationFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MotherLAbel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.MotherLAbel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.MotherLAbel.setFont(font)
        self.MotherLAbel.setObjectName("MotherLAbel")
        self.verticalLayout.addWidget(self.MotherLAbel)
        self.MotherField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.MotherField.setObjectName("MotherField")
        self.verticalLayout.addWidget(self.MotherField)
        self.PetLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.PetLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.PetLabel.setFont(font)
        self.PetLabel.setObjectName("PetLabel")
        self.verticalLayout.addWidget(self.PetLabel)
        self.PetField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PetField.setObjectName("PetField")
        self.verticalLayout.addWidget(self.PetField)
        self.CityLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.CityLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.CityLabel.setFont(font)
        self.CityLabel.setObjectName("CityLabel")
        self.verticalLayout.addWidget(self.CityLabel)
        self.CityField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CityField.setObjectName("CityField")
        self.verticalLayout.addWidget(self.CityField)
        self.registerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Секретные вопросы"))
        self.MotherLAbel.setText(_translate("Widget", "Девичья фамилия вашей матери:"))
        self.PetLabel.setText(_translate("Widget", "Имя первого домашнего питомца:"))
        self.CityLabel.setText(_translate("Widget", "Город, где родился:"))
        self.registerButton.setText(_translate("Widget", "Завершить"))

class ForgetPasswordUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 221))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 10, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.AuthorizationFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CityLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.CityLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.CityLabel.setFont(font)
        self.CityLabel.setObjectName("CityLabel")
        self.verticalLayout.addWidget(self.CityLabel)
        self.LoginField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.LoginField.setObjectName("CityField")
        self.verticalLayout.addWidget(self.LoginField)
        self.nextButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.nextButton.setGeometry(QtCore.QRect(0, 170, 299, 40))
        self.nextButton.setObjectName("registerButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Восстановление"))
        self.CityLabel.setText(_translate("Widget", "Введите ваш логин:"))
        self.nextButton.setText(_translate("Widget", "Далее"))

class EnteringAnswersUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 10, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.AuthorizationFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MotherLAbel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.MotherLAbel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.MotherLAbel.setFont(font)
        self.MotherLAbel.setObjectName("MotherLAbel")
        self.verticalLayout.addWidget(self.MotherLAbel)
        self.MotherField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.MotherField.setObjectName("MotherField")
        self.verticalLayout.addWidget(self.MotherField)
        self.PetLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.PetLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.PetLabel.setFont(font)
        self.PetLabel.setObjectName("PetLabel")
        self.verticalLayout.addWidget(self.PetLabel)
        self.PetField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PetField.setObjectName("PetField")
        self.verticalLayout.addWidget(self.PetField)
        self.CityLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.CityLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.CityLabel.setFont(font)
        self.CityLabel.setObjectName("CityLabel")
        self.verticalLayout.addWidget(self.CityLabel)
        self.CityField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CityField.setObjectName("CityField")
        self.verticalLayout.addWidget(self.CityField)
        self.finishButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.finishButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.finishButton)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Ответь на вопросы"))
        self.MotherLAbel.setText(_translate("Widget", "Девичья фамилия вашей матери:"))
        self.PetLabel.setText(_translate("Widget", "Имя первого домашнего питомца"))
        self.CityLabel.setText(_translate("Widget", "Город, где родился"))
        self.finishButton.setText(_translate("Widget", "Проверить"))

class ChangePasswordUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 221))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 10, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.AuthorizationFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PassLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 242, 255))
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.PassLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.PassLabel.setFont(font)
        self.PassLabel.setObjectName("PassLabel")
        self.verticalLayout.addWidget(self.PassLabel)
        self.PassField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PassField.setObjectName("PassField")
        self.verticalLayout.addWidget(self.PassField)
        self.finishButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.finishButton.setGeometry(QtCore.QRect(0, 170, 299, 40))
        self.finishButton.setObjectName("finishButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Восстановление"))
        self.PassLabel.setText(_translate("Widget", "Введите новый пароль:"))
        self.finishButton.setText(_translate("Widget", "Сменить пароль"))

class Game2UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.ExitLabel = ClickedLabel(Form)
        self.ExitLabel.setGeometry(QtCore.QRect(30, 10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ExitLabel.setFont(font)
        self.ExitLabel.setObjectName("TimeLabel")
        self.backLabel3 = ClickedLabel(Form)
        self.backLabel3.setGeometry(QtCore.QRect(420, 450, 91, 91))
        self.backLabel3.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel3.setText("")
        self.backLabel3.setObjectName("backLabel3")
        self.fieldLabel1 = ClickedLabel(Form)
        self.fieldLabel1.setGeometry(QtCore.QRect(270, 130, 91, 91))
        self.fieldLabel1.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldLabel1.setObjectName("fieldLabel1")
        self.fieldLabel2 = ClickedLabel(Form)
        self.fieldLabel2.setGeometry(QtCore.QRect(450, 130, 91, 91))
        self.fieldLabel2.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldLabel2.setObjectName("fieldLabel2")
        self.backLabel2 = ClickedLabel(Form)
        self.backLabel2.setGeometry(QtCore.QRect(300, 450, 91, 91))
        self.backLabel2.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel2.setText("")
        self.backLabel2.setObjectName("backLabel2")
        self.backLabel4 = ClickedLabel(Form)
        self.backLabel4.setGeometry(QtCore.QRect(540, 450, 91, 91))
        self.backLabel4.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel4.setText("")
        self.backLabel4.setObjectName("backLabel4")
        self.backLabel1 = ClickedLabel(Form)
        self.backLabel1.setGeometry(QtCore.QRect(180, 450, 91, 91))
        self.backLabel1.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel1.setText("")
        self.backLabel1.setObjectName("backLabel1")
        self.fieldLabel3 = ClickedLabel(Form)
        self.fieldLabel3.setGeometry(QtCore.QRect(270, 280, 91, 91))
        self.fieldLabel3.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldLabel3.setObjectName("fieldLabel3")
        self.fieldLabel4 = ClickedLabel(Form)
        self.fieldLabel4.setGeometry(QtCore.QRect(450, 280, 91, 91))
        self.fieldLabel4.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldLabel4.setObjectName("fieldLabel4")
        self.checkButton = ClickedLabel(Form)
        self.checkButton.setGeometry(QtCore.QRect(550, 30, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.checkButton.setFont(font)
        self.checkButton.setStyleSheet("transition: background-color 0.5s;\n"
"font: 22 pt \"Tw Cen MT Condensed Extra Bold\" ;\n"
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
        self.checkButton.setObjectName("checkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MemoryGame"))
        self.ExitLabel.setText(_translate("Form", "Выйти"))
        self.checkButton.setText(_translate("Form", "Проверить"))

class Game3UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.ExitLabel = ClickedLabel(Form)
        self.ExitLabel.setGeometry(QtCore.QRect(30, 10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ExitLabel.setFont(font)
        self.ExitLabel.setObjectName("TimeLabel")
        self.backLabel5 = ClickedLabel(Form)
        self.backLabel5.setGeometry(QtCore.QRect(360, 500, 91, 91))
        self.backLabel5.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel5.setText("")
        self.backLabel5.setObjectName("backLabel5")
        self.backLabel4 = ClickedLabel(Form)
        self.backLabel4.setGeometry(QtCore.QRect(260, 500, 91, 91))
        self.backLabel4.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel4.setText("")
        self.backLabel4.setObjectName("backLabel4")
        self.backLabel6 = ClickedLabel(Form)
        self.backLabel6.setGeometry(QtCore.QRect(460, 500, 91, 91))
        self.backLabel6.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel6.setText("")
        self.backLabel6.setObjectName("backLabel6")
        self.backLabel3 = ClickedLabel(Form)
        self.backLabel3.setGeometry(QtCore.QRect(160, 500, 91, 91))
        self.backLabel3.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel3.setText("")
        self.backLabel3.setObjectName("backLabel3")
        self.checkButton = ClickedLabel(Form)
        self.checkButton.setGeometry(QtCore.QRect(550, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.checkButton.setFont(font)
        self.checkButton.setStyleSheet("transition: background-color 0.5s;\n"
"font: 22 pt \"Tw Cen MT Condensed Extra Bold\" ;\n"
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
        self.checkButton.setObjectName("checkButton")
        self.backLabel2 = ClickedLabel(Form)
        self.backLabel2.setGeometry(QtCore.QRect(60, 500, 91, 91))
        self.backLabel2.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel2.setText("")
        self.backLabel2.setObjectName("backLabel2")
        self.backLabel7 = ClickedLabel(Form)
        self.backLabel7.setGeometry(QtCore.QRect(560, 500, 91, 91))
        self.backLabel7.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel7.setText("")
        self.backLabel7.setObjectName("backLabel7")
        self.backLabel8 = ClickedLabel(Form)
        self.backLabel8.setGeometry(QtCore.QRect(660, 500, 91, 91))
        self.backLabel8.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel8.setText("")
        self.backLabel8.setObjectName("backLabel8")
        self.backLabel9 = ClickedLabel(Form)
        self.backLabel9.setGeometry(QtCore.QRect(660, 400, 91, 91))
        self.backLabel9.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel9.setText("")
        self.backLabel9.setObjectName("backLabel9")
        self.backLabel1 = ClickedLabel(Form)
        self.backLabel1.setGeometry(QtCore.QRect(60, 400, 91, 91))
        self.backLabel1.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel1.setText("")
        self.backLabel1.setObjectName("backLabel1")
        self.fieldLabel1 = ClickedLabel(Form)
        self.fieldLabel1.setGeometry(QtCore.QRect(240, 100, 91, 91))
        self.fieldLabel1.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel1.setText("")
        self.fieldLabel1.setObjectName("fieldLabel1")
        self.fieldLabel2 = ClickedLabel(Form)
        self.fieldLabel2.setGeometry(QtCore.QRect(360, 100, 91, 91))
        self.fieldLabel2.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel2.setText("")
        self.fieldLabel2.setObjectName("fieldLabel2")
        self.fieldLabel3 = ClickedLabel(Form)
        self.fieldLabel3.setGeometry(QtCore.QRect(480, 100, 91, 91))
        self.fieldLabel3.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel3.setText("")
        self.fieldLabel3.setObjectName("fieldLabel3")
        self.fieldLabel4 = ClickedLabel(Form)
        self.fieldLabel4.setGeometry(QtCore.QRect(240, 210, 91, 91))
        self.fieldLabel4.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel4.setText("")
        self.fieldLabel4.setObjectName("fieldLabel4")
        self.fieldLabel5 = ClickedLabel(Form)
        self.fieldLabel5.setGeometry(QtCore.QRect(360, 210, 91, 91))
        self.fieldLabel5.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel5.setText("")
        self.fieldLabel5.setObjectName("fieldLabel5")
        self.fieldLabel6 = ClickedLabel(Form)
        self.fieldLabel6.setGeometry(QtCore.QRect(480, 210, 91, 91))
        self.fieldLabel6.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel6.setText("")
        self.fieldLabel6.setObjectName("fieldLabel6")
        self.fieldLabel9 = ClickedLabel(Form)
        self.fieldLabel9.setGeometry(QtCore.QRect(480, 320, 91, 91))
        self.fieldLabel9.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel9.setText("")
        self.fieldLabel9.setObjectName("fieldLabel9")
        self.fieldLabel8 = ClickedLabel(Form)
        self.fieldLabel8.setGeometry(QtCore.QRect(360, 320, 91, 91))
        self.fieldLabel8.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel8.setText("")
        self.fieldLabel8.setObjectName("fieldLabel8")
        self.fieldLabel7 = ClickedLabel(Form)
        self.fieldLabel7.setGeometry(QtCore.QRect(240, 320, 91, 91))
        self.fieldLabel7.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel7.setText("")
        self.fieldLabel7.setObjectName("fieldLabel7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MemoryGame"))
        self.ExitLabel.setText(_translate("Form", "Выйти"))
        self.checkButton.setText(_translate("Form", "Проверить"))

class Game4UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.ExitLabel = ClickedLabel(Form)
        self.ExitLabel.setGeometry(QtCore.QRect(10, -10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ExitLabel.setFont(font)
        self.ExitLabel.setObjectName("TimeLabel")
        self.backLabel5 = ClickedLabel(Form)
        self.backLabel5.setGeometry(QtCore.QRect(10, 420, 91, 91))
        self.backLabel5.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel5.setText("")
        self.backLabel5.setObjectName("backLabel5")
        self.backLabel4 = ClickedLabel(Form)
        self.backLabel4.setGeometry(QtCore.QRect(10, 330, 91, 91))
        self.backLabel4.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel4.setText("")
        self.backLabel4.setObjectName("backLabel4")
        self.backLabel6 = ClickedLabel(Form)
        self.backLabel6.setGeometry(QtCore.QRect(10, 510, 91, 91))
        self.backLabel6.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel6.setText("")
        self.backLabel6.setObjectName("backLabel6")
        self.backLabel3 = ClickedLabel(Form)
        self.backLabel3.setGeometry(QtCore.QRect(10, 240, 91, 91))
        self.backLabel3.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel3.setText("")
        self.backLabel3.setObjectName("backLabel3")
        self.checkButton = ClickedLabel(Form)
        self.checkButton.setGeometry(QtCore.QRect(610, 0, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.checkButton.setFont(font)
        self.checkButton.setStyleSheet("transition: background-color 0.5s;\n"
"font: 22 pt \"Tw Cen MT Condensed Extra Bold\" ;\n"
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
        self.checkButton.setObjectName("checkButton")
        self.backLabel2 = ClickedLabel(Form)
        self.backLabel2.setGeometry(QtCore.QRect(10, 150, 91, 91))
        self.backLabel2.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel2.setText("")
        self.backLabel2.setObjectName("backLabel2")
        self.backLabel7 = ClickedLabel(Form)
        self.backLabel7.setGeometry(QtCore.QRect(150, 510, 91, 91))
        self.backLabel7.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel7.setText("")
        self.backLabel7.setObjectName("backLabel7")
        self.backLabel8 = ClickedLabel(Form)
        self.backLabel8.setGeometry(QtCore.QRect(290, 510, 91, 91))
        self.backLabel8.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel8.setText("")
        self.backLabel8.setObjectName("backLabel8")
        self.backLabel9 = ClickedLabel(Form)
        self.backLabel9.setGeometry(QtCore.QRect(420, 510, 91, 91))
        self.backLabel9.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel9.setText("")
        self.backLabel9.setObjectName("backLabel9")
        self.backLabel1 = ClickedLabel(Form)
        self.backLabel1.setGeometry(QtCore.QRect(10, 60, 91, 91))
        self.backLabel1.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel1.setText("")
        self.backLabel1.setObjectName("backLabel1")
        self.fieldLabel1 = ClickedLabel(Form)
        self.fieldLabel1.setGeometry(QtCore.QRect(190, 90, 91, 91))
        self.fieldLabel1.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel1.setText("")
        self.fieldLabel1.setObjectName("fieldLabel1")
        self.fieldLabel2 = ClickedLabel(Form)
        self.fieldLabel2.setGeometry(QtCore.QRect(300, 90, 91, 91))
        self.fieldLabel2.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel2.setText("")
        self.fieldLabel2.setObjectName("fieldLabel2")
        self.fieldLabel3 = ClickedLabel(Form)
        self.fieldLabel3.setGeometry(QtCore.QRect(410, 90, 91, 91))
        self.fieldLabel3.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel3.setText("")
        self.fieldLabel3.setObjectName("fieldLabel3")
        self.fieldLabel4 = ClickedLabel(Form)
        self.fieldLabel4.setGeometry(QtCore.QRect(520, 90, 91, 91))
        self.fieldLabel4.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel4.setText("")
        self.fieldLabel4.setObjectName("fieldLabel4")
        self.fieldLabel5 = ClickedLabel(Form)
        self.fieldLabel5.setGeometry(QtCore.QRect(190, 180, 91, 91))
        self.fieldLabel5.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel5.setText("")
        self.fieldLabel5.setObjectName("fieldLabel5")
        self.fieldLabel6 = ClickedLabel(Form)
        self.fieldLabel6.setGeometry(QtCore.QRect(300, 180, 91, 91))
        self.fieldLabel6.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel6.setText("")
        self.fieldLabel6.setObjectName("fieldLabel6")
        self.fieldLabel9 = ClickedLabel(Form)
        self.fieldLabel9.setGeometry(QtCore.QRect(190, 270, 91, 91))
        self.fieldLabel9.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel9.setText("")
        self.fieldLabel9.setObjectName("fieldLabel9")
        self.fieldLabel8 = ClickedLabel(Form)
        self.fieldLabel8.setGeometry(QtCore.QRect(520, 180, 91, 91))
        self.fieldLabel8.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel8.setText("")
        self.fieldLabel8.setObjectName("fieldLabel8")
        self.fieldLabel7 = ClickedLabel(Form)
        self.fieldLabel7.setGeometry(QtCore.QRect(410, 180, 91, 91))
        self.fieldLabel7.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel7.setText("")
        self.fieldLabel7.setObjectName("fieldLabel7")
        self.fieldLabel10 = ClickedLabel(Form)
        self.fieldLabel10.setGeometry(QtCore.QRect(300, 270, 91, 91))
        self.fieldLabel10.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel10.setText("")
        self.fieldLabel10.setObjectName("fieldLabel10")
        self.fieldLabel11 = ClickedLabel(Form)
        self.fieldLabel11.setGeometry(QtCore.QRect(410, 270, 91, 91))
        self.fieldLabel11.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel11.setText("")
        self.fieldLabel11.setObjectName("fieldLabel11")
        self.fieldLabel12 = ClickedLabel(Form)
        self.fieldLabel12.setGeometry(QtCore.QRect(520, 270, 91, 91))
        self.fieldLabel12.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel12.setText("")
        self.fieldLabel12.setObjectName("fieldLabel12")
        self.fieldLabel13 = ClickedLabel(Form)
        self.fieldLabel13.setGeometry(QtCore.QRect(190, 360, 91, 91))
        self.fieldLabel13.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel13.setText("")
        self.fieldLabel13.setObjectName("fieldLabel13")
        self.fieldLabel14 = ClickedLabel(Form)
        self.fieldLabel14.setGeometry(QtCore.QRect(300, 360, 91, 91))
        self.fieldLabel14.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel14.setText("")
        self.fieldLabel14.setObjectName("fieldLabel14")
        self.fieldLabel15 = ClickedLabel(Form)
        self.fieldLabel15.setGeometry(QtCore.QRect(410, 360, 91, 91))
        self.fieldLabel15.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel15.setText("")
        self.fieldLabel15.setObjectName("fieldLabel15")
        self.fieldLabel16 = ClickedLabel(Form)
        self.fieldLabel16.setGeometry(QtCore.QRect(520, 360, 91, 91))
        self.fieldLabel16.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.fieldLabel16.setText("")
        self.fieldLabel16.setObjectName("fieldLabel16")
        self.backLabel10 = ClickedLabel(Form)
        self.backLabel10.setGeometry(QtCore.QRect(560, 510, 91, 91))
        self.backLabel10.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel10.setText("")
        self.backLabel10.setObjectName("backLabel10")
        self.backLabel11 = ClickedLabel(Form)
        self.backLabel11.setGeometry(QtCore.QRect(700, 510, 91, 91))
        self.backLabel11.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel11.setText("")
        self.backLabel11.setObjectName("backLabel11")
        self.backLabel16 = ClickedLabel(Form)
        self.backLabel16.setGeometry(QtCore.QRect(700, 60, 91, 91))
        self.backLabel16.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel16.setText("")
        self.backLabel16.setObjectName("backLabel16")
        self.backLabel15 = ClickedLabel(Form)
        self.backLabel15.setGeometry(QtCore.QRect(700, 150, 91, 91))
        self.backLabel15.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel15.setText("")
        self.backLabel15.setObjectName("backLabel15")
        self.backLabel14 = ClickedLabel(Form)
        self.backLabel14.setGeometry(QtCore.QRect(700, 240, 91, 91))
        self.backLabel14.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel14.setText("")
        self.backLabel14.setObjectName("backLabel14")
        self.backLabel13 = ClickedLabel(Form)
        self.backLabel13.setGeometry(QtCore.QRect(700, 330, 91, 91))
        self.backLabel13.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel13.setText("")
        self.backLabel13.setObjectName("backLabel13")
        self.backLabel12 = ClickedLabel(Form)
        self.backLabel12.setGeometry(QtCore.QRect(700, 420, 91, 91))
        self.backLabel12.setStyleSheet("transition: background-color 0.5s;\n"
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
        self.backLabel12.setText("")
        self.backLabel12.setObjectName("backLabel12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MemoryGame"))
        self.ExitLabel.setText(_translate("Form", "Выйти"))
        self.checkButton.setText(_translate("Form", "Проверить"))

class pregameSettingsUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 5, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 5, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        Widget.setFont(font)
        icon = QtGui.QIcon.fromTheme("face-wink")
        Widget.setWindowIcon(icon)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 381))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AuthrroizationLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AuthrroizationLabel.setGeometry(QtCore.QRect(0, 0, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.AuthrroizationLabel.setPalette(palette)
        self.AuthrroizationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthrroizationLabel.setObjectName("AuthrroizationLabel")
        self.sizeBox = QtWidgets.QGroupBox(self.AuthorizationFrame)
        self.sizeBox.setGeometry(QtCore.QRect(10, 30, 281, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.sizeBox.setPalette(palette)
        self.sizeBox.setObjectName("sizeBox")
        self.radioSize2 = QtWidgets.QRadioButton(self.sizeBox)
        self.radioSize2.setGeometry(QtCore.QRect(20, 50, 91, 22))
        self.radioSize2.setObjectName("radioSize2")
        self.radioSize3 = QtWidgets.QRadioButton(self.sizeBox)
        self.radioSize3.setGeometry(QtCore.QRect(110, 50, 91, 22))
        self.radioSize3.setObjectName("radioSize3")
        self.radioSize4 = QtWidgets.QRadioButton(self.sizeBox)
        self.radioSize4.setGeometry(QtCore.QRect(200, 50, 91, 22))
        self.radioSize4.setObjectName("radioSize4")
        self.timeBox = QtWidgets.QGroupBox(self.AuthorizationFrame)
        self.timeBox.setGeometry(QtCore.QRect(10, 120, 281, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.timeBox.setPalette(palette)
        self.timeBox.setObjectName("timeBox")
        self.radioSeconds5 = QtWidgets.QRadioButton(self.timeBox)
        self.radioSeconds5.setGeometry(QtCore.QRect(10, 50, 91, 22))
        self.radioSeconds5.setObjectName("radioSeconds5")
        self.radioSeconds10 = QtWidgets.QRadioButton(self.timeBox)
        self.radioSeconds10.setGeometry(QtCore.QRect(100, 50, 91, 22))
        self.radioSeconds10.setObjectName("radioSeconds10")
        self.radioSeconds20 = QtWidgets.QRadioButton(self.timeBox)
        self.radioSeconds20.setGeometry(QtCore.QRect(190, 50, 91, 22))
        self.radioSeconds20.setObjectName("radioSeconds20")
        self.elementBox = QtWidgets.QGroupBox(self.AuthorizationFrame)
        self.elementBox.setGeometry(QtCore.QRect(10, 210, 281, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.elementBox.setPalette(palette)
        self.elementBox.setObjectName("elementBox")
        self.radioNumbers = QtWidgets.QRadioButton(self.elementBox)
        self.radioNumbers.setGeometry(QtCore.QRect(10, 50, 91, 22))
        self.radioNumbers.setObjectName("radioNumbers")
        self.radioFIgures = QtWidgets.QRadioButton(self.elementBox)
        self.radioFIgures.setGeometry(QtCore.QRect(160, 40, 111, 41))
        self.radioFIgures.setObjectName("radioFIgures")
        self.startButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.startButton.setGeometry(QtCore.QRect(20, 310, 261, 51))
        self.startButton.setObjectName("startButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AuthrroizationLabel.setText(_translate("Widget", "Настройки"))
        self.sizeBox.setTitle(_translate("Widget", "Размер поля"))
        self.radioSize2.setText(_translate("Widget", "2x2"))
        self.radioSize3.setText(_translate("Widget", "3x3"))
        self.radioSize4.setText(_translate("Widget", "4x4"))
        self.timeBox.setTitle(_translate("Widget", "Время для запоминания"))
        self.radioSeconds5.setText(_translate("Widget", "5сек"))
        self.radioSeconds10.setText(_translate("Widget", "10сек"))
        self.radioSeconds20.setText(_translate("Widget", "20сек"))
        self.elementBox.setTitle(_translate("Widget", "Элементы запоминания"))
        self.radioNumbers.setText(_translate("Widget", "Числа"))
        self.radioFIgures.setText(_translate("Widget", "Фигуры"))
        self.startButton.setText(_translate("Widget", "Начать"))

class resultsUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 5, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 5, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        Widget.setFont(font)
        icon = QtGui.QIcon.fromTheme("face-wink")
        Widget.setWindowIcon(icon)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(250, 100, 301, 191))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.AllDoneLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.AllDoneLabel.setGeometry(QtCore.QRect(0, 0, 301, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.AllDoneLabel.setPalette(palette)
        self.AllDoneLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AllDoneLabel.setObjectName("AllDoneLabel")
        self.returnButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.returnButton.setGeometry(QtCore.QRect(20, 120, 261, 51))
        self.returnButton.setObjectName("returnButton")
        self.timeLabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.timeLabel.setGeometry(QtCore.QRect(0, 60, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.timeLabel.setPalette(palette)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.AllDoneLabel.setText(_translate("Widget", "Всё верно!!!"))
        self.returnButton.setText(_translate("Widget", "Вернуться"))
        self.timeLabel.setText(_translate("Widget", "Время: "))

class allResultsUI(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 5, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 5, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 194, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 227, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 233, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Widget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        Widget.setFont(font)
        icon = QtGui.QIcon.fromTheme("face-wink")
        Widget.setWindowIcon(icon)
        self.AuthorizationFrame = QtWidgets.QFrame(Widget)
        self.AuthorizationFrame.setEnabled(True)
        self.AuthorizationFrame.setGeometry(QtCore.QRect(180, 100, 451, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 75, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.AuthorizationFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.AuthorizationFrame.setFont(font)
        self.AuthorizationFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AuthorizationFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AuthorizationFrame.setLineWidth(300)
        self.AuthorizationFrame.setMidLineWidth(0)
        self.AuthorizationFrame.setObjectName("AuthorizationFrame")
        self.Resultlabel = QtWidgets.QLabel(self.AuthorizationFrame)
        self.Resultlabel.setGeometry(QtCore.QRect(0, 0, 451, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 137, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.Resultlabel.setPalette(palette)
        self.Resultlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultlabel.setObjectName("Resultlabel")
        self.backButton = QtWidgets.QPushButton(self.AuthorizationFrame)
        self.backButton.setGeometry(QtCore.QRect(100, 280, 251, 41))
        self.backButton.setObjectName("backButton")
        self.tableWidget = QtWidgets.QTableWidget(self.AuthorizationFrame)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 371, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "MemoryGame"))
        self.Resultlabel.setText(_translate("Widget", "Результаты"))
        self.backButton.setText(_translate("Widget", "Вернуться"))