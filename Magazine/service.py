import json

from database import get_connection
from author import Author
from article import Article


class EditorialService:
    def load_author(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                author_id, fio, is_blocked = line.strip().split(";")

                cursor.execute(
                    "INSERT INTO author VALUES (?, ?, ?)",
                    (int(author_id), fio, int(is_blocked))
                )

        connection.commit()
        connection.close()


    def load_author_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT author_id, fio, is_blocked FROM author"
        )

        rows = cursor.fetchall()
        connection.close()

        authors = []
        for a in rows:
            authors.append(
                Author(a[0], a[1], a[2])
            )

        return authors


    def load_article(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                article_id, author_id, date, lines, status = line.strip().split(";")

                cursor.execute(
                    "INSERT INTO article VALUES (?, ?, ?, ?, ?)",
                    (int(article_id), int(author_id), date, int(lines), status)
                )

        connection.commit()
        connection.close()


    def load_article_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT article_id, author_id, date, lines, status FROM article"
        )

        rows = cursor.fetchall()
        connection.close()

        articles = []
        for a in rows:
            articles.append(
                Article(a[0], a[1], a[2], a[3], a[4])
            )

        return articles


    def articles_on_review(self, check_date):
        """
        - отпечатать список статей на рассмотрении
          на указанную дату
        """
        articles = self.load_article_from_db()

        resultat = []

        for article in articles:
            if article.date <= check_date:
                if article.status != "rejected":
                    resultat.append({
                        "article_id": article.article_id,
                        "author_id": article.author_id,
                        "date": article.date,
                        "status": article.status
                    })

        return resultat


    def save_articles_on_review_json(self, filename):
        articles_on_review = self.articles_on_review('2024-05-15')

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(articles_on_review, file, ensure_ascii=False, indent=4)



    def payments_by_authors(self, start_date, end_date):
        """
        - отпечатать таблицу выплат авторам за период

        Формула:
        1000 рублей за статью
        + 10 рублей за строчку
        """
        articles = self.load_article_from_db()
        authors = self.load_author_from_db()

        payments = {}


        for article in articles:
            if start_date <= article.date <= end_date:
                if article.status != "rejected" and article.status != "new":
                    payment = 1000 + article.lines * 10

                    for author in authors:
                        fio_author = author.fio
                        if author.author_id == article.author_id:

                            if author.author_id not in payments:
                                payments[fio_author] = 0

                            payments[fio_author] += payment
                            break

        return payments


    def save_payments_by_authors_json(self, filename):
        payments_by_authors = self.payments_by_authors('2024-01-01', '2024-12-31')

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(payments_by_authors, file, ensure_ascii=False, indent=4)