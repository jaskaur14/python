from flask_app import app
from flask import render_template, redirect, request, session, flash
# update this
from flask_app.models import sighting, user

@app.route('/')
def index():
    return render_template('/reg_login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect('/')
    sightings = sighting.Sighting.get_all_sightings()
    return render_template('dashboard.html', sightings = sightings)

# used for just rendering, created a new path for just creating

@app.route('/new/sighting')
def new_sighting():
    if 'user_id' not in session: return redirect('/')
    return render_template('new_sighting.html')

@app.route('/create/sighting', methods = ['POST'])
def create_sighting():
    if 'user_id' not in session: return redirect('/')
    if sighting.Sighting.create_sighting(request.form):
        print(request.form)
        return redirect('/dashboard')
    return redirect('/new/sighting')

# all of these require sighting.id to render, therefore i passed them all in the parameters

@app.route('/show/<int:id>')
def users_sighting(id):
    if 'user_id' not in session: return redirect('/')
    this_sighting = sighting.Sighting.get_sighting_by_id(id)
    return render_template('view_sighting.html', sighting = this_sighting)

@app.route('/edit/<int:id>', methods = ['POST', 'GET'])
def edit_sighting(id):
    if 'user_id' not in session: return redirect('/')
    if request.method == 'GET':
        this_sighting = sighting.Sighting.get_sighting_by_id(id)
        return render_template('edit_sighting.html', sighting = this_sighting)
    # if request.method == 'POST':
    if sighting.Sighting.update_sighting(request.form):
        return redirect('/dashboard')
    return redirect (f'/edit/{id}')

@app.route('/delete/<int:id>')
def delete_sighting_by_id(id):
    if 'user_id' not in session: return redirect('/')
    sighting.Sighting.delete_sighting_by_id(id)
    return redirect('/dashboard')














# @app.route('/login', methods = ['POST'])
# def login():
#     # update this
#     if user.User.login(request.form):
#         # update
#         return redirect('/welcome')
#     return redirect ('/')

# @app.route('/logout')
# def logout():
#     # update this
#     if 'user_id' not in session: return redirect('/')
#     session.clear()
#     return redirect('/')