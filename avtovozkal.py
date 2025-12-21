"""
Задание для разработки.  Автовокзал. 
В базе данных хранятся сведения об автобусах и рейсах до станций по расписанию. Каждый автобус вмещает не более определённого количества пассажиров
Таблицы: станции (код станции, название станции), автобусы (код автобуса, марка автобуса, государственный номер, вместимость), рейсы (код рейса, код станции, код автобуса, время отправления).

Определить:
- сколько выполняется рейсов до каждой станции;
- каково общее количество пассажиров.
"""
import json
from station import Station
from bus import Bus
from trip import Trip
class Avtovokzal:
    def __init__(self):
        self.stations = {}
        self.buses = {}
        self.trips = []
    
    def load_stations(self):
        with open('station.txt', encoding='utf-8') as f:
            for line in f:
                id_s, name = line.strip().split(";")
                self.stations[int(id_s)] = Station(int(id_s), name)

    def load_bus(self):
        with open('bus.txt', encoding="utf-8") as f:
            for line in f:
                id_b, mark, number, cap = line.strip().split(";")
                self.buses[int(id_b)] = Bus(int(id_b), mark, number, int(cap))

    def load_trip(self):
        with open('trip.txt', encoding="utf-8") as f:
            for line in f:
                id_t, id_s, id_b, time = line.strip().split(";")
                station = self.stations[int(id_s)]
                bus = self.buses[int(id_b)]
                self.trips.append(Trip(int(id_t), station, bus, time))
    def number_of_trip(self):
        results = {}
        for trip in self.trips:
            name = trip.station.name
            results[name] = results.get(name, 0) + 1
        return results

    def save_json_number_of_trip(self):
        data = self.number_of_trip()
        with open("number_of_trip.json", "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    def number_of_pass(self):
        count = 0
        for trip in self.trips:
            count += trip.bus.cap
        return count
    
    def save_json_number_of_pass(self):
        c = self.number_of_pass()
        result = {"Общее количество": c}
        with open("number_of_pass.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)