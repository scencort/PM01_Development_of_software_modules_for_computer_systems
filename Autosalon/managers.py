class Manager:
    def __init__(self, manager_id, name):
        self.manager_id = int(manager_id)
        self.name = name

    def __str__(self):
        return f"Manager(id={self.manager_id}, name='{self.name}')"

    def __repr__(self):
        return self.__str__()