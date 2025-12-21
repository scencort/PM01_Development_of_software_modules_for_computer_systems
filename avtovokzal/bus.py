class Bus:
    def __init__(self, id_bus, mark, number, cap):
        self.id_bus = id_bus
        self.mark = mark
        self.number = number
        self.cap = cap
    
    def __str__(self):
        return f"Bus(id_bus={self.id_bus}, mark={self.mark}, number={self.number}, cap={self.cap})"

    def __repr__(self):
        return self.__str__()