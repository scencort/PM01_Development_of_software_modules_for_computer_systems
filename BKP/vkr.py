class Vkr:
    def __init__(self, direction, language, environment, year):
        self.direction = direction
        self.language = language
        self.environment = environment
        self.year = int(year)


    def __str__(self):
        return f"Vkr(direction={self.direction}, language={self.language}, environment={self.environment}, year={self.year}"


    def __repr__(self):
        return self.__str__()