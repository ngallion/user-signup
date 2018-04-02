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
    elif password == '':
        password_error = "Please enter a password"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
    elif re.match("^[a-zA-Z0-9_.-]+$", password) is None:
        password_error = "Invalid password"
    elif verify != password:
        verify_error = "Passwords do not match"
    elif re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]$", email) is None and email != '':
        email_error = "Invalid email"
    else:
        return redirect('/welcome?user={0}'.format(username))

    return render_template('signup_form.html', username=username, username_error=username_error, 
        password_error=password_error, verify_error=verify_error, email=email,  
        email_error=email_error)

@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.args.get('user')
    return render_template('welcome.html', username=username)


app.run()