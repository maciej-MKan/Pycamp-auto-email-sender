import smtplib
from email.message import EmailMessage
from os import getenv
from dotenv import load_dotenv

class Message:
    def __init__(self,  addres, text) -> None:
        self.addres = addres
        self.content = text

    def create_msg(self):
        msg = EmailMessage()
        msg.set_content(self.content)
        msg['Subject'] = 'Give me my book back'
        msg['From'] = 'me'
        msg['To'] = self.addres

        return msg

class AutoEmail:
    def __init__(self):
        load_dotenv()
        self.mail_box = smtplib.SMTP(getenv('SMTP_SERVER'), getenv('SMTP_PORT'))
        self.mail_box.login(getenv('MAIL_LOGIN'), getenv('MAIL_PASSWORD'))

    def __enter__(self):
        return self.mail_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mail_box.quit()
