"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserForm, AccountForm
from app.models import User, Account
from datetime import datetime
import base62
# import sqlite3

###
# Routing for your application.
###


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    account_form = AccountForm()

    if request.method == 'POST':
            if account_form.validate_on_submit():
                fullname = account_form.fullname.data
                username = account_form.username.data
                exists = Account.query.filter_by(username=username).first()
                if not exists:
                    account = Account(fullname, username)
                    db.session.add(account)
                    db.session.commit()
                return render_template('home.html')
                
    else:
        return render_template('login.html', form=account_form)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/users')
def show_users():
    users = User.query.all()

    return render_template('show_users.html', users=users)

@app.route('/add-user', methods=['POST', 'GET'])
def add_user():
    user_form = UserForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Get validated data from form
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            namefull = Account.query.filter_by(username=user_form.name.data).first()
            dt_day = 10000*now.year + 100*now.month + now.day
            valid = base62.encode(dt_day)
            if user_form.valid.data == valid:
            # save user's attendance time to database
                user = User(name = namefull.fullname, classno = user_form.classno.data , attendanceTime = dt_string)
                db.session.add(user)
                db.session.commit()

                flash('Attendance successfully taken!')
                return redirect(url_for('show_users'))

    flash_errors(user_form)
    return render_template('add_user.html', form=user_form)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

@app.route('/password')
def valid():
    now = datetime.now()
    dt_day = 10000*now.year + 100*now.month + now.day
    valid = base62.encode(dt_day)
    return render_template('password.html', valid=valid)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
