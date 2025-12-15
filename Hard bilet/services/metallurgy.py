"""
Модуль обработки чертежей отделом главного металлурга.
"""

from database import Database


class MetallurgyService:
    """
    Класс для формирования раскроя и расчёта КИМ.
    """

    def __init__(self, sheet_mass: float) -> None:
        """
        Инициализация сервиса металлурга.

        :param sheet_mass: масса листа металла
        """
        self.sheet_mass = sheet_mass

    def process_drawings(self) -> None:
        """
        Обрабатывает необработанные чертежи и рассчитывает КИМ.
        """
        connection = Database.get_connection()
        cursor = connection.cursor()


        cursor.execute(
            "SELECT id, mass FROM drawings WHERE processed = 0"
        )
        drawings = cursor.fetchall()

        for drawing_id, mass in drawings:
            kim = mass / self.sheet_mass


            cursor.execute(
                """
                INSERT INTO layouts (drawing_id, sheet_mass, kim)
                VALUES (?, ?, ?)
                """,
                (drawing_id, self.sheet_mass, kim)
            )


            cursor.execute(
                """
                UPDATE drawings
                SET processed = 1
                WHERE id = ?
                """,
                (drawing_id,)
            )

        connection.commit()
        connection.close()
