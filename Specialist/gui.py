import sys
from service import SpecialistService
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class SpecialistWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.service = SpecialistService()

        self.setWindowTitle("Специалисты онлайн")
        self.setFixedSize(400, 400)

        self.layout = QVBoxLayout()


        self.layout.addWidget(QLabel("Период (YYYY-MM-DD)"))
        self.start_date = QLineEdit()
        self.start_date.setPlaceholderText("Дата с ...")
        self.layout.addWidget(self.start_date)

        self.end_date = QLineEdit()
        self.end_date.setPlaceholderText("Дата по ...")
        self.layout.addWidget(self.end_date)

        self.button_best_expert = QPushButton("Лучший эксперт с ... по ...")
        self.button_best_expert.clicked.connect(self.best_expert)
        self.layout.addWidget(self.button_best_expert)


        self.layout.addWidget(QLabel("Дата проверки (YYYY-MM-DD)"))

        self.check_date = QLineEdit()
        self.layout.addWidget(self.check_date)

        self.button_not_closed = QPushButton("Незакрытые вопросы")
        self.button_not_closed.clicked.connect(self.not_closed_question)
        self.layout.addWidget(self.button_not_closed)

        self.setLayout(self.layout)

    def best_expert(self):
        self.service.save_most_answer_date_json("best_expert.json")

        QMessageBox.information(self, "Отлично", "Результат сохранён")

    def not_closed_question(self):
        self.service.save_not_closed_question_json("not_closed_question.json")

        QMessageBox.information(self, "Отлично", "Результат сохранён")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpecialistWindow()
    window.show()
    sys.exit(app.exec())