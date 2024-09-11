from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setting()
        self.UI()
        self.eventHandler()

    def setting(self):
        self.setGeometry(340, 200, 680, 400)
        self.setWindowTitle("")
        self.show()

    def UI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        mainLayout = QVBoxLayout()
        miniLayout1 = QHBoxLayout()
        miniLayout2 = QHBoxLayout()
        miniLayout3 = QHBoxLayout()
        miniLayout4 = QHBoxLayout()

        label1 = QLabel("Ismingiz:")
        self.edit1 = QLineEdit(self)
        label2 = QLabel("Familiya:")
        self.edit2 = QLineEdit(self)
        label3 = QLabel("Elektron pochta:")
        self.edit3 = QLineEdit(self)
        label4 = QLabel("Parol:")
        self.edit4 = QLineEdit(self)

        self.btnEnd = QPushButton("Yakunlash")
        

        miniLayout1.addWidget(label1)
        miniLayout1.addWidget(self.edit1)
        miniLayout2.addWidget(label2)
        miniLayout2.addWidget(self.edit2)
        miniLayout3.addWidget(label3)
        miniLayout3.addWidget(self.edit3)
        miniLayout4.addWidget(label4)
        miniLayout4.addWidget(self.edit4)

        mainLayout.addLayout(miniLayout1)
        mainLayout.addLayout(miniLayout2)
        mainLayout.addLayout(miniLayout3)
        mainLayout.addLayout(miniLayout4)

        mainLayout.addWidget(self.btnEnd)

        centralWidget.setLayout(mainLayout)

    def eventHandler(self):
        self.btnEnd.clicked.connect(lambda: self.btnEndClicked())

    def btnEndClicked(self): 
        if self.edit1.text() == "" or self.edit2.text() == "" or self.edit3.text() == "" or self.edit4.text() == "":
            warning = QMessageBox()
            warning.warning(self, "warning", "Barcha ma'lumotlar kiritilmagan", QMessageBox.StandardButton.Ok)
        else:
            information = QMessageBox()
            information.setIcon(QMessageBox.Icon.Information)
            information.setText(f"Ma'lumotlaringizni tasdiqlang:\nIsmingiz: {self.edit1.text()}\nFamiliyangiz: {self.edit2.text()}\nElektron pochtangiz: {self.edit3.text()}\nParolingiz: {self.edit4.text()}\n\n\nBarcha ma'lumotlaringiz to'g'rimi?")
            information.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            information.buttonClicked.connect(self.btnClicked)
            information.exec_()

    def btnClicked(self, btn):
        if btn.text() == "OK":
            print(f"Ismingiz: {self.edit1.text()}\nFamiliyangiz: {self.edit2.text()}\nElektron pochtangiz: {self.edit3.text()}\nParolingiz: {self.edit4.text()}")
            self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec_()