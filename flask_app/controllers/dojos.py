from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def index():
    dojos = Dojo.getall()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/create_ninja')
def new_ninja():
    return render_template("new_ninja.html")

@app.route('/create', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "age": request.form["age"],
        "dojos_id": request.form["dojo"]
    }
    Ninja.save(data)
    return redirect('/')

@app.route('/<int:dojos_id>/')
def show_ninjas(dojos_id):
    ninjas = Ninja.getdojo(dojos_id)
    print(ninjas)
    return render_template("ninjas.html", all_ninjas = ninjas)

