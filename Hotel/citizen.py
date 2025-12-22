class Citizen:
    def __init__(self, citizen_id, fio, passport):
        self.citizen_id = int(citizen_id)
        self.fio = fio
        self.passport = int(passport)


    def __str__(self):
        return f"Citizen(citizen_id={self.citizen_id}, fio={self.fio}, passport={self.passport})"


    def __repr__(self):
        return self.__str__()