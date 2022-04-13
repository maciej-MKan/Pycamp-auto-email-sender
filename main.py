
import sqlite3
import smtplib
from os import path
from datetime import datetime
import tasks

class AutoEmail:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(sel, exc_type, exc_val, exc_tb):
        pass

class DataBase:
    def __init__(self, db_name):
        self.db = db_name

    def db_manager(self, task):
        with sqlite3.connect(self.db, check_same_thread=False) as connection:
            cursor = connection.cursor()
            if isinstance(task, tuple):
                cursor.execute(task[0],task[1])
            else:
                cursor.execute(task)
            return cursor

    def check_if_exists(self):
        if self.db == ':memory:' or not path.isfile(self.db):
            self.create_db()
        return True

    def create_db(self):
        self.db_manager(tasks.task_creation)

    def get_content(self, column = 'id', data = None):
        output_content = []

        if data:
            curent_task = f"SELECT id, name, book_name, date FROM book WHERE {column} = ?", (data,)
        else:
            curent_task = "SELECT id, name, book_name, date FROM book"

        curent_cursor = self.db_manager(curent_task)
        for id, name, book_name, date in curent_cursor.fetchall():
            output_content.append({'id': id, 'name' : name, 'book_name' : book_name, 'date' : date}) 
        return output_content

    def put_content(self, name, book_name, date = datetime.now()):
        curent_task = "INSERT INTO book(name, book_name, date) VALUES (?,?,?)", (name, book_name, date)
        self.db_manager(curent_task)

    def delete_content(self):
        pass

class Menu:
    def __init__(self) -> None:
        pass

    def show_main_menu(self):
        pass

    def show_details(self):
        pass

    def add_entry(self):
        pass

    def remove_entry(self):
        pass

    def send_reminder(self):
        pass

if __name__ == '__main__':
    pass