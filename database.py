
import sqlite3
from os import path
from datetime import datetime

class DataBase:
    def __init__(self, db_name):
        self.db = db_name
        self.connect = sqlite3.connect(self.db)
        self.db_connect()

    def db_connect(self):
        with self.connect as connection:
            self.cursor = connection.cursor()


    def check_if_exists(self):
        if self.db == ':memory:' or not path.isfile(self.db):
            self.create_db()
        return True

    def create_db(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, mail TEXT NOT NULL, book_name TEXT, date DATE)""")

    def get_content(self, column = 'id', data = None):
        output_content = []

        if data:
            self.cursor.execute(f"SELECT id, name, mail, book_name, date FROM book WHERE {column} IS ?", (data,))
        else:
            self.cursor.execute("SELECT id, name, mail, book_name, date FROM book")

        for id, name, mail, book_name, date in self.cursor.fetchall():
            output_content.append({'id': id, 'name' : name, 'mail' : mail, 'book_name' : book_name, 'date' : date})
        return output_content

    def put_content(self, name, mail, book_name, date = datetime.now()):
        self.cursor.execute("INSERT INTO book(name, mail, book_name, date) VALUES (?, ?, ?, ?)", (name, mail, book_name, date))

    def delete_content(self, column = 'id', data = not None):
        self.cursor.execute(f"DELETE FROM book WHERE {column} IS ?", (data,))

    def __del__(self):
        del self.cursor
        self.connect.commit()
        self.connect.close()