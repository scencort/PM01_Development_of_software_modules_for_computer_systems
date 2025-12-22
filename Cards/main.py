from service import CardsService
from database import get_connection
from database_init import create_tables

def main():
    cs = CardsService()

    create_tables()

    cs.load_client("client.txt")
    cs.load_card("card.txt")
    cs.load_operation("operation.txt")

    cs.save_actual_card_json("actual_card_json.json")
    cs.save_journal_json("journal_json.json")
    # cs.journal()

if __name__ == "__main__":
    main()