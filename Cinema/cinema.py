from hall import Hall
from film import Film
from sale import Sale


class Cinema:
    def __init__(self):
        self.halls = {}
        self.films = {}
        self.sales = []

    def load_halls(self, filename):
        with open(filename, "r", encoding="utf-8") as halls_f:
            for line in halls_f:
                hall_id, capacity = line.strip().split(";")
                hall_id = int(hall_id)
                capacity = int(capacity)
                hall = Hall(hall_id, capacity)
                self.halls[hall_id] = hall

    def load_films(self, filename):
        with open(filename, "r", encoding="utf-8") as films_f:
            for line in films_f:
                film_id, title, genre = line.strip().split(";")
                film_id = int(film_id)
                film = Film(film_id, title, genre)
                self.films[film_id] = film

    def load_sales(self, filename):
        with open(filename, "r", encoding="utf-8") as sales_f:
            for line in sales_f:
                sale_id, film_id, hall_id, time, seat = line.strip().split(";")
                sale_id = int(sale_id)
                film_id = int(film_id)
                hall_id = int(hall_id)
                seat = int(seat)

                sale = Sale(sale_id, film_id, hall_id, time, seat)
                self.sales.append(sale)

    def hall_occupancy(self):
        sessions = {}

        for sale in self.sales:
            key = (sale.hall_id, sale.time)
            if key not in sessions:
                sessions[key] = 0
            sessions[key] += 1

        result = {}
        for (hall_id, time), sold_seats in sessions.items():
            capacity = self.halls[hall_id].capacity
            percent = sold_seats / capacity * 100
            result[(hall_id, time)] = percent

        return result

    def most_popular_genre(self):
        genre_count = {}

        for sale in self.sales:
            genre = self.films[sale.film_id].genre
            if genre not in genre_count:
                genre_count[genre] = 0
            genre_count[genre] += 1

        return max(genre_count, key=genre_count.get)