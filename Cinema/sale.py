class Sale:
    def __init__(self, sale_id: int, film_id: int, hall_id: int, time: str, seat: int):
        self.sale_id = sale_id
        self.film_id = film_id
        self.hall_id = hall_id
        self.time = time
        self.seat = seat

    def __str__(self):
        return f"{self.sale_id};{self.film_id};{self.hall_id};{self.time};{self.seat}"