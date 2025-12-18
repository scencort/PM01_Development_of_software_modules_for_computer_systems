import json

from brigades import Brigade
from workers import Worker
from parts import Part
from production import Product

class FactoryService:
    def __init__(self):
        self.brigades = {}
        self.workers = {}
        self.parts = {}
        self.productions = []


    def load_brigades(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                brigade_id, name = line.strip().split(";")

                brigade_id = int(brigade_id)

                brigade = Brigade(brigade_id, name)
                self.brigades[brigade_id] = brigade


    def load_workers(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                worker_id, name, brigade_id = line.strip().split(";")

                worker_id = int(worker_id)
                brigade_id = int(brigade_id)

                worker = Worker(worker_id, name, brigade_id)
                self.workers[worker_id] = worker


    def load_parts(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                part_id, name, price = line.strip().split(";")

                part_id = int(part_id)
                price = float(price)

                part = Part(part_id, name, price)
                self.parts[part_id] = part


    def load_productions(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                date, worker_id, brigade_id, part_id, is_defect = line.strip().split(";")

                worker_id = int(worker_id)
                brigade_id = int(brigade_id)
                part_id = int(part_id)

                product = Product(date, worker_id, brigade_id, part_id, is_defect)
                self.productions.append(product)


    def no_defect_brigades(self, from_date, to_date):
        bad_brigades = {}

        for product in self.productions:
            if from_date <= product.date <= to_date:
                if product.is_defect == True:
                    bad_brigades[product.brigade_id] = True

        resultat = []
        for brigade_id, brigade in self.brigades.items():
            if brigade_id not in bad_brigades:
                resultat.append({
                    "brigade_id": brigade.brigade_id,
                    "name": brigade.name
                })

        return resultat


    def save_no_defect_brigades_json(self, filename):
        no_defect_brigades = self.no_defect_brigades(from_date="2024-05-01", to_date="2024-05-03")

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(no_defect_brigades, file, ensure_ascii=False, indent=4)