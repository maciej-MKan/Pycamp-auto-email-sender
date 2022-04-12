
import sqlite3
import smtplib
from os import path

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

    def check_if_exists(self):
        if not path.isfile(self.db):
            self.create_db()
        return True

    def create_db(self):
        pass

    def get_content(self):
        pass

    def put_content(self):
        pass

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