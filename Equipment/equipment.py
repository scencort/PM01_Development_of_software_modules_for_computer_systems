class Equipment:
    def __init__(self, equipment_id, name):
        self.equipment_id = int(equipment_id)
        self.name = name


    def __str__(self):
        return f"Equipment(equipment_id={self.equipment_id}, name={self.name}"


    def __repr__(self):
        return self.__str__()