"""
Модуль работы с базой данных SQLite.

Отвечает за подключение и создание таблиц.
"""

import sqlite3


class Database:
    """
    Класс для управления базой данных SQLite.
    """

    DB_NAME = "metal_cutting.db"

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        """
        Создаёт и возвращает соединение с базой данных.
        """
        return sqlite3.connect(cls.DB_NAME)

    @classmethod
    def initialize(cls) -> None:
        """
        Создаёт таблицы базы данных, если они ещё не существуют.
        """
        connection = cls.get_connection()
        cursor = connection.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS drawings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                mass REAL NOT NULL,
                processed INTEGER DEFAULT 0
            )
            """
        )


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS layouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                drawing_id INTEGER NOT NULL,
                sheet_mass REAL NOT NULL,
                kim REAL NOT NULL,
                FOREIGN KEY (drawing_id) REFERENCES drawings(id)
            )
            """
        )

        connection.commit()
        connection.close()
