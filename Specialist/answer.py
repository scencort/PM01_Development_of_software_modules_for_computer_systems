class Answer:
    def __init__(self, answer_id, question_id, expert_id, date):
        self.answer_id = int(answer_id)
        self.question_id = int(question_id)
        self.expert_id = int(expert_id)
        self.date = date


    def __str__(self):
        return f"Answer(answer_id={self.answer_id}, question_id={self.question_id}, expert_id={self.expert_id}, date={self.date}"


    def __repr__(self):
        return self.__str__()