from main import DataBase

def test_create_put_get():
    test_db = DataBase(":memory:")
    content = ('test_name', 'test_book', '13.04.2022 12:00')
    test_db.check_if_exists()
    test_db.put_content(content[0], content[1], content[2])
    test_return = test_db.get_content()[0]
    test_return_content = (
        test_return['name'],
        test_return['book_name'],
        test_return['date'])

    assert test_return_content == content

