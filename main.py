
from database import DataBase
from mail_sender import AutoEmail, Message


class Reminder:
    def __init__(self, database : DataBase) -> None:
        self.db = database
        self.db.check_if_exists()

    def show_all_entry(self):
        pass

    def show_details(self):
        pass

    def add_entry(self):
        pass

    def remove_entry(self):
        pass

    def send_remind(self, *args):
        recipients_list = []
        if args:
            for arg in args:
                recipients_list.append(self.db.get_content(column='name', data = arg)[0])
        else:
            recipients_list.append(self.db.get_content())

        for recipient in recipients_list:
            address = recipient['mail']
            name = recipient['name']
            book = recipient['book_name']
            message = f"""
Hi {name}!
You have my book "{book}".
Have you read it yet?"""

            mail = Message(address, message).create_msg()
            with AutoEmail() as mail_box:
                if mail_box.send_message(mail):
                    print(f"nie powiodła się wysyłka do {mail['to']}")
                else:
                    print(f"wysłałem wiadomość do: {mail['to']}")

if __name__ == '__main__':
    Reminder(DataBase('test.db')).send_remind('Jaro', 'Kasia')
