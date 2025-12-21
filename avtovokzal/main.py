from avtovozkal import Avtovokzal
from db.database import create_tables
def main():
    a = Avtovokzal()
    create_tables()
    a.load_bus()
    a.load_stations()
    a.load_trip()
    a.save_json_number_of_trip()
    a.save_json_number_of_pass()


if __name__ == "__main__":
    main()

