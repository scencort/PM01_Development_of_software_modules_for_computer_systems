class Station:
    def __init__(self, id_station, name):
        self.id_station = id_station
        self.name = name
    def __str__(self):
        return f"Station(id_station={self.id_station}, name={self.name})"

    def __repr__(self):
        return self.__str__()