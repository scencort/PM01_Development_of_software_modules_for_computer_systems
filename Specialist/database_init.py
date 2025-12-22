from database import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE visitor (
        visitor_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE expert (
        expert_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE section (
        section_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE question (
        question_id INTEGER PRIMARY KEY,
        visitor_id INTEGER,
        section_id INTEGER,
        date TEXT,
        is_closed BIT
    )
    """)

    cursor.execute("""
    CREATE TABLE answer (
        answer_id INTEGER PRIMARY KEY,
        question_id INTEGER,
        expert_id INTEGER,
        date TEXT
    )
    """)

    connection.commit()
    connection.close()