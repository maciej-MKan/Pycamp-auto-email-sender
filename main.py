
import smtplib
from os import path
from database import DataBase
from email.message import EmailMessage

class Message:
    def __init__(self,  addres, text) -> None:
        self.addres = addres
        self.content = text
        self.msg = self.create_msg()

    def create_msg(self):
        msg = EmailMessage()
        msg.set_content(self.content)
        msg['Subject'] = 'Give me my book back'
        msg['From'] = 'me'
        msg['To'] = self.addres

        return msg

class AutoEmail:
    def __init__(self):
        self.mail_box = smtplib.SMTP("smtp.mailtrap.io", 2525)
        self.mail_box.login("100aaa2dcbda2a", "5f7c644d934550")

    def __enter__(self):
        return self.mail_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mail_box.quit()

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
    mail = Message('alien125@g.pl', 'test text').create_msg()
    with AutoEmail() as mail_box:
        mail_box.send_message(mail)
