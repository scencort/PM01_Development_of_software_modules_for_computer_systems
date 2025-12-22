class Expert:
    def __init__(self, expert_id, name):
        self.expert_id = int(expert_id)
        self.name = name


    def __str__(self):
        return f"Expert(expert_id={self.expert_id}, name={self.name})"


    def __repr__(self):
        return self.__str__()