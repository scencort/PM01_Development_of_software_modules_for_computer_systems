from service import LibraryService

def main():
    library = LibraryService()

    library.load_books("books.txt")
    library.load_readers("readers.txt")
    library.load_issues("issues.txt")

    library.save_popular_author_json("most_popular_author.json")
    library.save_issues_date("issues_date.json")

if __name__ == "__main__":
    main()