from service import HotelService

def main():
    hs = HotelService()

    hs.load_category("categories.txt")
    hs.load_number("numbers.txt")
    hs.load_citizen("citizens.txt")
    hs.load_placement('placements.txt')

    hs.save_free_number_json("free_number_json.json")
    hs.save_busy_percent_json("busy_percent_json.json")

if __name__ == "__main__":
    main()