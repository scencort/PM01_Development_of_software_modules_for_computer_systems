from db.get_connection import get_connection

def create_tables():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bus(
        id_bus INTEGER PRIMARY KEY,
        mark TEXT, 
        number TEXT, 
        cap INTEGER
        )
        """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS station(
        id_station INEGER PRIMARY KEY, 
        name TEXT
        )
    """)

    cur.execute("""
CREATE TABLE IF NOT EXISTS trip (
    id_trip INTEGER PRIMARY KEY,
    station INTEGER,
    bus INTEGER,
    time TEXT,
    FOREIGN KEY (station) REFERENCES station(id_station),
    FOREIGN KEY (bus) REFERENCES bus(id_bus)
)
""")
    con.commit()
    con.close()
