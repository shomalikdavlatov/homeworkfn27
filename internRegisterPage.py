from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,QFormLayout
import pickle


class Register(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(340, 200, 680, 400)
        self.setWindowTitle("Register")

        central = QWidget()
        self.setCentralWidget(central)
        mainLayout = QVBoxLayout()

        self.btnBack = QPushButton("Back")
        self.btnBack.clicked.connect(lambda: self.btnBackClicked())

        headerLayout = QHBoxLayout()
        headerLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        headerLayout.addWidget(self.btnBack)

        username = QLabel("Username:")
        self.username = QLineEdit()
        miniLayout1 = QFormLayout()
        miniLayout1.addRow(username, self.username)

        fullname = QLabel("Full name:")
        self.fullname = QLineEdit()
        miniLayout2 = QFormLayout()
        miniLayout2.addRow(fullname, self.fullname)

        phone = QLabel("Phone:")
        self.phone = QLineEdit()
        miniLayout3 = QFormLayout()
        miniLayout3.addRow(phone, self.phone)

        password = QLabel("Password:")
        self.password = QLineEdit()
        miniLayout4 = QFormLayout()
        miniLayout4.addRow(password, self.password)

        self.btnSignUp = QPushButton("Sign Up")
        self.btnSignUp.clicked.connect(lambda: self.btnSigUpClicked())
        
        mainLayout.addLayout(headerLayout)
        mainLayout.addLayout(miniLayout1)
        mainLayout.addLayout(miniLayout2)
        mainLayout.addLayout(miniLayout3)
        mainLayout.addLayout(miniLayout4)
        mainLayout.addWidget(self.btnSignUp)

        central.setLayout(mainLayout)

        self.show()

    def btnBackClicked(self):
        self.close()
        self.parent().show()

    def btnSigUpClicked(self):
        username = self.username.text()
        fullname = self.fullname.text()
        phone = self.phone.text()
        password = self.password.text()
        data = None
        try:
            with open('users.bin', 'rb') as file:
                data = pickle.load(file)
        except:
            data = []
        
        with open('users.bin', 'wb') as file:
            data.append((username, fullname, phone, password))
            pickle.dump(data, file)
