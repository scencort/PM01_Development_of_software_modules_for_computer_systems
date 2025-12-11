import sys
import pymysql
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QApplication
from db import get_connection


class LoginWindow(QDialog):  # объявление класса окна авторизации, наследуемого от qdialog
    """
    Окно авторизации, где пользователь будет вводить логин и пароль
    Если ничего не введёт - выброс ошибки
    """

    def __init__(self):  # конструктор класса, вызывается при создании окна
        super().__init__()  # инициализация родительского класса qdialog

        self.setWindowTitle("Вход в систему")  # установка заголовка окна
        self.setFixedSize(400, 200)  # задаём фиксированный размер окна

        self.label_login = QLabel("Логин:")  # создаём текстовую надпись для поля логина
        self.label_password = QLabel("Пароль:")  # создаём текстовую надпись для поля пароля

        self.edit_login = QLineEdit()  # создаём текстовое поле для ввода логина
        self.edit_password = QLineEdit()  # создаём текстовое поле для ввода пароля
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_login = QPushButton("Войти")  # создаём кнопку входа
        self.button_login.clicked.connect(self.authenticate_user)  # привязываем функцию проверки логина и пароля к нажатию кнопки

        self.layout = QVBoxLayout()  # создаём вертикальный layout для размещения элементов интерфейса

        self.layout.addWidget(self.label_login)  # добавляем надпись "логин" в layout
        self.layout.addWidget(self.edit_login)  # добавляем поле ввода логина в layout

        self.layout.addWidget(self.label_password)  # добавляем надпись "пароль" в layout
        self.layout.addWidget(self.edit_password)  # добавляем поле ввода пароля в layout

        self.layout.addWidget(self.button_login)  # добавляем кнопку "войти" в layout

        self.setLayout(self.layout)  # применяем созданный layout к окну


    def authenticate_user(self):  # метод, который выполняет проверку логина и пароля при нажатии кнопки
        login = self.edit_login.text()  # получаем текст, введённый пользователем в поле логина
        password = self.edit_password.text()  # получаем текст, введённый пользователем в поле пароля

        if not login or not password:  # проверяем, пустые ли поля логина или пароля
            QMessageBox.warning(self, "Ошибка", "Введите логин или пароль")  # показываем предупреждение об ошибке
        try:  # начинаем блок, где может произойти ошибка работы с базой
            connection = get_connection()  # создаём подключение к базе данных через вашу функцию

            with connection.cursor() as cursor:  # создаём cursor для выполнения sql-запросов
                cursor.execute(
                    "SELECT * FROM users WHERE login = %s AND password = %s",  # sql-запрос на поиск пользователя с указанными логином и паролем
                    (login, password)  # передаём параметры безопасно в виде кортежа
                )

                zapros = cursor.fetchone()  # получаем одну строку результата (или none, если пользователь не найден)
                print(zapros)  # выводим результат поиска в консоль для отладки

        except pymysql.MySQLError as error:  # ловим ошибки подключения к базе данных или выполнения запроса
            QMessageBox.critical(self, "Ошибка в базе данных", "Запрос в базу не выполнен или запрос не корректен")  # показываем сообщение об ошибке базы

        if zapros:  # проверяем, найден ли пользователь
            QMessageBox.information(self, "Успех", "Вход выполнен")  # показываем сообщение об успешной авторизации
        else:  # если пользователь не найден (zapros == none)
            QMessageBox.warning(self, "Данные не верные", "Попробуйте повторить вход, введя ещё раз логин и пароль")  # показываем ошибку неверных данных


app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec())
