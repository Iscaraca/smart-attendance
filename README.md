# Smart Attendance
A Flask Application that allows the user to take attendance quickly and reliably.
Aimed at schools in Singapore.

## About
This project is for my school's Computing CA, where every student must design a
web app on the topic of "smart schools". I wanted to make an app that demonstrates
Flask-WTF and Flask-SQLAlchemy using a SQLite database, storing both accounts and
attendance timings in two distinct tables, to familiarise myself with OOP concepts.

Students must log in first with a username and full name, then proceed to Confirm
Attendance to book in with their username, class and a validation code displayed
on the teachers' end. After confirming their attendance, their details and time of
confirmation will be shown on Attendance Logs.

Teachers must display a unique validation code on their screens inaccessible to
students. Accessing this code would require navigating to /password.html.
The code will refresh every day at 00 00.

## Instructions for localhost
Clone this repository and cd into the directory.

```
$ git clone https://github.com/Iscaraca/smart-attendance.git
$ cd smart-attendance
```

Ensure you create a virtual environment for this application and install
the necessary libraries from the `requirements.txt` file.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Start the development server

```
$ python run.py 127.0.0.1
```

Browse to http://127.0.0.1:8080/

To reset the users/accounts table, run the following SQL queries on DB Browser:
```
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer primary key autoincrement,
  name string not null,
  classno string not null,
  attendanceTime string not null,
);

DROP TABLE IF EXISTS accounts;
CREATE TABLE users (
  id integer primary key autoincrement,
  fullname string not null,
  username string not null
);
```
