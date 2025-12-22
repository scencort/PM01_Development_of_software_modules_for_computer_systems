import json

from category import Category
from number import Number
from citizen import Citizen
from placement import Placement

class HotelService:
    def __init__(self):
        self.categories = {}
        self.numbers = {}
        self.citizens = {}
        self.placements = []


    def load_category(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                category_id, name = line.strip().split(";")

                category_id = int(category_id)

                category = Category(category_id, name)
                self.categories[category_id] = category


    def load_number(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                number_id, category_id, number, place = line.strip().split(";")

                number_id = int(number_id)
                category_id = int(category_id)
                number = int(number)
                place = int(place)

                number_c = Number(number_id, category_id, number, place)
                self.numbers[number_id] = number_c


    def load_citizen(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                citizen_id, fio, passport = line.strip().split(";")

                citizen_id = int(citizen_id)
                passport = int(passport)

                citizen = Citizen(citizen_id, fio, passport)
                self.citizens[citizen_id] = citizen


    def load_placement(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                placement_id, citizen_id, number_id, date_start, length_stay = line.strip().split(";")

                placement_id = int(placement_id)
                citizen_id = int(citizen_id)
                number_id = int(number_id)
                length_stay = int(length_stay)

                placement = Placement(placement_id, citizen_id, number_id, date_start, length_stay)
                self.placements.append(placement)


    def free_number(self):
        not_free_numbers = set()

        for placement in self.placements:
            not_free_numbers.add(placement.number_id)

        print(not_free_numbers)

        count = 0
        for number_id in self.numbers:
            if number_id not in not_free_numbers:
                count += 1

        return {
            "counts_free_number": count
        }


    def save_free_number_json(self, filename):
        free_number = self.free_number()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(free_number, file, ensure_ascii=False, indent=4)


    def busy_percent(self):
        resultat = []

        for category_id, category in self.categories.items():
            total = 0
            busy = 0

            for number in self.numbers.values():
                if number.category_id == category_id:
                    total += 1

                    for placement in self.placements:
                        if placement.number_id == number.number_id:
                            busy += 1
                            break

            percent = 0
            if total > 0:
                percent = busy / total * 100

            resultat.append({
                "category": category.name,
                "percent": round(percent, 2)
            })

        return resultat


    def save_busy_percent_json(self, filename):
        busy_percent = self.busy_percent()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(busy_percent, file, ensure_ascii=False, indent=4)