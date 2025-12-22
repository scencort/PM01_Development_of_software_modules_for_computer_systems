class Number:
    def __init__(self, number_id, category_id, number, place):
        self.number_id = int(number_id)
        self.category_id = int(category_id)
        self.number = int(number)
        self.place = int(place)


    def __str__(self):
        return f"Number(number_id={self.number_id}, category_id={self.category_id}, number={self.number}, place={self.place})"


    def __repr__(self):
        return self.__str__()