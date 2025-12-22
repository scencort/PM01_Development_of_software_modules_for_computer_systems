class Question:
    def __init__(self, question_id, visitor_id, section_id, date, is_closed):
        self.question_id = int(question_id)
        self.visitor_id = int(visitor_id)
        self.section_id = int(section_id)
        self.date = date
        self.is_closed = bool(is_closed)


    def __str__(self):
        return f"Question(question_id={self.question_id}, visitor_id={self.visitor_id}, section_id={self.section_id}, date={self.date}, closed?={self.is_closed})"


    def __repr__(self):
        return self.__str__()