"""
Задание для разработки.  Автовокзал. 
В базе данных хранятся сведения об автобусах и рейсах до станций по расписанию. Каждый автобус вмещает не более определённого количества пассажиров
Таблицы: станции (код станции, название станции), автобусы (код автобуса, марка автобуса, государственный номер, вместимость), рейсы (код рейса, код станции, код автобуса, время отправления).

Определить:
- сколько выполняется рейсов до каждой станции;
- каково общее количество пассажиров.
"""
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
                self.trips.append(Trip(int(id_s), station, bus, time))

