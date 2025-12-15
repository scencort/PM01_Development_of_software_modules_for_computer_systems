"""
Точка входа в программу.
"""

from database import Database
from services.importer import DrawingImporter
from services.metallurgy import MetallurgyService
from services.reports import ReportService


def main() -> None:
    """
    Основной сценарий работы программы.
    """

    Database.initialize()

    importer = DrawingImporter("C:/Users/yaros/Desktop/PM01_Development_of_software_modules_for_computer_systems/Hard bilet/data/drawings.csv")
    importer.import_to_db()

    metallurgy = MetallurgyService(sheet_mass=50.0)
    metallurgy.process_drawings()

    print("Максимальный КИМ:", ReportService.get_max_kim())
    print(
        "Количество необработанных чертежей:",
        ReportService.get_unprocessed_count()
    )


if __name__ == "__main__":
    main()