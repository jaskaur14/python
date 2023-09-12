from flask import render_template, request, redirect

from flask_app import app
# ...server.py

from flask_app.models.users import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("second.html", users=User.get_all())
    #renders info from second.html which is basically ALL the users added to the form, second part gets all the data

@app.route('/user/new')
def new():
    return render_template("first.html")
    #renders info from first.html which is basically the new user info form

@app.route('/user/create', methods=['POST'])
def create():
    User.save(request.form)
    # this makes it so we dont have to repeat the same data presented in users.py
        #data dictionary from request.form (has to be same as query string)
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name": request.form["last_name"],
    #     "email": request.form["email"],
    # }
    # when i was trying to add the id, it wouldn't let me do it, said bad getaway
    # User.save(data)
    return redirect('/users')
    # calls on save function established in users.py to return to users page
