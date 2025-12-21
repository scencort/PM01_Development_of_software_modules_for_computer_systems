from avtovozkal import Avtovokzal

def main():
    a = Avtovokzal()

    a.load_bus()
    a.load_stations()
    a.load_trip()
    a.save_json_number_of_trip()
    a.save_json_number_of_pass()


if __name__ == "__main__":
    main()

