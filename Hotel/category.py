class Category:
    def __init__(self, category_id, name):
        self.category_id = int(category_id)
        self.name = name


    def __str__(self):
        return f"Category(category_id={self.category_id}, name={self.name})"


    def __repr__(self):
        return self.__str__()