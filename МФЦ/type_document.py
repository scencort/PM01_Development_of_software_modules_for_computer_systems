class DocumentType:
    def __init__(self, type_id, name):
        self.type_id = int(type_id)
        self.name = name


    def __str__(self):
        return f"DocumentType(type_id={self.type_id}, name{self.name})"


    def __repr__(self):
        return self.__str__()