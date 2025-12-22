class Card:
    def __init__(self, card_id, name, number, client_id, is_active):
        self.card_id = int(card_id)
        self.name = name
        self.number = int(number)
        self.client_id = int(client_id)
        self.is_active = int(is_active)


    def __str__(self):
        return f"Card(card_id={self.card_id}, name={self.name}, number={self.number}, client_id={self.client_id}, active?{self.is_active}"


    def __repr__(self):
        return self.__str__()