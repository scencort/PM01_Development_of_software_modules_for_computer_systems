class Sale:
    def __init__(self, manager_id, car_id, plate, customer_id, date, price):
        self.manager_id = int(manager_id)
        self.car_id = int(car_id)
        self.plate = plate
        self.customer_id = int(customer_id)
        self.date = date
        self.price = float(price)

    def __str__(self):
        return (
            f"Sale(manager_id={self.manager_id}, car_id={self.car_id}, "
            f"plate='{self.plate}', customer_id={self.customer_id}, "
            f"date='{self.date}', price={self.price})"
        )

    def __repr__(self):
        return self.__str__()