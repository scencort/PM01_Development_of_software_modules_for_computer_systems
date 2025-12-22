from BusStation.station import Station
from BusStation.bus import Bus
from BusStation.trip import Trip

class Avtovokzal:
    def __init__(self):
        self.stations = {}
        self.buses = {}
        self.trips = []

    def load_stations(self, filename):
        with open(filename, encoding='utf-8') as file:
            for i in file:
                station_id, name = i.strip().split(";")
                station_id = int(station_id)

                self.stations[station_id] = Station(station_id, name)
    
    def load_buses(self, filename):
        with open(filename, encoding='utf-8') as file:
            for i in file:
                bus_id, brand, number, capacity = i.strip().split(";")
                bus_id = int(bus_id)
                capacity = int(capacity)

                self.buses[bus_id] = Bus(bus_id, brand, number, capacity)

    def load_trips(self, filename):
        with open(filename, encoding='utf-8') as file:
            for i in file:
                trip_id, station_id, bus_id, time = i.strip().split(";")

                self.trips.append(Trip(int(trip_id), int(station_id), int(bus_id), time))

    """
    – сколько выполняется рейсов до каждой станции?
    """
    def trips_station(self):
        resultat = {}

        for trip in self.trips:
            station_id = trip.station_id

            if station_id not in resultat:
                resultat[station_id] = 0

            resultat[station_id] += 1

        return resultat