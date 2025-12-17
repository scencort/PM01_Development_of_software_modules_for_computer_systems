from books import Book
from readers import Reader
from issues import Issue
import json

class LibraryService:
    def __init__(self):
        self.books = {}
        self.readers = {}
        self.issues = []


    def load_books(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                book_id, title, author, genre, year = line.strip().split(";")

                book_id = int(book_id)

                book = Book(book_id, title, author, genre, year)
                self.books[book_id] = book


    def load_readers(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                reader_id, last, first, middle, ticket = line.strip().split(";")

                reader_id = int(reader_id)

                reader = Reader(reader_id, last, first, middle, ticket)
                self.readers[reader_id] = reader


    def load_issues(self, filename):
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                reader_id, book_id, date = line.strip().split(";")

                issue = Issue(reader_id, book_id, date)
                self.issues.append(issue)


    def most_popular_author(self):
        counts = {}

        for issue in self.issues:
            author = self.books[issue.book_id].author

            if author not in counts:
                counts[author] = 0

            counts[author] += 1

            best_author = max(counts, key=counts.get)
            best_count = counts[best_author]

            return {
                "most_popular_author": best_author,
                "issues_count": best_count
            }


    def issues_by_date(self):
        counts = {}

        for issue in self.issues:
            date = issue.date

            if date not in counts:
                counts[date] = 0

            counts[date] += 1

        return counts


    def save_popular_author_json(self, filename):
        popular_author = self.most_popular_author()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(popular_author, file, ensure_ascii=False, indent=4)


    def save_issues_date(self, filename):
        issue_date = self.issues_by_date()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(issue_date, file, ensure_ascii=False, indent=4)