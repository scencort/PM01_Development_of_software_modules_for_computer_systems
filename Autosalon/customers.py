class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = int(customer_id)
        self.name = name

    def __str__(self):
        return f"Customer(id={self.customer_id}, name='{self.name}')"

    def __repr__(self):
        return self.__str__()