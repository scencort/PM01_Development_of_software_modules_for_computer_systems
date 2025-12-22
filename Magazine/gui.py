import sys
from service import EditorialService
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QMessageBox

class MagazineWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.editor_service = EditorialService()

        self.setWindowTitle("Газеты")
        self.setFixedSize(400, 400)

        self.layout = QVBoxLayout()

        self.button_save_articles_on_review = QPushButton("Вывести 1")
        self.button_save_articles_on_review.clicked.connect(self.save_articles_on_review_json_gui)
        self.layout.addWidget(self.button_save_articles_on_review)

        self.button_save_payments_by_authors = QPushButton("Вывести 2")
        self.button_save_payments_by_authors.clicked.connect(self.save_payments_by_authors_json_gui)
        self.layout.addWidget(self.button_save_payments_by_authors)

        self.setLayout(self.layout)

    def save_articles_on_review_json_gui(self):
        self.editor_service.save_articles_on_review_json("articles_on_review_json.json")

        QMessageBox.information(self, "Отлично", "Файл создан")

    def save_payments_by_authors_json_gui(self):
        self.editor_service.save_payments_by_authors_json("payments_by_authors_json.json")

        QMessageBox.information(self, "Отлично", "Файл создан")


app = QApplication(sys.argv)
window = MagazineWindow()
window.show()
sys.exit(app.exec())