from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QCheckBox, QRadioButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setting()
        self.UI()
        self.eventHandler()

    def setting(self):
        self.setGeometry(340, 200, 680, 400)
        self.setWindowTitle("Dastur")
        self.show()

    def UI(self):
        centralWidget = QWidget()
        mainLayout = QVBoxLayout()
        centralWidget.setLayout(mainLayout)

        radio = QLabel("Sizning sevimli rangiz qaysi?")
        self.radio1 = QRadioButton("Qizil")
        self.radio2 = QRadioButton("Ko'k")
        self.radio3 = QRadioButton("Yashil")
        self.radio4 = QRadioButton("Sariq")

        checkbox = QLabel("Sizda qaysi hayvon bor?")
        self.checkbox1 = QCheckBox("Mushuk")
        self.checkbox2 = QCheckBox("It")
        self.checkbox3 = QCheckBox("Quyon")
        self.checkbox4 = QCheckBox("Baliq")

        self.btnSubmit = QPushButton("Yakunlash")

        mainLayout.addWidget(radio)
        mainLayout.addWidget(self.radio1)
        mainLayout.addWidget(self.radio2)
        mainLayout.addWidget(self.radio3)
        mainLayout.addWidget(self.radio4)

        mainLayout.addWidget(checkbox)
        mainLayout.addWidget(self.checkbox1)
        mainLayout.addWidget(self.checkbox2)
        mainLayout.addWidget(self.checkbox3)
        mainLayout.addWidget(self.checkbox4)

        mainLayout.addWidget(self.btnSubmit)

        self.setCentralWidget(centralWidget)

    def eventHandler(self):
        self.btnSubmit.clicked.connect(lambda: self.btnSubmitClicked())

    def btnSubmitClicked(self):
        radio = None
        if self.radio1.isChecked():
            radio = self.radio1.text() 
        elif self.radio2.isChecked(): 
            radio = self.radio2.text()
        elif self.radio3.isChecked(): 
            radio = self.radio3.text()
        elif self.radio4.isChecked(): 
            radio = self.radio4.text()

        checkboxes = ""

        if self.checkbox1.checkState():
            checkboxes += self.checkbox1.text()
            checkboxes += '\n'
        if self.checkbox2.checkState():
            checkboxes += self.checkbox2.text()
            checkboxes += '\n'
        if self.checkbox3.checkState():
            checkboxes += self.checkbox3.text()
            checkboxes += '\n'
        if self.checkbox4.checkState():
            checkboxes += self.checkbox4.text()
            checkboxes += '\n'

        information = QMessageBox()
        information.setIcon(QMessageBox.Icon.Information)
        information.setText(f"Siz yoqtirgan rang:\n{"Yo'q" if radio is None else radio}\n\n\nSizda bor uy hayvonlari:\n{"Yo'q" if len(checkboxes) == 0 else checkboxes}")
        information.setStandardButtons(QMessageBox.StandardButton.Ok)

        information.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec_()