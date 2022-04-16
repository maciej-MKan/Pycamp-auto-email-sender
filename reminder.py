"""Main module with user interface"""

from datetime import timedelta, datetime
from database import DataBase
from mail_sender import AutoEmail, Message

class DateFormatError(Exception):
    """Exception when script get wrong date formt in entry"""

class Reminder:
    """Class that carries out the user's commands"""
    def __init__(self, database : DataBase) -> None:
        self.dbase = database
        self.dbase.check_if_exists()

    def show_all_entry(self):
        """Return all entrys from data bas"""
        return self.dbase.get_content()

    def add_entry(self, entry : dict):
        """Method to adding entry to data base

        Args:
            entry (dict): {name, mail, book name, date of rent}
        """
        self.dbase.put_content(entry['name'], entry['mail'], entry['book'], entry['date'])

    def remove_entry(self, entry_id : str):
        """Method to remove entry from database

        Args:
            entry_id (str): id of delation entry
        """
        self.dbase.delete_content(data = entry_id)

    def check_laggards(self):
        """Method to serch laggards from all entrys

        Raises:
            DateFormatError: Exception when date format in entry is invalid

        Yields:
            entry['mail'] : e-mail address who keeps the book for more than 30 days
        """
        entrys = self.show_all_entry()
        for single_entry in entrys:
            try:
                entry_date = datetime.strptime(single_entry['date'], '%Y.%m.%d')
                if datetime.now() - entry_date > timedelta(days=30):
                    yield single_entry['mail']
            except ValueError as exc:
                raise DateFormatError(f'\nWrong date format in {single_entry} check it') from exc

    def send_remind(self, args=None):
        """Method to send email with remind

        Args:
            args [list, str or gen]: email addresses to send message

        Yields:
            str: Message about the success or failure of sending the e-mail"""

        recipients_list = []
        if args:
            for arg in args:
                recipients_list.append(self.dbase.get_content(column='mail', data = arg)[0])
        else:
            recipients_list.append(self.dbase.get_content())

        for recipient in recipients_list:
            recipient_address = recipient['mail']
            recipient_name = recipient['name']
            recipient_book = recipient['book_name']
            message = f"""
Hi {recipient_name}!
You have my book "{recipient_book}".
Have you read it yet?"""

            mail = Message(recipient_address, message).create_msg()
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
            for s_entry in all_entry:
                print(f"{s_entry['name']} has book {s_entry['book_name']} from {s_entry['date']}")

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
            e_mail = input('email > ')
            book = input('book name > ')
            date = input('from(yyyy.mm.dd) > ')
            my_reminder.add_entry({'name' : name, 'mail' : e_mail, 'book' : book, 'date' : date})

        if choice == '4':
            all_entry = my_reminder.show_all_entry()
            for rem_entry in all_entry:
                print(f"{rem_entry['id']}. {rem_entry['name']} - {rem_entry['book_name']}")
            sub_choice = input('\nWhich one? ')
            my_reminder.remove_entry(sub_choice)

        if choice == '5':
            break
