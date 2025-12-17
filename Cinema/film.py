class Film:
    def __init__(self, film_id: int, title: str, genre: str):
        self.film_id = film_id
        self.title = title
        self.genre = genre

    def __str__(self):
        return f"{self.film_id};{self.title};{self.genre}"