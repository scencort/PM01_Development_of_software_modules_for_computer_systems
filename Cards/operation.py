class Operation:
    def __init__(self, operation_id, card_id, date, type_operation):
        self.operation_id = int(operation_id)
        self.card_id = int(card_id)
        self.date = date
        self.type_operation = type_operation


    def __str__(self):
        return f"Operation(operation_id={self.operation_id}, card_id={self.card_id}, date={self.date}, type_operation={self.type_operation}"


    def __repr__(self):
        return self.__str__()