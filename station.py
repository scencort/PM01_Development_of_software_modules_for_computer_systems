class Station:
    def __init__(self, id_station, name):
        self.id_station = id_station
        self.name = name
    def __str__(self):
        return f"{self.id_station}: {self.name}"