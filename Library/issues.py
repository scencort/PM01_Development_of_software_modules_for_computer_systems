class Issue:
    def __init__(self, reader_id, book_id, date):
        self.reader_id = int(reader_id)
        self.book_id = int(book_id)
        self.date = date


    def __str__(self):
        return f"Issue(reader_id={self.reader_id}, book_id={self.book_id}, date='{self.date}')"


    def __repr__(self):
        return self.__str__()