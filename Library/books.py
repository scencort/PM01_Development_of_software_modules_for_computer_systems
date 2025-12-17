class Book:
    def __init__(self, book_id, title, author, genre, year):
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.genre = genre
        self.year = int(year)


    def __str__(self):
        return f"Book(id={self.book_id}, title='{self.title}, author='{self.author}'"


    def __repr__(self):
        return self.__str__()