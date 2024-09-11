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

        checkbox = QLabel("Variantlarni tanlang:")
        self.checkbox1 = QCheckBox("Variant1")
        self.checkbox2 = QCheckBox("Variant2")
        self.checkbox3 = QCheckBox("Variant3")

        radio = QLabel("Variantni tanlang:")
        self.radio1 = QRadioButton("VariantA")
        self.radio2 = QRadioButton("VariantB")

        self.btnSubmit = QPushButton("Yakunlash")

        mainLayout.addWidget(checkbox)
        mainLayout.addWidget(self.checkbox1)
        mainLayout.addWidget(self.checkbox2)
        mainLayout.addWidget(self.checkbox3)

        mainLayout.addWidget(radio)
        mainLayout.addWidget(self.radio1)
        mainLayout.addWidget(self.radio2)

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

        information = QMessageBox()
        information.setIcon(QMessageBox.Icon.Information)
        information.setText(f"Siz kiritgan checkboxlar:\n{"Yo'q" if len(checkboxes) == 0 else checkboxes}\n\nSiz kiritgan radio:\n{"Yo'q" if radio is None else radio}")
        information.setStandardButtons(QMessageBox.StandardButton.Ok)

        information.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec_()