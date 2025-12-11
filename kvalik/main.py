import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt6.QtCore import Qt
from login_window import LoginWindow

class MainWindow(QMainWindow):
    """
    Главное окно программы
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Система управления гостиницей")

        self.label = QLabel("Добро пожаловать!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginWindow()
    if login.exec() == LoginWindow.DialogCode.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())