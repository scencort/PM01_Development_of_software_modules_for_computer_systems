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
        with open(filename, "w", encoding='utf-8') as file:
            printed_equipments = self.print_equipment(1002)

            json.dump(printed_equipments, file, ensure_ascii=False, indent=4)