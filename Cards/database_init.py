from database import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE client (
        client_id INTEGER PRIMARY KEY,
        fio TEXT,
        passport INTEGER,
        address TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE card (
        card_id INTEGER PRIMARY KEY,
        name TEXT,
        number INTEGER,
        client_id INTEGER,
        is_active INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE operation (
        operation_id INTEGER PRIMARY KEY,
        card_id INTEGER,
        date TEXT,
        type_operation TEXT
    )
    """)

    connection.commit()
    connection.close()