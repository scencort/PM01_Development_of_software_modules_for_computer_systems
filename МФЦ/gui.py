import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from service import Mfc

class MfcWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.service = Mfc()

        self.setWindowTitle("MFC")
        self.setFixedSize(350, 350)

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Период"))
        self.start_date = QLineEdit()
        self.layout.addWidget(self.start_date)

        self.end_date = QLineEdit()
        self.layout.addWidget(self.end_date)

        self.button_report = QPushButton("Отчёт по типам документов")
        self.button_report.clicked.connect(self.make_report)
        self.layout.addWidget(self.button_report)

        self.layout.addWidget(QLabel("ID заявителя"))
        self.applicant_id = QLineEdit()
        self.layout.addWidget(self.applicant_id)

        self.button_card = QPushButton("Отчёт по выдачи социальной карты")
        self.button_card.clicked.connect(self.get_card_date)
        self.layout.addWidget(self.button_card)

        self.setLayout(self.layout)


    def make_report(self):
        start_date = self.start_date.text()
        end_date = self.end_date.text()

        if not start_date or not end_date:
            QMessageBox.warning(self, "Ошибка", "Надо ввести преиод дат")
            return

        self.service.save_document_type_json(
            "document_count.json",
            start_date,
            end_date
        )

        QMessageBox.information(self, "Супер", "Результат сохранён")


    def get_card_date(self):
        applicant = self.applicant_id.text()

        if not applicant:
            QMessageBox.warning(self, "Ошибка", "Введи корректный ID")
            return

        self.service.save_get_social_card_json(
            applicant,
            "card_ready_date.json"
        )

        QMessageBox.information(self, "Супер", "Результат сохранён")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MfcWindow()
    window.show()
    sys.exit(app.exec())