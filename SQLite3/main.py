import sqlite3

DB_NAME = "sqlite_db.db"

# # Create new table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        students_qty integer,
        reviews_qty integer
    );"""
    sqlite_conn.execute(sql_request)

# # Add records to the courses table
courses = [
    (355, "JavaScrypt course", 22, 255),
    (100, "DataScience course", 500, 30),
    (500, "Java course", 500, 23)
]

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()

# # Read data
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses"
    sql_cursor = sqlite_conn.execute(sql_request)
    # # Иттерация с помощью цикла
    for record in sql_cursor:
        print(record)
    # # Иттерация с помощью метода fetchall
    records = sql_cursor.fetchall()
    print(records)
