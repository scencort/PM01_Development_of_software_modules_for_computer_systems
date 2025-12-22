class Section:
    def __init__(self, section_id, name):
        self.section_id = int(section_id)
        self.name = name


    def __str__(self):
        return f"Section(section_id={self.section_id}, name={self.name})"


    def __repr__(self):
        return self.__str__()