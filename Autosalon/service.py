from customers import Customer
from managers import Manager
from cars import Car
from sales import Sale


class AutoSalonService:
    def __init__(self):
        self.customers = {}
        self.managers = {}
        self.cars = {}
        self.sales = []

    def load_customer(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                customer_id, name = line.strip().split(";")
                customer_id = int(customer_id)

                customer = Customer(customer_id, name)
                self.customers[customer_id] = customer

    def load_managers(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                manager_id, name = line.strip().split(";")
                manager_id = int(manager_id)

                manager = Manager(manager_id, name)
                self.managers[manager_id] = manager

    def load_cars(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                car_id, brand = line.strip().split(";")
                car_id = int(car_id)

                car = Car(car_id, brand)
                self.cars[car_id] = car

    def load_sales(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                manager_id, car_id, plate, customer_id, date, price = line.strip().split(";")

                manager_id = int(manager_id)
                car_id = int(car_id)
                customer_id = int(customer_id)
                price = float(price)

                sale = Sale(manager_id, car_id, plate, customer_id, date, price)
                self.sales.append(sale)

    def avg_sale_price(self):
        total = 0

        for sale in self.sales:
            total = total + sale.price

        avg = total / len(self.sales)
        return avg

    def save_avg(self, filename):
        avg = self.avg_sale_price()
        with open(filename, "w", encoding='utf-8') as file:
            file.write(f"Средняя сумма сделки: {avg}")