class Author:
    def __init__(self, author_id, fio, is_blocked):
        self.author_id = int(author_id)
        self.fio = fio
        self.is_blocked = int(is_blocked)

    def __str__(self):
        return f"Author({self.author_id}, {self.fio}, blocked={self.is_blocked})"

    def __repr__(self):
        return self.__str__()