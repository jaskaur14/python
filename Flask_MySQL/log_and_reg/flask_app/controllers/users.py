from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user

@app.route('/')
def index():
    return render_template('reg_login.html')

# page that appears once successfully registered/logged in
@app.route('/welcome')
def welcome():
    if 'user_id' not in session: return redirect('/')
    all_users = user.User.get_all_users()
    # get_user_by_email?
    return render_template('welcome.html', user= all_users)

# CREATE
@app.route('/create/user', methods=['POST'])
def create_user():
    if user.User.create_user(request.form):
        return redirect('/welcome')
    return redirect('/')
    #     data = {
    #         "first_name": request.form['first_name'],
    #         "last_name": request.form['last_name'],
    #         "email": request.form['email'],
    #         "password": request.form['password']
    # }

# LOGIN LOGOUT
@app.route('/login', methods=['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/welcome')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



