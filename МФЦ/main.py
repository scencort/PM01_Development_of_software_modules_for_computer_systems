from service import Mfc
from database_init import create_tables

def main():
    mfc = Mfc()

    create_tables()

    mfc.load_document_type("type_document.txt")
    mfc.load_applicant("applicant.txt")
    mfc.load_application("application.txt")

    mfc.save_document_type_json(filename="document_count.json", start_date='2025-01-01', end_date='2025-12-31')

if __name__ == "__main__":
    main()