from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QRadioButton, QCheckBox, QVBoxLayout, QHBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setting()
        self.UI()

    def setting(self):
        self.setGeometry(340, 200, 680, 400)
        self.setWindowTitle("Sahifa")
        self.show()

    def UI(self):
        self.mainLayout = QVBoxLayout()
        self.miniLayout1 = QHBoxLayout()
        self.miniLayout2 = QHBoxLayout()
        self.miniLayout3 = QVBoxLayout()

        self.firstName = QLineEdit()
        self.firstName.setPlaceholderText("Ismingizni kiriting")

        self.lastName = QLineEdit()
        self.lastName.setPlaceholderText("Familiyangizni kiriting")

        age = QLabel("Yoshingiz:")

        self.age1 = QRadioButton("0-18")
        self.age2 = QRadioButton("19-25")
        self.age3 = QRadioButton("26-80")
        self.age4 = QRadioButton("81-...")
        
        region = QLabel("Viloyat:")

        self.region = QComboBox()
        self.region.addItems(['', 'Andijon', "Farg'ona", "Namangan"])

        proglan = QLabel("Dasturlash tillari:")

        self.proglan1 = QCheckBox("Python")
        self.proglan2 = QCheckBox("Java")
        self.proglan3 = QCheckBox("Javascript")
        self.proglan4 = QCheckBox("Go")
        self.proglan5 = QCheckBox("C++")

        self.btnSend = QPushButton("YAKUNLASH")
        self.btnSend.clicked.connect(lambda: self.btnClicked())
        


        self.miniLayout1.addWidget(self.age1)
        self.miniLayout1.addWidget(self.age2)
        self.miniLayout1.addWidget(self.age3)
        self.miniLayout1.addWidget(self.age4)

        self.miniLayout2.addWidget(region)
        self.miniLayout2.addWidget(self.region)

        self.miniLayout3.addWidget(self.proglan1)
        self.miniLayout3.addWidget(self.proglan2)
        self.miniLayout3.addWidget(self.proglan3)
        self.miniLayout3.addWidget(self.proglan4)
        self.miniLayout3.addWidget(self.proglan5)

        self.mainLayout.addWidget(self.firstName)
        self.mainLayout.addWidget(self.lastName)
        self.mainLayout.addWidget(age)
        self.mainLayout.addLayout(self.miniLayout1)
        self.mainLayout.addLayout(self.miniLayout2)
        self.mainLayout.addWidget(proglan)
        self.mainLayout.addLayout(self.miniLayout3)
        self.mainLayout.addWidget(self.btnSend)
        self.setLayout(self.mainLayout)

    def btnClicked(self):
        clicked = None
        if self.age1.isChecked():
            clicked = self.age1
        if self.age2.isChecked():
            clicked = self.age2
        if self.age3.isChecked():
            clicked = self.age3
        if self.age4.isChecked():
            clicked = self.age4

        proglans = []
        proglan = ""
        if self.proglan1.checkState():
            proglans.append(self.proglan1.text())
        if self.proglan2.checkState():
            proglans.append(self.proglan2.text())
        if self.proglan3.checkState():
            proglans.append(self.proglan3.text())
        if self.proglan4.checkState():
            proglans.append(self.proglan4.text())
        if self.proglan5.checkState():
            proglans.append(self.proglan5.text())
        
        for lan in proglans:
            proglan += lan
            proglan += '\n'

        information = QMessageBox()
        information.setIcon(QMessageBox.Icon.Information)
        information.setText("Ma'lumotlaringiz sahifasi")
        information.setStandardButtons(QMessageBox.StandardButton.Ok)
        information.setDetailedText(f"Ismingiz: {"Kiritilmagan" if len(self.firstName.text()) == 0 else self.firstName.text()}\nFamiliyangiz: {"Kiritilmagan" if len(self.lastName.text()) == 0 else self.lastName.text()}\nYoshingiz oralig'i: {"Kiritilmagan" if clicked is None else clicked.text()}\nViloyatingiz: {"Yo'q" if len(self.region.currentText()) == 0 else self.region.currentText()}\nDasturlash tillaringiz: {"Yo'q" if len(proglan) == 0 else '\n' + proglan}")
        information.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec_())