class Part:
    def __init__(self, part_id, name, price):
        self.part_id = int(part_id)
        self.name = name
        self.price = float(price)


    def __str__(self):
        return f"Part(part_id={self.part_id}, name={self.name}, price={self.price}"


    def __repr__(self):
        return self.__str__()