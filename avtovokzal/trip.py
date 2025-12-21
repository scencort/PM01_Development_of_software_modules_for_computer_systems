class Trip:
    def __init__(self, id_trip, station, bus, time):
        self.id_trip = id_trip
        self.station = station
        self.bus = bus 
        self.time = time
    
    def __str__(self):
        return f"Trip(id_strip={self.id_trip}, id_station={self.station}, id_bus={self.bus}, time={self.time})"

    def __repr__(self):
        return self.__str__()