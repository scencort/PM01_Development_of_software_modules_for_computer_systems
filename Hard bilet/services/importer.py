"""
Модуль импорта чертежей из CSV-файла.
"""

import csv
from database import Database


class DrawingImporter:
    """
    Класс для загрузки чертежей в базу данных.
    """

    def __init__(self, csv_path: str) -> None:
        """
        Инициализация импортёра.

        :param csv_path: путь к CSV-файлу с чертежами
        """
        self.csv_path = csv_path

    def import_to_db(self) -> None:
        """
        Импортирует данные из CSV в таблицу drawings.
        """
        connection = Database.get_connection()
        cursor = connection.cursor()

        with open(self.csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute(
                    """
                    INSERT INTO drawings (name, mass)
                    VALUES (?, ?)
                    """,
                    (row["name"], float(row["mass"]))
                )

        connection.commit()
        connection.close()
