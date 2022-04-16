
from sqlite3 import connect
from datetime import datetime
from database import DataBase

def test_create_put_get():
    test_db = DataBase(":memory:")
    contents = (
        ['test_name', 'test_mail', 'test_book', '13.04.2022'],
        ['test_name2', 'test_mail2', 'test_book2', '10.04.2022'],
        ['test_name3', 'test_mail3', 'test_book3', '01.04.2022'])
    connection = connect(":memory:")
    test_db.cursor = connection.cursor()
    test_db.create_db()
    for content in contents:
        test_db.put_content(content[0], content[1], content[2], content[3])
    test_answer = test_db.get_content(data=2)[0]
    test_answer_content = (
        test_answer['name'],
        test_answer['mail'],
        test_answer['book_name'],
        test_answer['date'])

    assert list(test_answer_content) == contents[1]

def test_delete():
    test_db = DataBase(":memory:")
    test_db.cursor = connect(":memory:").cursor()
    test_db.create_db()
    test_db.cursor.execute(
        "INSERT INTO book (name, mail, book_name, date) VALUES (?, ?, ?, ?)",
        ('test_name', 'test_mail', 'test_book', datetime.now())
        )

    test_db.delete_content()
    test_db.cursor.execute("SELECT * FROM book")

    test_anwer = test_db.cursor.fetchall()

    assert test_anwer == []