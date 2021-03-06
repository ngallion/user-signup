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
    if re.match("^[a-zA-Z0-9_.-]{3,20}$", username) is None:
        username_error = "Invalid username"
    if password == '':
        password_error = "Please enter a password"
    if re.match("^[a-zA-Z0-9_.-]{3,20}$", password) is None:
        password_error = "Invalid password"
    if verify != password:
        verify_error = "Passwords do not match"
    if re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is None and email != '':
        email_error = "Invalid email"
    
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?user={0}'.format(username))
    else:
        return render_template('signup_form.html', username=username, username_error=username_error, 
        password_error=password_error, verify_error=verify_error, email=email,  
        email_error=email_error)
    

@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.args.get('user')
    return render_template('welcome.html', username=username)


app.run()