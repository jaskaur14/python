# dojos.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo, ninja

# READ
@app.route("/")
def index():
    return redirect("/dojos")

# READ
@app.route("/dojos")
def show_all_dojos():
    all_dojos=dojo.Dojo.get_all_dojos()
    return render_template("dojos.html", dojos=all_dojos)

# CREATE
@app.route("/dojo/add", methods = ['POST'])
def create_dojo():
    dojo_id = dojo.Dojo.create_dojo(request.form)
    return redirect ("/dojos")

# READ
@app.route('/dojos/<int:dojo_id>')
def show(dojo_id):
    # calling the get_one method and supplying it with the id of the dojo we want to get
    this_dojo=dojo.Dojo.get_dojo_by_id_with_ninjas(dojo_id)
    return render_template("dojo_show.html", dojo=this_dojo)