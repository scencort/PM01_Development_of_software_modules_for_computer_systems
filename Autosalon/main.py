from service import AutoSalonService

def main():
    salon = AutoSalonService()

    salon.load_customer("customers.txt")
    salon.load_managers("managers.txt")
    salon.load_cars("cars.txt")
    salon.load_sales("sales.txt")

    salon.save_avg("avg_price.txt")

if __name__ == "__main__":
    main()