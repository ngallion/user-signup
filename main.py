from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup_form.html')

@app.route('/', methods=['POST'])
def submit():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error = "Please enter a username"
    elif re.match("^[a-zA-Z0-9_.-]+$", username) is None:
        username_error = "Invalid username"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"

    if email == '':
        email_error = "Please enter an email address"
    # elif re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]$", email) is None:
    #     email_error = "Invalid email"

    if password == '':
        password_error = "Please enter a password"
    # elif re.match(("^[a-zA-Z0-9_.-]+$", password)) is None:
    #     password_error = "Invalid password"

    if verify != password:
        verify_error = "Passwords do not match"

    return render_template('signup_form.html', username=username, username_error=username_error, 
        password_error=password_error, verify_error=verify_error, email=email,  
        email_error=email_error)

app.run()