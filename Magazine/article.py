class Article:
    def __init__(self, article_id, author_id, date, lines, status):
        self.article_id = int(article_id)
        self.author_id = int(author_id)
        self.date = date
        self.lines = int(lines)
        self.status = status

    def __str__(self):
        return f"Article({self.article_id}, author={self.author_id}, status={self.status})"

    def __repr__(self):
        return self.__str__()