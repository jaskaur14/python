from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe



@app.route('/user/create', methods = ['POST'])
def create_user():
    if user.User.create_user(request.form):
        return redirect('/recipes')
    return redirect('/')

    # # if not user_id:
    #     return redirect('/')
    # session['user_id'] = user.id
    # return redirect('/recipes')

@app.route('/login', methods=['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/recipes')
    return redirect('/')