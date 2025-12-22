class Placement:
    def __init__(self, placement_id, citizen_id, number_id, date_start, length_stay):
        self.placement_id = int(placement_id)
        self.citizen_id = int(citizen_id)
        self.number_id = int(number_id)
        self.date_start = date_start
        self.length_stay = int(length_stay)


    def __str__(self):
        return f"Placement(placement_id={self.placement_id}, citizen_id={self.citizen_id}, number_id={self.number_id}, date_start={self.date_start}, length_stay={self.length_stay})"


    def __repr__(self):
        return self.__str__()