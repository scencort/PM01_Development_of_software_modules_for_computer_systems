from service import EditorialService
from database_init import create_tables

def main():
    es = EditorialService()

    create_tables()

    es.load_author("author.txt")
    es.load_article("article.txt")

    es.save_articles_on_review_json("articles_on_review_json.json")
    es.save_payments_by_authors_json("payments_by_authors_json.json")

if __name__ == "__main__":
    main()