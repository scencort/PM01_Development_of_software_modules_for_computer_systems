import json
from vkr import Vkr


class BKPService:
    def __init__(self):
        self.vkrs = []


    def load_vkrs(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                direction, language, environment, year = line.strip().split(";")

                vkr = Vkr(direction, language, environment, year)
                self.vkrs.append(vkr)


    def languages_and_envs(self):
        languages = set()
        environments = set()

        for vkr in self.vkrs:
            if vkr.year == 2025:
                languages.add(vkr.language)
                environments.add(vkr.environment)

        return {
            "year": 2025,
            "languages": list(languages),
            "environments": list(environments)
        }


    def save_languages_and_envs_json(self, filename):
        lang_and_envs = self.languages_and_envs()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(lang_and_envs, file, ensure_ascii=False, indent=4)


    def most_popular_direction(self):
        counts = {}

        for vkr in self.vkrs:
            direction = vkr.direction

            if direction not in counts:
                counts[direction] = 0

            counts[direction] += 1

        best_direction = None
        best_count = 0

        for direction, count in counts.items():
            if count > best_count:
                best_count = count
                best_direction = direction

        return {
            "direction": best_direction,
            "count": best_count
        }


    def save_most_popular_direction_json(self, filename):
        popular_description = self.most_popular_direction()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(popular_description, file, ensure_ascii=False, indent=4)