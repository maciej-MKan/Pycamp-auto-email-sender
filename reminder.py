
from datetime import timedelta, datetime
from database import DataBase
from mail_sender import AutoEmail, Message

class DateFormatError(Exception):
    """Exception when script get wrong date formt in entry"""

class Reminder:
    def __init__(self, database : DataBase) -> None:
        self.db = database
        self.db.check_if_exists()

    def show_all_entry(self):
        return self.db.get_content()

    def add_entry(self, entry : dict):
        self.db.put_content(entry['name'], entry['mail'], entry['book'], entry['date'])

    def remove_entry(self, entry_id : str):
        self.db.delete_content(data = entry_id)

    def check_laggards(self):
        entrys = self.show_all_entry()
        for entry in entrys:
            try:
                date = datetime.strptime(entry['date'], '%Y.%m.%d')
                if datetime.now() - date > timedelta(days=30):
                    yield entry['mail']
            except ValueError:
                raise DateFormatError(f'\nWrong date format in {entry} check it')

    def send_remind(self, args=None):
        recipients_list = []
        if args:
            for arg in args:
                recipients_list.append(self.db.get_content(column='mail', data = arg)[0])
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
                    yield f"failure send mail to: {mail['to']}"
                else:
                    yield f"Correct send mail to: {mail['to']}"

if __name__ == '__main__':
    my_reminder = Reminder(DataBase('test.db'))
    while True:
        print('\nMain menu')
        choice = input("""
        1. Show all entry
        2. Send mail to every late
        3. Add entry
        4. Delete entry
        5. Exit

    > """)
        if choice == '1':
            all_entry = my_reminder.show_all_entry()
            for entry in all_entry:
                print(f"{entry['name']} has book {entry['book_name']} from {entry['date']}")

        if choice == '2':
            try:
                mailing_list = my_reminder.check_laggards()
                confirms = my_reminder.send_remind(mailing_list)
                for confirm in confirms:
                    print(confirm)
            except DateFormatError as err:
                print(err)

        if choice == '3':
            name = input('Name > ')
            mail = input('email > ')
            book = input('book name > ')
            date = input('from(yyyy.mm.dd) > ')
            my_reminder.add_entry({'name' : name, 'mail' : mail, 'book' : book, 'date' : date})

        if choice == '4':
            all_entry = my_reminder.show_all_entry()
            for entry in all_entry:
                print(f"{entry['id']}. {entry['name']} - {entry['book_name']}")
            sub_choice = input('\nWhich one? ')
            my_reminder.remove_entry(sub_choice)

        if choice == '5':
            break
