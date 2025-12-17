class Car:
    def __init__(self, car_id, brand):
        self.car_id = int(car_id)
        self.brand = brand

    def __str__(self):
        return f"Car(id={self.car_id}, brand='{self.brand}')"

    def __repr__(self):
        return self.__str__()