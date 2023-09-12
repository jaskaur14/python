from flask_app import app
from flask import render_template, redirect, request, session, flash
# update this
from flask_app.models import sighting, user

# REGISTER method

@app.route('/user/create', methods = ['POST'])
def create_user():
    if user.User.create_user(request.form):
        # update
        return redirect('/dashboard')
    return redirect('/')

# LOGIN/LOGOUT methods

@app.route('/login', methods = ['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/dashboard')
    return redirect('/')

@app.route('/logout')
def logout():
    # update this
    if 'user_id' not in session: return redirect('/')
    session.clear()
    return redirect('/')
