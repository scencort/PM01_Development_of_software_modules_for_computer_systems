class Visitor:
    def __init__(self, visitor_id, name):
        self.visitor_id = int(visitor_id)
        self.name = name


    def __str__(self):
        return f"Visitor(visitor_id={self.visitor_id}, name={self.name})"


    def __repr__(self):
        return self.__str__()