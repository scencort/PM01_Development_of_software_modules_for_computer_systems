"""
Модуль формирования отчётов.
"""

from database import Database


class ReportService:
    """
    Класс для аналитических отчётов по раскрою.
    """

    @staticmethod
    def get_max_kim() -> float:
        """
        Возвращает максимальный коэффициент использования металла.
        """
        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT MAX(kim) FROM layouts")
        result = cursor.fetchone()[0]

        connection.close()
        return result

    @staticmethod
    def get_unprocessed_count() -> int:
        """
        Возвращает количество необработанных чертежей.
        """
        connection = Database.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM drawings WHERE processed = 0"
        )
        result = cursor.fetchone()[0]

        connection.close()
        return result
