# Pycamp-auto-email-sender
Project from PyCamp module 3
Book rental script

## General info
Program allows you to store information about borrowed books in the database,
add and delete entries,
and send notifications to people who keep the book for more than 30 days

## Technologies
The program was created in Python 3.8 with using the smtplib, email, dotenv, datetime and os libraries and sqlite data base.

## Using

### Before first run
To run the project you must put your email config to .env file. See example.

### Run
To run the project, enter:
```
$ python reminder.py
```
The database will be created automatically.
