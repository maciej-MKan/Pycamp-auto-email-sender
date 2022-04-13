
import sqlite3
from os import path
from datetime import datetime

class DataBase:
    def __init__(self, db_name):
        self.db = db_name

    def db_manager(self):
        with sqlite3.connect(self.db) as connection:
            self.cursor = connection.cursor()


    def check_if_exists(self):
        if self.db == ':memory:' or not path.isfile(self.db):
            self.create_db()
        return True

    def create_db(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, book_name TEXT, date DATE)""")

    def get_content(self, column = 'id', data = not None):
        output_content = []

        self.cursor.execute(f"SELECT id, name, book_name, date FROM book WHERE {column} IS ?", (data,))

        for id, name, book_name, date in self.cursor.fetchall():
            output_content.append({'id': id, 'name' : name, 'book_name' : book_name, 'date' : date}) 
        return output_content

    def put_content(self, name, book_name, date = datetime.now()):
        self.cursor.execute("INSERT INTO book(name, book_name, date) VALUES (?,?,?)", (name, book_name, date))

    def delete_content(self, column = 'id', data = not None):
        self.cursor.execute(f"DELETE FROM book WHERE {column} IS ?", (data,))