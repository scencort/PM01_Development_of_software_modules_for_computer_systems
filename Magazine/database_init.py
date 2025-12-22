from database import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS author (
            author_id INTEGER PRIMARY KEY,
            fio TEXT,
            is_blocked INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS article (
            article_id INTEGER PRIMARY KEY,
            author_id INTEGER,
            date TEXT,
            lines INTEGER,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()