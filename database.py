
import sqlite3

DB_NAME = "transit.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS routes (
            name TEXT PRIMARY KEY,
            trips INTEGER NOT NULL,
            on_time INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_route(name, trips, on_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO routes (name, trips, on_time)
        VALUES (?, ?, ?)
    """, (name, trips, on_time))
    conn.commit()
    conn.close()


def get_all_routes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, trips, on_time FROM routes")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"name": row[0], "trips": row[1], "on_time": row[2]}
        for row in rows
    ]

def delete_route(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM routes WHERE name = ?", (name,))
    conn.commit()
    conn.close()


