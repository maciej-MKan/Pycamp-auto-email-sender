
from sqlite3 import connect
from datetime import datetime
from database import DataBase

def test_create_put_get():
    test_db = DataBase(":memory:")
    content = ('test_name', 'test_book', '13.04.2022 12:00')
    connection = connect(":memory:")
    test_db.cursor = connection.cursor()
    test_db.create_db()
    test_db.put_content(content[0], content[1], content[2])
    test_answer = test_db.get_content()[0]
    test_answer_content = (
        test_answer['name'],
        test_answer['book_name'],
        test_answer['date'])

    assert test_answer_content == content

def test_delete():
    test_db = DataBase(":memory:")
    test_db.cursor = connect(":memory:").cursor()
    test_db.create_db()
    test_db.cursor.execute("INSERT INTO book (name, book_name, date) VALUES (?, ?, ?)", ('test_name', 'test_book', datetime.now()))

    test_db.delete_content()
    test_db.cursor.execute("SELECT * FROM book")

    test_anwer = test_db.cursor.fetchall()

    assert test_anwer == []