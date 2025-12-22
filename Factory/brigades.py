class Brigade:
    def __init__(self, brigade_id, name):
        self.brigade_id = int(brigade_id)
        self.name = name


    def __str__(self):
        return f"Brigade(brigade_id={self.brigade_id}, name={self.name}"


    def __repr__(self):
        return self.__str__()