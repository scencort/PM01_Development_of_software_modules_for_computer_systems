class Reader:
    def __init__(self, reader_id, last, first, middle, ticket):
        self.reader_id = int(reader_id)
        self.last = last
        self.first = first
        self.middle = middle
        self.ticket = ticket


    def __str__(self):
        return f"Reader(id={self.reader_id}, name='{self.last} {self.first}'"


    def __repr__(self):
        return self.__str__()