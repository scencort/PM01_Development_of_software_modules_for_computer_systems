from database import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS type_document (
        type_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applicant (
        applicant_id INTEGER PRIMARY KEY,
        fio TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS application (
        application_id INTEGER PRIMARY KEY,
        applicant_id INTEGER,
        type_document_id INTEGER,
        date TEXT
    )
    """)

    connection.commit()
    connection.close()