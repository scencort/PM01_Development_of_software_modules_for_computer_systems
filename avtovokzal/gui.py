from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
import sys
from avtovozkal import Avtovokzal
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.vokzal = Avtovokzal()
        self.vokzal.load_bus()
        self.vokzal.load_stations()
        self.vokzal.load_trip()
        self.setWindowTitle("Вывод")
        self.resize(400, 400)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Вывести колво"))
        self.button_number_of_pass = QPushButton("Сохранить результат")
        self.button_number_of_pass.clicked.connect(self.output_pass)
        self.layout.addWidget(self.button_number_of_pass)
        self.layout.addWidget(QLabel("Вывести поездки"))
        self.button_number_of_trip = QPushButton("Сохранить результат")
        self.button_number_of_trip.clicked.connect(self.output_trip)
        self.layout.addWidget(self.button_number_of_trip)
        self.setLayout(self.layout)
    
    def output_pass(self):
        try:
            self.vokzal.save_json_number_of_pass()
            QMessageBox.information(self, "Успешно", "Файл сохранен")
        except:
            QMessageBox.information(self, "Анлак", "Файл не сохранен")

    def output_trip(self):
        try:
            self.vokzal.save_json_number_of_trip()
            QMessageBox.information(self, "Успешно", "Файл сохранен")
        except:
            QMessageBox.information(self, "Анлак", "Файл не сохранен")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())