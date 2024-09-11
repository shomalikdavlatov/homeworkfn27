from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton
from internRegisterPage import Register
from internLoginPage import Login


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(340, 200, 680, 400)
        self.setWindowTitle("Main")
        self.users = []

        central = QWidget()
        self.setCentralWidget(central)
        mainLayout = QVBoxLayout()

        self.btnRegister = QPushButton("Sign up")
        self.btnLogin = QPushButton("Sign in")

        self.btnRegister.clicked.connect(lambda: self.btnRegisterClicked())
        self.btnLogin.clicked.connect(lambda: self.btnLoginClicked())

        mainLayout.addWidget(self.btnRegister)
        mainLayout.addWidget(self.btnLogin)
        central.setLayout(mainLayout)

        self.show()

    def btnRegisterClicked(self):
        self.rg = Register(self)
        self.hide()

    def btnLoginClicked(self):
        self.lg = Login(self)
        self.hide()


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()