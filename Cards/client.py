class Client:
    def __init__(self, client_id, fio, passport, address):
        self.client_id = int(client_id)
        self.fio = fio
        self.passport = passport
        self.address = address


    def __str__(self):
        return f"Client(client_id={self.client_id}, fio={self.fio}, passport={self.passport}, address={self.address})"


    def __repr__(self):
        return self.__str__()