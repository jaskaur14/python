from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe

@app.route('/')
def index():
    return render_template('reg_login.html')

@app.route('/recipes')
def recipes():
    if 'user_id' not in session: return redirect('/')
    # this_user = user.User.get_all_users()
    recipes = recipe.Recipe.get_all_recipes()
    # user.User.get_user_by_id ({"id":session['user_id']})
    return render_template('welcome.html', recipes=recipes)

@app.route('/recipes/new')
def new_recipe():
    # all_users=user.User.get_all_users()
    if 'user_id' not in session: return redirect('/')
    return render_template('add_recipe.html')

@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session: return redirect('/')
    if recipe.Recipe.create_recipe(request.form):
        print(request.form)
        return redirect ('/recipes')
    return redirect('/recipes/new')


@app.route('/recipes/<int:id>')
def users_recipe(id):
    if 'user_id' not in session: return redirect('/')
    this_recipe = recipe.Recipe.get_by_id(id)
    return render_template('/view_recipe.html', recipe=this_recipe)

@app.route('/logout')
def logout():
    if 'user_id' not in session: return redirect('/')
    session.clear()
    return redirect('/')

# @app.route('/login', methods=['POST'])
# def login():
#     if user.User.login(request.form):
#         return redirect('/recipes')
#     return redirect('/')

@app.route('/recipes/edit/<int:id>', methods = ['POST', 'GET'])
def edit_recipe(id):
    if 'user_id' not in session: return redirect('/')
    if request.method == 'GET':
        this_recipe = recipe.Recipe.get_by_id(id)
        return render_template('/edit_recipe.html', recipe = this_recipe)
        # if request.method == 'POST":
    if recipe.Recipe.update_recipe(request.form):
        return redirect('/recipes')
    return redirect(f'/recipes/edit/{id}')

@app.route('/recipes/delete/<int:id>')
def delete_recipe_by_id(id):
    if 'user_id' not in session: return redirect('/')
    recipe.Recipe.delete_recipe_by_id(id)
    return redirect('/recipes')