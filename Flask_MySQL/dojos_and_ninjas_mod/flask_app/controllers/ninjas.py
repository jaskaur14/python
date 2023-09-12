# ninjas.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import ninja, dojo

@app.route("/create/ninja")
# , methods = ['GET'])
def create_ninja():
    all_dojos=dojo.Dojo.get_all_dojos()
    # ninja.Ninja.create_ninja(request.form)
    return render_template("create_ninja.html", dojos=all_dojos)

# @app.route("/ninjas")
# def ninjas():
#     this_dojo=dojo.Dojo.get_dojo_by_id_with_ninjas(dojo_id)
#     return render_template("dojo_show.html", dojo=this_dojo)

@app.route("/create/add", methods = ['POST'])
def add():
    ninja.Ninja.create_ninja(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')
