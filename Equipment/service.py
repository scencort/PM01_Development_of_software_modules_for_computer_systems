import json

from equipment import Equipment
from request import Request

class EquipmentService:
    def __init__(self):
        self.equipments = {}
        self.requests = []


    def load_equipment(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                equipment_id, name = line.strip().split(";")

                equipment_id = int(equipment_id)
                equipment = Equipment(equipment_id, name)
                self.equipments[equipment_id] = equipment


    def load_requests(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                request_id, equipment_id, object_id, request_date, is_installed, install_date = line.strip().split(";")

                request_id = int(request_id)
                equipment_id = int(equipment_id)
                object_id = int(object_id)

                request = Request(request_id, equipment_id, object_id, request_date, is_installed, install_date)
                self.requests.append(request)


    def print_equipment(self, object_id):
        resultat = []

        for request in self.requests:
            if request.object_id == object_id:
                equipment = self.equipments[request.equipment_id]

                resultat.append({
                    "equipment_id": equipment.equipment_id,
                    "name": equipment.name
                })

        return resultat


    def save_print_equipment_json(self, filename):
        printed_equipments = self.print_equipment(1002)

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(printed_equipments, file, ensure_ascii=False, indent=4)

    """
    - отпечатать перечень оборудования по выбранному объекту (по заявкам);
    """
    def print_not_installed(self, check_date):
        resultat = []

        for request in self.requests:
            if request.request_date <= check_date:
                if request.is_installed == False:
                    equipment = self.equipments[request.equipment_id]
                    resultat.append({
                        "equipment_id": equipment.equipment_id,
                        "name": equipment.name
                    })

                elif request.is_installed == True and request.install_date > check_date:
                    equipment = self.equipments[request.equipment_id]
                    resultat.append({
                        "equipment_id": equipment.equipment_id,
                        "name": equipment.name
                    })

        return resultat


    def save_print_not_installed(self, filename):
        not_installed = self.print_not_installed("2024-02-15")

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(not_installed, file, ensure_ascii=False, indent=4)
