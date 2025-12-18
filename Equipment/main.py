from service import EquipmentService

def main():
    es = EquipmentService()

    es.load_equipment("equipment.txt")
    es.load_requests("request.txt")

    es.save_print_equipment_json("printed_equipment_json.json")

if __name__ == "__main__":
    main()