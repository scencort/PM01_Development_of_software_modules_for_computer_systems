class Hall:
    def __init__(self, hall_id: int, capacity: int):
        self.hall_id = hall_id
        self.capacity = capacity

    def __str__(self):
        return f"{self.hall_id};{self.capacity}"