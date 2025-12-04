import sys

from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QMessageBox

import db

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Логин")
        self.setFixedSize(500, 200)

        self.login_label = QLabel("Логин:")
        self.login_input = QLineEdit()

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()

        self.enter_button = QPushButton("Войти")
        self.enter_button.clicked.connect(self.check_login)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.login_label)
        self.layout.addWidget(self.login_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.enter_button)

        self.setLayout(self.layout)

    def check_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        try:
            connection = db.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE login=%s AND password=%s", (login, password)
                )
                zapros = cursor.fetchone()

            connection.close()

            if zapros:
                QMessageBox.information(self, "успех", "слава Z")
            else:
                QMessageBox.warning(self, "ошибка", "не верный пароль")

        except Exception as error:
            QMessageBox.critical(self, "ошибка", "ошибка бд")

app = QApplication(sys.argv)
window = Login()
window.show()
sys.exit(app.exec())